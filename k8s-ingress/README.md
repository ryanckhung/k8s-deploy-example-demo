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

# create the k8s pod and svc
./k8s/red-pod.yaml
./k8s/green-pod.yaml
./k8s/blue-pod.yaml
> cd k8s
> kubectl apply -f=red-pod.yaml 
> kubectl apply -f=green-pod.yaml 
> kubectl apply -f=blue-pod.yaml
apply the service
> kubectl apply -f red-svc.yaml
> kubectl apply -f green-svc.yaml
> kubectl apply -f blue-svc.yaml

check connectivity
> kubectl exec pod/red-pod -- curl blue-svc:8088

apply ingress rule
> kubectl apply -f ingress.yaml

check the ip of the node
> kubectl get nodes -o wide (get the Internal-IP; in this example it is 192.168.99.100)

load the page
> curl 192.168.99.100/red
> curl 192.168.99.100/green
> curl 192.168.99.100/blue
