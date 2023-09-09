import os
import pickle
from tqdm import tqdm
from saar.data.production import get_google_news
from saar.infer import Infer
from saar.utils import deduplicate_list_of_dicts, get_full_news

# fetch news
news = get_google_news(use_method="search")
news += get_google_news(use_method="get_news")

# deduplicate news
news = deduplicate_list_of_dicts(news, keys_to_check=["link"])

"""
this is a way to getthe urls already processed
just to take out the delta
and process the new urls only
"""
title_store_path = ""
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
    summary_adapter_path = "./checkpoint/summary/"
    title_adapter_path = "./checkpoint/title/"

    infer = Infer(
        summary_adapter_path=summary_adapter_path, title_adapter_path=title_adapter_path
    )

    # generate summary
    news = infer(mode="summary", data=news)

    # generate title
    # NOTE: Title generation needs summary already generated as "generated_summary" key in the news dict
    news = infer(mode="title", data=news)

"""
save the delta news
"""
