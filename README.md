# akc-hedwig
Centralize logging solution for Akachain platform

## Installation Guide Using Sh
This project using helm to install. Install in order 1.prequisite -> 2.graylog -> 3.fluentbit. There is a deploy.sh file in each folder, just run this file to complete install.  
In step 2.Graylog, an ingress must be defined in values.yaml file. Ingress's Annotation must be defined, default is nginx. A host name for graylog client must be define. 
## Caution
Elasticsearch is not allow delete index automatically. So we will put an api to elasticsearch-client pod to allow delete index:

```kubectl port-forward --namespace graylog elasticsearch-client-xxxxxxx 9200:9200  ```  

```curl -X PUT "localhost:9200/_all/_settings?pretty" -H 'Content-Type: application/json' -d '{"index.blocks.read_only_allow_delete": null}'```