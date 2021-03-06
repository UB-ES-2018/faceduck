#!/bin/bash

export DOCKER_RESTART="no"
export CI=true

docker-compose build
docker-compose up -d
docker-compose run --entrypoint "bash -c '/wait-for-it.sh --timeout=60 elasticsearch:9200 && /wait-for-it.sh --timeout=15 api:5000 && /wait-for-it.sh --timeout=15 frontend:8080 && exit 0'" test_runner
docker-compose run -e CI=true --entrypoint "npm run test:unit -- --coverage" frontend
docker-compose run --entrypoint "bash -c 'newman run /API.postman_collection.json -e /TRAVIS_ENV.json --delay-request 1000'" test_runner
docker-compose run -e CI=true --entrypoint "ash -c 'cd /app; pip install coverage; coverage report'" api
docker-compose down

rm -f backend/app/.coverage
