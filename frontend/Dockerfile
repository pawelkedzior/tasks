FROM node:22.18.0-slim AS development

WORKDIR /frontend

COPY package.json /frontend/package.json
COPY yarn.lock /frontend/yarn.lock

RUN npm install

COPY . /frontend

RUN npm run build

CMD ["node", "/frontend/.output/server/index.mjs"]
