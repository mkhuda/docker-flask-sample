# docker-flask-sample
Docker container with Python 2.7 and Flask (Sample from Get Started)

![Alt text](images/docker-screenshot.png?raw=true "Web Screenshot")

This container was bringin from Docker Get Started Page. I added feature for checking and parsing user agent of visitors.

## Libs Imported
- Flask
- pyyaml
- ua-parser
- user-agents

## Usages
1. Clone this image
2. Run `docker build -t <your_whathever_image_name> .` (ended with dot)
3. Run `docker images` to check images
4. Run `docker run -p 4000:80 <your_whathever_image_name>` or `docker run -d -p 4000:80 <your_whathever_image_name>` to detached container on background
5. Locate to `http://localhost:4000` from your current browser

Want to stop? Run `docker container stop $(docker container ls -a -q)`

To Remove containers Run `docker container rm $(docker container ls -a -q)`

To see list of container running, use `docker ps`.

## Service and Swarm
Docker has a service and swarms feature to demonstrate like load balancing over containers. You need to do is `docker-compose.yml` :

```
version: "3"
services:
  web:
    image: emsi_python_sample:latest
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:
```

I use local image for this project, you don't need a Docker Cloud account.

And then run this following commands to make it:

1. Run `docker swarms init` to initialize swarms
2. Then run `docker stack deploy -c docker-compose.yml pythonproject` to define a new service called *pythonproject*
3. Run `docker service ls` to check running service

![Alt text](images/service-screenshot.png?raw=true "Service Screenshot")

4. Because we ported the app into port 80, you can access this service through `http://localhost:80` and Voila!
5. Refresh it, and make sure container host ID is changed on every hit.

### Thank you. And happy coding!