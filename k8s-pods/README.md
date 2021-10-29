# Create Virtual Environment
> python3 -m venv /venv

# Activate Virtual Environment
> source ./venv/bin/activate

# After writing all the code, export the library as
# In this example, it shows empty requirement
> pip freeze > requirements.txt 

# For Local Linux Machine without Virtualization
> main.sh
1. this will first set the Linux environment variables
2. load the virtual environment
3. execute the python with arguments 
4. update can be checked with ./data/env.txt and ./data/log.txt


# ============================================================================================================================#
# Build with Dockerfile and simple docker command
goto the folder with Dockerfile, then build with
> docker build -t ryantest .
list the running docker
> docker container ls -a

# Running in container ($  docker run [OPTIONS] IMAGE [COMMAND] [ARG...])
Example 1:
run the docker image by without argument supply; 
it wil run the default argument listed in the Docker file [CMD]
> sudo docker run -d --name=ryan-container ryantest
> sudo docker exec -it ryan-container cat /usr/src/app/data/log.txt
> sudo docker exec -it ryan-container cat /usr/src/app/data/env.txt
you will see that the container run the command as listed in the Dockerfile => ENTRYPOINT and CMD
./data/env.txt sample output as:
None
./data/log.txt sample output as:
HELLO WORLD: 1635316596
HELLO WORLD: 1635316606
HELLO WORLD: 1635316616
> sudo docker container rm -f ryan-container


Example 2: 
with argument durint "run"; the last option is the argument
> sudo docker run -d --name=ryan-container ryantest "NEW ARGUMENT"
> sudo docker exec -it ryan-container cat /usr/src/app/data/log.txt
> sudo docker exec -it ryan-container cat /usr/src/app/data/env.txt
./data/env.txt sample output as:
None
./data/log.txt sample output as:
NEW ARGUMENT: 1635318201
NEW ARGUMENT: 1635318211
> sudo docker container rm -f ryan-container

Example 3: 
with environment variable - env var please refer to main.py, it is nothing related to the Dockerfile
> sudo docker run -d --env=TEST_TOKEN=docker-token --name=ryan-container ryantest 
> sudo docker exec -it ryan-container cat /usr/src/app/data/log.txt
> sudo docker exec -it ryan-container cat /usr/src/app/data/env.txt
./data/env.txt sample output as:
docker-token
./data/log.txt sample output as:
HELLO WORLD: 1635318201
HELLO WORLD: 1635318211
> sudo docker container rm -f ryan-container

Example 4:
push the image to docker hub
> sudo docker login
create a repository called ryantest in docker hub
> sudo docker build -t ryanckhung/ryantest .
> sudo docker push ryanckhung/ryantest

Example 5:
Mount the folder from container to host
> mkdir -p /home/ryanhung/Desktop/temp_folder
> sudo docker run -d --mount type=bind,source=/home/ryanhung/Desktop/temp_folder,target=/usr/src/app/data --name ryan-container ryanckhung/ryantest 
Check the file in host: /home/ryanhung/Desktop/temp_folder
> sudo docker exec -it ryan-container cat /usr/src/app/data/log.txt     (check for the container)
Now delete the container and check the host folder (/home/ryanhung/Desktop/temp_folder) again
> sudo docker container rm -f ryan-container
You can find that the log.txt and env.txt are still under the host folder (/home/ryanhung/Desktop/temp_folder)


# ============================================================================================================================#
# K8S

# load signel pod from local repository (assume ryanckhung/ryantest is built and pushed to Docker hub; minikube is running)
# ./k8s/single_pod.yaml
> kubectl apply -f single_pod.yaml      (image pull from ryanckhung/ryantest)
> kubectl get pods                      (check the running status)
> kubectl exec ryan -- cat /usr/src/app/data/log.txt
Sample Output:
HELLO WORLD: 1635321547
HELLO WORLD: 1635321557
HELLO WORLD: 1635321567
> kubectl exec ryan -- cat /usr/src/app/data/env.txt
Sample Output:
None
> kubectl delete pod ryan


# load single pod with argument
# ./k8s/single_pod_with_args.yaml
> kubectl apply -f single_pod_with_args.yaml
> kubectl get pods
> kubectl exec ryan -- cat /usr/src/app/data/log.txt
Sample Output:
HELLO Pods: 1635321547
HELLO Pods: 1635321557
HELLO Pods: 1635321567
> kubectl exec ryan -- cat /usr/src/app/data/env.txt
Sample Output:
None
> kubectl delete pod ryan


# load single pod with argument and environment variable
# ./k8s/single_pod_with_args.yaml
> kubectl apply -f single_pod_with_args_env.yaml
> kubectl get pods
> kubectl exec ryan -- cat /usr/src/app/data/log.txt
Sample Output:
HELLO Token Pods: 1635321547
HELLO Token Pods: 1635321557
HELLO Token Pods: 1635321567
> kubectl exec ryan -- cat /usr/src/app/data/env.txt
Sample Output:
token-pod
> kubectl delete pod ryan


# load single pod with configmap
# ./k8s/single_pod_with_configmap.yaml
# ./k8s/env_configmap.yaml
> kubectl apply -f env_configmap.yaml 
> kubectl apply -f single_pod_with_configmap.yaml 
> kubectl get pods
> kubectl exec ryan -- cat /usr/src/app/data/log.txt
Sample Output:
HELLO ConfigMap : 1635321547
HELLO ConfigMap : 1635321557
HELLO ConfigMap : 1635321567
> kubectl exec ryan -- cat /usr/src/app/data/env.txt
Sample Output:
token-pod
> kubectl delete pod ryan


# load single pod with host volume
> mkdir -p /home/ryanhung/Desktop/temp_folder
> kubectl apply -f single_pod_with_volume.yaml 
> kubectl exec ryan -- cat /usr/src/app/data/log.txt (check the content)
try to delete the pod and add the pod back, you will find that the data still can assess inside the new pod
> kubectl detele pods/ryan


# use pv and pvc
> kubectl apply -f pv.yaml
> kubectl apply -f pvc1.yaml
> kubectl apply -f pvc2.yaml
> kubectl get pvc               (if it's success, the status="Bound")
> kubectl apply -f single_pod_a_with_pvc.yaml 
> kubectl apply -f single_pod_b_with_pvc.yaml 
> kubectl exec ryan-a -- cat ./data/log.txt
> kubectl exec ryan-b -- cat ./data/log.txt
ryan-a and ryan-b use the same PVC, but their content is isolated
> kubectl detele pods/ryan-a
> kubectl detele pods/ryan-b
> kubectl apply -f pvc3.yaml    (pv is 100Mi, each pvc is 50Mi, but pv1,pv2,pv3 can create at the same time)


