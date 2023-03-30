FROM node:lts-slim as build

ARG PUBLIC_API_URL

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN echo PUBLIC_API_URL=${PUBLIC_API_URL} > .env

RUN npm run build


FROM node:lts-slim

WORKDIR /app

COPY --from=build /app/build .

COPY --from=build /app/package.json .

RUN npm install --omit=dev

CMD node index.js