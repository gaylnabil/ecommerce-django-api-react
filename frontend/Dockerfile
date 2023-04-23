FROM node:18.13.0-alpine as development

ENV NODE_ENV development

WORKDIR /react_frontend

COPY ./package.json ./
COPY ./package-lock.json ./

COPY ./ ./

RUN yarn install

CMD [ "npm", "start" ]

