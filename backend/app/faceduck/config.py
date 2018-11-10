from elasticsearch_dsl.connections import connections

FRONTEND_HOST = "localhost"
FRONTEND_PORT = 8080
FRONTEND_PATHS = [
    '/',
    '/about',
    '/wall',
    '/profile',
    '/search'
]

# ElasticSearch configuration
connections.create_connection(hosts=['elasticsearch'])
