# python virtual environment
> python3 -m venv venv

# Activate Virtual Environment
> source ./venv/bin/activate

# install python package like flask
> pip install flask

# run the code
> python main.py

# After writing all the code, export the library as
# In this example, it shows empty requirement
> pip freeze > requirements.txt 


# Build with Dockerfile and simple docker command
> sudo docker build -t ryanckhung/ryanflask .
> sudo docker run -d -p 8087:5000 --name=ryan-flask ryanckhung/ryanflask
> curl http://localhost:8087
Goto docker hub and create a repository ryanflask, then push it to the docker hub
> sudo docker push ryanckhung/ryanflask


# Test ryanckhung/ryanflask with k8s
> minikube status (check if minikube is running up)
> kubectl apply -f ryan-flask.yaml
> kubectl exec -it pods/ryan-flask-pod sh
> curl http://localhost:5000 (curl inside the k8s pod)


# Deploy nginx with 3 replica; use Load Balancer and minikube to explose it to outisde world
> kubectl create deploy nginx --image=nginx --port=80 --replicas=3
> kubectl get pods (check if 3 pods are created)
> kubectl apply -f svc-loadbalancer.yaml
> kubectl get svc  (check the service, you will see that it is in pending stage)       
> minikbue service svc-lb (svc-lb is the service stated in svc-loadbalancer.yaml)

# Deploy alpine with 3 replica; use ClusterIP to connect
> kubectl create deploy alpine --image=alpine --port=80 --replicas=3 -- sleep 3600
> kubectl get pods (try to get into one of the pods)
> kubectl exec -it alpine-5b96b55f45-6cp7l sh (try to ping the other pods inside the current pod. you will find that it's success)
assume the pod/alpine-5b96b55f45-6cp7l is with ip 172.17.0.5, you can't ping this IP from host
> kubectl get svc (no service created for this deployment)
> kubectl expose deploy/alpine --port=80 (expose the deployment to ClusterIP[default])
> kubectl describe svc/alpine (in this example, the CulsterIP=10.104.18.135/ End Point connect to 3 pods with 172.17.0.2/3/5:80)

> kubectl delete svc/alpine
> kubectl expose deploy/alpine --port=80 --type=NodePort
> kubectl get svc (this time ClusterIP=10.99.245.191, with port=80:30431)
> kubectl delete svc/alpine

# Deploy nginx and expose it with NodePort
> kubectl create deploy nginx --image=nginx --port=80 --replicas=3
> kubectl expose deploy/nginx --port=80 --type=NodePort
> kubectl get svc (this example ClusterIP=10.100.182.237, port80:32595)
> kubectl port-forward --address 0.0.0.0 deploy/nginx 32595:80
goto the host and open the browser => http://localhost:32595 (it should work)
goto the other machine and type => http://<host ip>:32595 (it should work)

# single pod with multiple containers inside
use "localhost" to communicate 
http://localhsot:<port-of-container-A>/api/xxx
http://localhsot:<port-of-container-B>/api/yyy

# create two pods; each in it's own services; CLUSTER IP  can call each other by service name;
# Cluster IP only work inside the cluster
> kubectl apply -f ryan-flask-a.yaml -f ryan-flask-b.yaml 
> kubectl get pods --selector=app=ryan-flask-pod-a
> kubectl get pods --selector=app=ryan-flask-pod-b

When service is created, the IP for that service will be fixed; and won't be changed
> kubectl apply -f ryan-flask-svc-a.yaml -f ryan-flask-svc-b.yaml
> kubectl get svc (check the Cluster IP of each created services)
in this example [svc-a/ClusterIP: 10.103.218.140], [svc-b/ClusterIP: 10.107.234.249]

check the end point of the services; 
the endpoints IP may keep changing whe pod created/deleted; but ClusterIP is fixed after created
> kubectl describe svc/svc-a 
> kubectl describe svc/svc-b 
Log into the pod/alpine-a
> kubectl exec -it pod/ryan-flask-pod-a sh
in ryan-flask-pod-a curl the ip of the svc-b; 
then the svc-b will assign a pod to respone it [in this case it's ryan-flask-pod-b]
> curl http://10.107.234.249:80 OR > curl http://svc-b OR > curl svc-b (can't curl svc-a; that's can't curl itself)

short cut
> kubectl exec pod/ryan-flask-pod-a -- curl svc-b

the pods works with "curl svc-b" because of the build in coreDNS
it will base on the service and namespace to route inside the cluster
in this case svc-b is in default namespace, therefore svc-b is good enough
for pod in other namespaces, we need to <service-name>.<namespace>

Delete all the pod and services
> kubectl delete svc/svc-a svc/svc-b
> kubectl delete pod/ryan-flask-pod-a pod/ryan-flask-pod-b