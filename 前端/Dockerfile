FROM node:10 AS tsiantuan
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1-alpine
#error_page  404              /404.html;
RUN sed 's/#error/error/g' -i /etc/nginx/conf.d/default.conf
COPY --from=tsiantuan /app/build /usr/share/nginx/html
COPY --from=tsiantuan /app/build/index.html /usr/share/nginx/html/404.html
