# Edit the Dockerfile and build it

> sudo docker build -t ryanckhung/ryannginx01 .
> sudo docker run -d -p 8087:80 --name=ryan-nginx-01 ryanckhung/ryannginx01
> curl localhost:808 (in the host)
> Success! The page is loaded

# Now create 3 nginx frontend which load /red, /green, /blue

> cd ./red
> sudo docker build -t ryanckhung/ryannginx_red .
> cd ../green
> sudo docker build -t ryanckhung/ryannginx_green .
> cd ../blue
> sudo docker build -t ryanckhung/ryannginx_blue .
> try it in local
> sudo docker run -d -p 8087:80 --name=ryan-nginx-blue ryanckhung/ryannginx_blue
> curl in host
> curl localhost:8087
> Create the repository in docker hub. Then push it by
> docker login
> docker push ryanckhung/ryannginx_red
> docker push ryanckhung/ryannginx_green
> docker push ryanckhung/ryannginx_blue
