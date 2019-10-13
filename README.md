# datetimeweb

Messing about with Kubernetes as inspired by Chris Shiels

## Dependencies
    virtualenv --python=python3 virtualenv
    . virtualenv/bin/activate
    pip install -r requirements.txt

## Build
    ( cd images/date/build/ ; make build )
    ( cd images/time/build/ ; make build )
    ( cd images/web/build/ ; make build )

## Docker compose
    docker-compose -f compose/docker-compose.yml up -d
    curl http://127.0.0.1:7000
    docker-compose -f compose/docker-compose.yml down

## Kubernetes

    kubectl apply -f kubernetes/date.yml
    kubectl apply -f kubernetes/time.yml
    kubectl apply -f kubernetes/web.yml

    curl http://127.0.0.1:7000

    kubectl delete -f kubernetes/date.yml
    kubectl delete -f kubernetes/time.yml
    kubectl delete -f kubernetes/web.yml
