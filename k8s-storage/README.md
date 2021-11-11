hostPath: share data between pods within a signle NODE (test for hostPath)
host_vol.yaml
> kubectl apply -f host_vol.yaml
> kubectl exec -it test-hostpath sh
check the /tmp/test.txt file
> cat /tmp/test.txt | wc -l

delete the created pod
> kubectl delete pod test-hostpath
Recreate the pod
> kubectl apply -f host_vol.yaml
> kubectl exec -it test-hostpath sh
check the /test.txt file
> cat /tmp/test.txt | wc -l

the test.txt file should become longer and keep the data from the previous pod


#### IMPORTANT #####
all the kubectl command is running in the host
while the minikube is running in a VM in the same host
kubectl just like a command line tool which access the VM (minikube)
the created pod is auctually running inside the VM but not the host
Therefore the hostPath (specify in the host_vol.yaml file) in inside the VM BUT NOT THE host
you can access the path by
> minikube ssh (running in the host and loginto the VM)
> cd /home/ryanhung/Desktop (check the test.txt)
> cat test.txt




