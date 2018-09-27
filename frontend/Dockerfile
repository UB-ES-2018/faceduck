FROM ubuntu

RUN apt-get update && apt-get install -y npm

CMD cd /app; npm install; npm run serve

EXPOSE 8080