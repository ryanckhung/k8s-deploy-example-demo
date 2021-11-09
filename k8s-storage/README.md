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
