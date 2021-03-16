# Akc-hedwig
Centralize logging solution for Akachain platform

## Installation Guide Using Sh
This project using helm to install. Install in order 1.prequisite -> 2.graylog -> 3.fluentbit. There is a deploy.sh file in each folder, just run this file to complete install.  
In step 2.Graylog, an ingress and a host name must be defined in values.yaml file (default ingress is nginx). 
## Create stream by script
We can route logs to stream by rules. To create stream, follow this guide  [https://docs.graylog.org/en/3.1/pages/streams.html]  
or use API instead:  
```curl -i -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'X-Requested-By: cli' -u $USERNAME:@PASSWORD 'https://$URL/api/streams?pretty=true' -d '{ "title": "stream1", "description": "stream1","rules": [{"field": "namespace_name","type": 1,"value": "test"},{"field": "pod_name","type": 6,"value": "test"}],"content_pack": null,"matching_type": "AND","remove_matches_from_default_stream": false,"index_set_id": "$INDEX_SET_ID"}'```
## Caution
Elasticsearch is not allow delete index automatically. So we will put an api to elasticsearch-client pod to allow delete index:

```kubectl port-forward --namespace graylog elasticsearch-client-xxxxxxx 9200:9200  ```  

```curl -X PUT "localhost:9200/_all/_settings?pretty" -H 'Content-Type: application/json' -d '{"index.blocks.read_only_allow_delete": null}'```