from elasticsearch_dsl.connections import connections

# ElasticSearch configuration
connections.create_connection(hosts=['elasticsearch'])