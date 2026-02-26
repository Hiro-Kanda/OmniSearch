FROM node:20-slim

WORKDIR /app

COPY package.json package-lock.json* /app/
RUN npm ci || npm install

COPY . /app
