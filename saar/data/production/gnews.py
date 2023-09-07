"""
Google News Scraper
This Python script retrieves news articles from Google News based on user-specified topics and parameters. 
It provides a Python function, 'get_google_news', for fetching news articles from Google News.

Usage:
    - To retrieve news articles using search terms, set 'use_method' to "search".
    - To retrieve news articles based on predefined categories, set 'use_method' to "get_news".

Parameters:
    - use_method (str, optional): The method for retrieving news articles. Defaults to "search".
    - disable_tqdm (bool, optional): Whether to disable the tqdm progress bar. Defaults to False.
    - period (str, optional): The time period for which news articles are retrieved. Defaults to "2d" (2 days).

Returns:
    List[Dict]: A list of dictionaries, where each dictionary represents a news article with the following keys:
        - 'title': The title of the news article.
        - 'media': The source or media outlet of the news article.
        - 'date': The publication date of the news article as a string.
        - 'datetime': The publication date of the news article as a datetime object.
        - 'link': The URL link to the full news article.
        - 'category': The category or topic of the news article.

Note:
    - The function can fetch news articles for predefined topics specified in the 'topics' list.
    - The 'use_method' parameter determines whether to search for news articles or get predefined category news.
    - Some data cleaning is applied to the fetched news articles to remove unnecessary information.

For more information about the 'GoogleNews' library and its parameters, refer to its documentation.
"""



from tqdm import tqdm
from GoogleNews import GoogleNews
from typing import List, Dict


topics = ['Top Stories',
          'World',
          'Nation',
          'Business',
          'Technology',
          'Entertainment',
          'Sports',
          'Science',
          'Health',
          'Politics']


def get_google_news(use_method: str="search", 
                    disable_tqdm: bool=False, 
                    period: str="2d") -> List[Dict]:
    
    googlenews = GoogleNews(lang='en', 
                            period=period,
                            encode='utf-8')
    
    results = []

    for topic in tqdm(topics, disable=disable_tqdm):
        if use_method == "search":
            # search news on "topic"
            googlenews.search(topic)
            
            # fetch all pages from google search
            for i in range(2, 10):
                googlenews.get_page(i)
            
        else:
            # directly call the news API
            googlenews.get_news(topic)

        # get results
        result = googlenews.results()
        
        for news in result:
            news["link"] = news["link"].split("&ved")[0]
            news["category"] = topic
            
            del news["img"]
            del news["desc"]
        
        results.extend(result)
        googlenews.clear()

    results = sorted(results, reverse=True, key=lambda d: d['datetime'])
    return results


if __name__ == "__main__":
    """
    Example:
    ---------
    To fetch news articles using the "search" method and predefined topics, use the following code:

        news = get_google_news(use_method="search")

    To fetch news articles using the "get_news" method for predefined categories, use:

        news += get_google_news(use_method="get_news")

    Sample News Dictionary:
    -------------------------
        A sample news dictionary returned by the function looks like this:

        {
            'title': '2023 NFL power rankings: Chiefs, Eagles lead our initial list',
            'media': 'FOX Sports',
            'date': '0 hours ago',
            'datetime': datetime.datetime(2023, 9, 6, 9, 39, 36, 481550),
            'link': 'https://www.foxsports.com/stories/nfl/2023-nfl-power-rankings-chiefs-eagles-lead-our-initial-list',
            'category': 'Sports'
        }
    """
    news = get_google_news(use_method="search")
    news += get_google_news(use_method="get_news")