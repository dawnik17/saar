import os
import pickle
import logging
from tqdm import tqdm
from saar.data.production import get_google_news
from saar.infer import Infer
from saar.utils import deduplicate_list_of_dicts, get_full_news
from dotenv import load_dotenv
from datetime import date


load_dotenv()
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s]  [%(levelname)s]  %(message)s"
)

# fetch news
logging.info("fetching news..")
# news = get_google_news(use_method="search")
news = get_google_news(use_method="get_news")

# deduplicate news
news = deduplicate_list_of_dicts(news, keys_to_check=["link"])

"""
this is a way to get the urls already processed
just to take out the delta
and process the new urls only
"""
title_store_path = os.environ["TITLE_STORE_PATH"]
title_store = (
    pickle.load(open(title_store_path, "rb"))
    if os.path.isfile(title_store_path)
    else set()
)

# remove news that is already inserted
news = [new for new in news if new["link"] not in title_store]

# add newly insterted news to title store and save the title store
title_store = title_store.union({new["link"] for new in news})
pickle.dump(title_store, open(title_store_path, "wb"))

"""
get full news
"""
news = [get_full_news(new) for new in tqdm(news)]
news = [new for new in news if new is not None]

"""
run inference
"""
if len(news) > 0:
    # summary adapter, title adapter path
    summary_adapter_path = os.environ["SUMMARY_ADAPTER_PATH"]
    title_adapter_path = os.environ["TITLE_ADAPTER_PATH"]

    logging.info("loading models..")
    infer = Infer(
        summary_adapter_path=summary_adapter_path, title_adapter_path=title_adapter_path
    )

    # batching
    batch = lambda data, batch_size: [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    
    batch_size = int(os.environ["BATCH_SIZE"])
    news = batch(news, batch_size=batch_size)
    
    data = []
    
    logging.info("running inference..")
    for news_batch in tqdm(news):
        # generate summary
        news_batch = infer(mode="summary", data=news_batch)

        # generate title
        # NOTE: Title generation needs summary already generated as "generated_summary" key in the news dict
        news_batch = infer(mode="title", data=news_batch)
        
        data.extend(news_batch)

"""
save the delta news as files
"""
# save delta news seperately
delta_news_path = os.environ["DELTA_NEWS_PATH"]
pickle.dump(data, open(delta_news_path, "wb"))

# append the delta news in today's news to make the data whole
date_wise_news_path = os.environ["DATE_WISE_NEWS_PATH"]
date_wise_news_path = os.path.join(date_wise_news_path, f"{date.today()}.pkl")

if os.path.exists(date_wise_news_path):
    with open(date_wise_news_path, "rb") as file:
        news = pickle.load(file)
else:
    news = []

news.extend(data)
pickle.dump(news, open(date_wise_news_path, "wb"))
