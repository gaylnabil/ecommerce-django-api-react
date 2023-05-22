FROM node:18.13.0-alpine as development

ENV NODE_ENV development

WORKDIR /next_frontend

COPY ./package.json ./
COPY ./package-lock.json ./

COPY ./ ./

RUN yarn install

EXPOSE 3000

CMD [ "npm", "run", "dev" ]