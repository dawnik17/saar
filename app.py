from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from es.index import index


app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")


@app.route("/api/index", methods=["POST"])
def index_news_data():
    """
    Endpoint to index news data into Elasticsearch.

    Example curl command:
    curl -X POST -H "Content-Type: application/json" -d @news_data.json http://localhost:5000/api/index

    The request should contain a JSON array of news data objects.


    PYTHON EXAMPLE:

        import requests
        import json

        data = [
            {
                "title": "abc",
                "content": "This is the content of the first article.",
                "link": "https://abc.com/news/article",
                "datetime": "2023-09-12T12:00:00Z",
                "summary": "xyz"
            },
            {
                "title": "bbc",
                "content": "This is the content of the second article.",
                "link": "https://bbc.com/news/article",
                "datetime": "2023-09-13T13:00:00Z"
            }
        ]

        api_url='http://localhost:5000/api/index'
        headers = {'Content-Type': 'application/json'}

        response = requests.post(api_url, data=json.dumps(data), headers=headers)
    """
    try:
        data = request.get_json()
        if data:
            index(data=data, es=es, es_index_name="news")
            return "Data indexed successfully", 201
        else:
            return "No data provided in the request", 400
    except Exception as e:
        return str(e), 500


@app.route("/api/filter", methods=["GET"])
def filter_news_by_value():
    """
    Filter news articles based on query parameters and return the results.

    This endpoint allows users to filter news articles stored in an Elasticsearch
    index based on query parameters provided in the URL. The filtered results are
    sorted by the "datetime" field in descending order.

    Parameters:
        size (int, optional): The number of articles to return (default is 100).

    Query Parameters:
        Any query parameter key-value pair provided in the URL will be treated as a
        filter criterion. The function constructs an Elasticsearch query to match
        articles that satisfy all provided criteria.

    Returns:
        list of dict: A list of news articles matching the filter criteria.
        
    EXAMPLE REQUESTS
    -----------------

        COMMAND LINE REQUEST:

            curl -X GET 'http://localhost:5000/api/filter?source=CNN&category=Top%20Stories'

        PYTHON REQUEST:

            import requests

            base_url = 'http://localhost:5000/api/filter'
            query_params = {
                'category': 'Politics',
                'source': "CNN"
            }

            response = requests.get(base_url, params=query_params)

    Example Response:
        [
            {
                "title": "News Article 1",
                "content": "This is the content of the first article.",
                "source": "CNN",
                "category": "Politics",
                "datetime": "2023-09-10T12:00:00Z"
            },
            {
                "title": "News Article 2",
                "content": "This is the content of the second article.",
                "source": "CNN",
                "category": "Politics",
                "datetime": "2023-09-09T14:00:00Z"
            },
            ...
        ]

    """
    default_size = 100
    size = request.args.get('size', default=default_size)

    if request.args:
        # exact keyword match
        data = [
            {"term": {f"{key}.keyword": value}}
            for key, value in request.args.to_dict().items()
            if key != "size"
        ]
        query = {
            "size": size,
            "query": {"bool": {"must": data}},
            "sort": [{"datetime": {"order": "desc"}}],
        }

    else:
        # Sort all documents and return
        query = {
            "size": size,
            "query": {"match_all": {}},
            "sort": [{"datetime": {"order": "desc"}}],
        }

    result = es.search(index="news", body=query)
    hits = result["hits"]["hits"]
    news_list = [hit["_source"] for hit in hits]
    return jsonify(news_list)


@app.route("/api/search", methods=["GET"])
def fuzzy_search_news():
    """
    Perform a fuzzy search on news articles based on a query string.

    This endpoint allows users to perform a fuzzy search on news articles stored in an Elasticsearch index.
    
    Parameters:
        field (str, optional): The field in which to perform the fuzzy search (default is "full_text").
        size (int, optional): The maximum number of search results to return (default is 100).
        query (str): The query string to search for.

    Returns:
        jsonify: A JSON response containing a list of news articles matching the fuzzy search.

    Example:
        To perform a fuzzy search for news articles in the "full_text" field with the query "technology":
        curl -X GET 'http://localhost:5000/api/search?field=full_text&query=technology'
    """
    # default field to query in
    default_field = "full_text"
    field = request.args.get('field', default=default_field)

    # default size
    default_size = 100
    size = request.args.get('size', default=default_size)

    # search query
    query_string = request.args.get("query")

    if not query_string:
        return "Please provide a 'query' parameter for fuzzy search.", 400

    query = {
        "size": size,
        "query": {
            "match": {
                field: {
                    "query": query_string,
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    result = es.search(index="news", body=query)
    hits = result["hits"]["hits"]
    news_list = [hit["_source"] for hit in hits]

    return jsonify(news_list)


if __name__ == "__main__":
    app.run(debug=True)
