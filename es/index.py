from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import pickle
from typing import List, Dict


def index(data: List[Dict], es: Elasticsearch, es_index_name: str = "news"):
    """
    Indexes a list of news data into an Elasticsearch index while checking for duplicate entries based on the "link" field.

    Parameters:
        data (List[Dict]): A list of dictionaries containing news data to be indexed.
        es (Elasticsearch): An Elasticsearch client instance.
        es_index_name (str, optional): The name of the Elasticsearch index where the data will be indexed (default is "news").

    Returns:
        None

    This function loads news data from a list of dictionaries and checks if each news item already exists in the specified
    Elasticsearch index based on the "link" field. If a news item with the same "link" is not found, it is indexed
    into Elasticsearch. This helps prevent duplicate entries in the index.

    Args:
        data (List[Dict]): A list of dictionaries containing news data.
        es (Elasticsearch): An Elasticsearch client instance.
        es_index_name (str, optional): The name of the Elasticsearch index to which the data will be indexed.

    Example usage:
        data_paths = ["2023-09-09.pkl", "2023-09-08.pkl", "2023-09-07.pkl"]
        data = []

        for data_path in data_paths:
            data.extend(pickle.load(open(data_path, "rb")))

        es = Elasticsearch("http://localhost:9200")
        index(data, es, es_index_name="news")
    """
    # Check if the specified index exists, and create it if it doesn't
    if not es.indices.exists(index=es_index_name):
        es.indices.create(index=es_index_name)
        print(f"Index '{es_index_name}' created.")

    total_data_in_es = es.count()["count"]
    data2index = []

    for idx, news in enumerate(data):
        # Define a query to check if a document with "link" matching "news["link"]" exists
        query = {"query": {"term": {"link.keyword": news["link"]}}}
        response = es.search(index=es_index_name, body=query)

        if response["hits"]["total"]["value"] > 0:
            continue

        data2index.append(
            {"_index": es_index_name, "_id": idx + total_data_in_es, "_source": news}
        )

    if len(data2index) > 0:
        bulk(es, data2index)


if __name__ == "__main__":
    data_paths = ["2023-09-09.pkl", "2023-09-08.pkl", "2023-09-07.pkl"]
    data = []

    for data_path in data_paths:
        data.extend(pickle.load(open(data_path, "rb")))

    index(es_url="http://localhost:9200", data=data, es_index_name="news")
