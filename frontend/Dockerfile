FROM ubuntu

RUN apt-get install npm
RUN npm install -q http-server
RUN npm install 
RUN npm run build

EXPOSE 8080
CMD ["npm","run","serve"]
