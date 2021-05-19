# fluent-bit-docker-image
This docker image is clone from [https://github.com/fluent/fluent-bit/tree/master/dockerfiles]. Some lua library is added to Dockerfile.  
To use this image, change image in fluentbit-deamonset to 
```
docker.pkg.github.com/akachain/akc-hedwig/custom-fluentbit:v1
``` 
and update configmap to use lua script:
```
[INPUT]
        name                    tail
        tag                     docker.<container_id>
        tag_regex               (?<container_id>[^/]+)-json\.log$
        path                    /var/lib/docker/containers/*/*-json.log
        db                      /var/log/fluent-bit-docker.pos
        parser                  docker
        docker_mode             true
        buffer_chunk_size       64k
        buffer_max_size         64k
        mem_buf_limit           5MB
        refresh_interval        10
        Docker_Mode             On
        Docker_Mode_Parser      first_line_docker
        Skip_Long_Lines         On
        Multiline_Flush         5
[FILTER]
        name                    parser
        match                   docker.*
        key_name                log
        parser                  json
[FILTER]
    name                    lua
    match                   docker.*
    script                  filters.lua
    call                    enrich
[PARSER]
    Name        first_line_docker
    Format      regex
    Regex       (?<timestamp>[0-9]{2,4}\-[0-9]{1,2}\-[0-9]{1,2} [0-9]{1,2}\:[0-9]{1,2}\:[0-9]{1,2})
filters.lua: |
  cjson = require("cjson")

  cache = {}

  local function get_metadata(container_id)
      -- Read config file
      local config_file_path = "/var/lib/docker/containers/" .. container_id .. "/config.v2.json"
      local config_file = io.open(config_file_path, "rb")
      if not config_file then
          return nil
      end
      local config_json = config_file:read("*a")
      config_file:close()

      -- Map json config
      local config = cjson.decode(config_json)

      return {
          id = config.ID,
          name = config.Name:gsub("^/", ""),
          hostname = config.Config.Hostname,
          image = config.Config.Image,
          image_id = config.Image,
          labels = config.Config.Labels
      }
  end

  function enrich(tag, timestamp, record)
      -- Get container id from tag
      local container_id = tag:match("docker%.(.+)")
      if not container_id then
          return 0, timestamp, record
      end

      -- Get metadata from cache or config
      local metadata = cache[container_id]
      if not metadata then
          metadata = get_metadata(container_id)
          if metadata then
              cache[container_id] = metadata
          end
      end

      if metadata then
          record.docker = metadata
      end

      if (metadata.labels["io.kubernetes.pod.name"] == nil) then
          return 2, timestamp, record
      end

      return -1
  end
```
To pull this image, a secret must be created:
```
kubectl create secret docker-registry github-pull-image --docker-server=docker.pkg.github.com --docker-username=USERNAME --docker-password=PASSWORD/TOKEN --docker-email=EMAIL -n graylog
```
Then reset fluentbit-deamonset to pull this custom fluentbit image
