FROM nginx:1.19-alpine
WORKDIR /usr/share/nginx/html/
COPY ./index.html .
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]