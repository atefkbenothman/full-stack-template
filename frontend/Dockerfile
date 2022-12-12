# development
FROM node:16 as react-build

WORKDIR /code

COPY ./app ./

RUN yarn install

RUN yarn build


# production
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=react-build /code/build /usr/share/nginx/html

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
