kubectl create namespace graylog
helm install --namespace "graylog" -n "mongodb" ../../helm-chart/mongodb-replicaset -f mongo-values.yaml
helm install --namespace "graylog" -n "elasticsearch" ../../helm-chart/elasticsearch -f elastic-values.yaml

