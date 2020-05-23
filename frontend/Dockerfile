FROM node:latest

# create docker container directory where app will be transferred to
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app

RUN npm install

CMD ["npm", "start"]