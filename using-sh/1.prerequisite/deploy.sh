kubectl create namespace graylog
helm install --namespace "graylog" -n "mongodb" stable/mongodb-replicaset -f mongo-values.yaml
helm install --namespace "graylog" -n "elasticsearch" stable/elasticsearch -f elastic-values.yaml

