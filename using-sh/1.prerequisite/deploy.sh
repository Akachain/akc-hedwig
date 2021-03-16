kubectl create namespace graylog
helm install --namespace "graylog" -n "mongodb" ./mongodb-replicaset -f mongo-values.yaml
helm install --namespace "graylog" -n "elasticsearch" ./elasticsearch -f elastic-values.yaml

