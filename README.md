# datetimeweb

Messing about with Kubernetes as inspired by Chris Shiels

## Kubernetes - Imperative

    kubectl run date --image datetimeweb/date --replicas 3 --port 7001 --image-pull-policy Never
    kubectl run time --image datetimeweb/time --replicas 3 --port 7002 --image-pull-policy Never
    kubectl run web  --image datetimeweb/web --replicas 3 --port 7000 --image-pull-policy Never

    kubectl expose deployment date --type=ClusterIP
    kubectl expose deployment time --type=ClusterIP
    kubectl expose deployment web  --type=NodePort

    kubectl expose deployment web --type=LoadBalancer --name=web-loadbalancer
    kubectl get service web-loadbalancer

    kubectl delete deployment date
    kubectl delete deployment time
    kubectl delete deployment web
    kubectl delete service date
    kubectl delete service time
    kubectl delete service web
    kubectl delete service web-loadbalancer
