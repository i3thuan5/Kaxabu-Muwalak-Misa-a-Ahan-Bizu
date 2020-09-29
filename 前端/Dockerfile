FROM node:10 AS tsiantuan
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.16.0-alpine
COPY --from=tsiantuan /app/build /usr/share/nginx/html
