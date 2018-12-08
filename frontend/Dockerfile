FROM node:slim
COPY /app/package.json /app/package.json
WORKDIR /app
RUN npm install

CMD cd /app && npm run lint && npm run build && npm run serve
EXPOSE 8080