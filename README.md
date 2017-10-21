# docker-flask-sample
Docker container with Python 2.7 and Flask (Sample from Get Started)

This container was bringin from Docker Get Started Page.

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
5. Locate to `http://<ip-address/localhost/your-machine-vhosts-name>:4000` from your current browser

Want to stop? Run `docker container stop $(docker container ls -a -q)`

To Remove containers Run `docker container rm $(docker container ls -a -q)`

To see list of container running, use `docker ps`.

### Thank you. And happy coding!