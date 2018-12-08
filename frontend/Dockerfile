FROM node:slim
COPY /app/package.json /app/package.json
WORKDIR /app
RUN npm install

CMD cd /app && npm run lint && npm run build && if [ ! $CI ]; then npm run serve; fi
EXPOSE 8080