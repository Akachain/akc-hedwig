# fluent-bit-docker-image
This docker image is clone from [https://github.com/fluent/fluent-bit/tree/master/dockerfiles]. Some lua library is added to Dockerfile.  
To use this image, change image in fluentbit-deamonset to 
```
docker.pkg.github.com/akachain/akc-hedwig/custom-fluentbit:v1
``` 
To pull this image, a secret must be created:
```
kubectl create secret docker-registry github-pull-image --docker-server=docker.pkg.github.com --docker-username=USERNAME --docker-password=PASSWORD/TOKEN --docker-email=EMAIL -n graylog
```
Then reset fluentbit-deamonset to pull this custom fluentbit image
