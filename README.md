# datetimeweb

Messing about with Kubernetes as inspired by Chris Shiels


## Kubernetes - Declarative

    kubectl apply -f kubernetes/date.yml
    kubectl apply -f kubernetes/time.yml
    kubectl apply -f kubernetes/web.yml

    curl http://127.0.0.1:7000

    kubectl delete -f kubernetes/date.yml
    kubectl delete -f kubernetes/time.yml
    kubectl delete -f kubernetes/web.yml
