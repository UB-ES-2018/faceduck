from elasticsearch_dsl.connections import connections

FRONTEND_HOST = "faceduck.xyz"
FRONTEND_PATHS = [
    '/',
    '/about',
    '/wall',
    '/profile',
    '/search'
]

# ElasticSearch configuration
connections.create_connection(hosts=['elasticsearch'])
