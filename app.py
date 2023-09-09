from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch


app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")


@app.route('/api/filter', methods=['GET'])
def filter_news_by_value():
    """
    sample command line call:

        curl -X GET 'http://localhost:5000/api/filter?source=CNN'
    """
    if request.args:
        data = {key: value for key, value in request.args.to_dict().items()}
        query = {"query": {"match": data}, 
                "sort": [{"datetime": {"order": "desc"}}]}
        
    else:
        query = {
            "query": {"match_all": {}},  # Match all documents
            "sort": [{"datetime": {"order": "desc"}}]
        }

    result = es.search(index="news", body=query)
    hits = result["hits"]["hits"]
    news_list = [hit["_source"] for hit in hits]
    return jsonify(news_list)


if __name__ == '__main__':
    app.run(debug=True)
