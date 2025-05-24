```
kubectl explain pod
kubectl api-versions
kubectl explain deployments
kubectl apply -f pod.yaml
kubectl get pods -o wide
kubectl describe pod mlops-pod

kubectl get pods                         # list all running pods in current active namespace
kubectl get pods -n kube-system          # list all running pods in specified namespace
kubectl get pods --all-namespaces        # list all running pods in all namespaces available
kubectl get pods -o wide                 # list all running pods in current active namespace wider output

kubectl describe pod <podname>              # detailed output about a pod in current namespace
kubectl describe pod <podname> -n namespace # detailed output about a pod in current namespace
kubectl describe pod <podname> -o wide      # detailed output about a pod wider output
kubectl describe pod <podname> -o yaml      # detailed manifest file from apiserver yaml format
kubectl describe pod <podname> -o json      # detailed manifest file from apiserver json format

kubectl logs my-pod                                 # dump pod logs (stdout)
kubectl logs -f my-pod                              # stream pod logs (stdout)
kubectl logs -f my-pod -c my-container              # stream pod container logs (stdout, multi-container case)

kubectl exec -it my-pod -- /bin/bash     # get interactive shell of the container in existing pod ( 1 container case )
kubectl exec -it my-pod -c my-container -- /bin/bash # get interative shell of the container in existing pod ( multi container ) 

kubectl expose pod nginx --port=80 --target-port=80  # expose pod as service within the cluster
kubectl expose pod nginx --target-port=80 --type=NodePort # expose pod as service within the cluster & outside of the cluster

kubectl delete pods <podname>                    # delete a pod in current active namespace
kubectl delete pods --all                        # delete all pods 
kubectl delete pod <pod-name> --grace-period=0 --force  # delete pod forcefully



kubectl get svc                         # list all running services in current active namespace
kubectl get svc -n kube-system          # list all running services in specified namespace
kubectl get svc --all-namespaces        # list all running services in all namespaces available
kubectl get svc -o wide                 # list all running services in current active namespace wider output
kubectl get svc --show-labels           # list services with labels
kubectl get svc -l env=prod             # list services with matching labels


kubectl describe svc <svcname>              # detailed output about a service in current namespace
kubectl describe svc <svcname> -n namespace # detailed output about a service in current namespace
kubectl describe svc <svcname> -o wide      # detailed output about a service wider output
kubectl describe svc <svcname> -o yaml      # detailed manifest file from apiserver yaml format
kubectl describe svc <svcname> -o json      # detailed manifest file from apiserver json format

kubectl label svc <svcname> env=prod        # add label to svc
kubectl label svc <svcname> env-            # remove a label

kubectl delete svc <svcname>                    # delete a svc in current active namespace
kubectl delete svc <svcname> -n <my-namespace>  # delete a svc in specified namespace
kubectl delete svc -l env=test                  # delete svc matching labels
kubectl delete svc --all                        # delete all svc
```