FROM node:slim

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
RUN npm install -g newman
ADD TRAVIS_ENV.json /TRAVIS_ENV.json
