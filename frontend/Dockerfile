FROM node:slim
ADD /app/package.json /app/package.json
WORKDIR /app
RUN npm install

CMD cd /app && npm run build && if [ ! $CI ]; then npm run serve; fi
EXPOSE 8080