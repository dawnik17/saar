# saar

## Procedure

How to start?

    1. start es cluster
        docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0

    2. Run the app
        python3 app.py

    3. Index and query data
        checkout `app.ipynb`

How to bring news data every hour?

    1. python3 run.py (Run every one hour) - Brings delta news, summarises it and saves it in a file
    2. Index these new articles fetched and summarised - Step number 3 in the above list 

## Resources
1. Elastic Search: https://dylancastillo.co/elasticsearch-python/