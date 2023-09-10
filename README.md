# saar

## Procedure

    1. start es cluster
        docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0

    2. Run the app
        python3 app.py

    3. Index and query data
        checkout `app.ipynb`

## Resources
1. Elastic Search: https://dylancastillo.co/elasticsearch-python/