"""
This Python script extracts and curates full news articles from a given URL using the Newspaper3k library. It performs the following tasks:

1. Imports necessary libraries: 'newspaper', 're', 'nltk', and 'datetime'.
2. Downloads and installs the 'punkt' tokenizer from the NLTK library.
3. Defines a regular expression pattern to remove characters not on the QWERTY keyboard.
4. Specifies a list of phrases to remove from the article content.
5. Defines the 'remove_phrases' function to remove specific phrases from a string.
6. Defines the 'curate_article' function, which:
   - Removes non-QWERTY keyboard characters.
   - Removes "Advertisement" sections.
   - Reduces multiple consecutive newlines to a maximum of two.
   - Removes content following specified phrases.
   - Normalizes whitespace and strips leading/trailing whitespace.

7. Defines the 'get_full_news' function, which:
   - Takes a dictionary 'news' containing a 'link' to the article URL.
   - Downloads, parses, and performs natural language processing on the article using Newspaper3k.
   - Curates the article content using 'curate_article'.
   - Applies several checks:
     - It checks if the article is considered media news (e.g., videos) or if it contains less than 50 words, in which case it returns None.
     - If 'image_url' is not in the news dictionary, it sets it to the top image from the article.
     - It checks for a publication date in the article metadata and adds it to 'date' and 'datetime' in the news dictionary.
     - If 'title' is not in the news dictionary, it sets it to the article title.
   - Finally, it returns the curated news dictionary.

Note: This script assumes that the 'newspaper3k' library is installed and that you have an active internet connection to fetch and parse articles.
"""


from newspaper import Article
import re
import nltk
from datetime import datetime
from typing import Dict


nltk.download("punkt")
pattern = re.compile(r'[^a-zA-Z0-9`~!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\| -]')
phrases_to_remove = [
    "Sign In",
    "Want to read more?",
    "Already have an account?",
    "To continue reading",
]


def remove_phrases(string, phrases):
    pattern = "|".join(re.escape(phrase) for phrase in phrases)
    result = re.split(pattern, string)
    return result[0]


def curate_article(article):
    # Remove characters not on the QWERTY keyboard
    article = pattern.sub("", article)

    # Remove "Advertisement" sections
    curated_article = re.sub(r"Advertisement", "", article)

    # Remove extra spaces and new lines
    curated_article = re.sub(r"\n{3,}", "\n\n", curated_article)

    # Remove everything after the stop phrases
    curated_article = remove_phrases(curated_article, phrases_to_remove)

    # routine curation
    curated_article = re.sub(r"\s+", " ", curated_article)
    curated_article = curated_article.strip()

    return curated_article


def get_full_news(news: Dict):
    url = news["link"]

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

    except:
        return

    full_text = curate_article(article.text)

    # failure criteria
    if article.is_media_news() or len(full_text.split()) < 50:
        return

    news["full_text"] = full_text

    if "image_url" not in news:
        news["image_url"] = article.top_image

    # check for date
    is_date = "pdate" in article.meta_data

    if "date" not in news and is_date:
        news["date"] = datetime.strptime(str(article.meta_data["pdate"]), "%Y%m%d")

    if "datetime" not in news and is_date:
        news["datetime"] = datetime.strptime(str(article.meta_data["pdate"]), "%Y%m%d")

    # check for title
    if "title" not in news:
        news["title"] = article.title

    return news


if __name__ == "__main__":
    # Example usage:
    news_article = {"link": "https://example.com/news-article-url"}

    result = get_full_news(news_article)

    if result:
        print("Curated News Article:")
        print("Title:", result.get("title", "N/A"))
        print("Publication Date:", result.get("date", "N/A"))
        print("Image URL:", result.get("image_url", "N/A"))
        print("Full Text:", result.get("full_text", "N/A"))
    else:
        print("Failed to retrieve or curate the news article.")
