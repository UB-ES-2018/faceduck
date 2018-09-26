FROM ubuntu

RUN apt-get update && apt-get install -y npm && npm install -g http-server

CMD cd /app; npm install && npm run build && http-server dist

EXPOSE 8080