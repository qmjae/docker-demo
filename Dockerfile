#FROM imagename:tag
FROM python:latest

#docker init
#docker build -f Dockerfile -t <imagename> .
#docker run -it <imagename>

#Connect to Docker Hub
#for easy access do:
    #docker login --> docker build -f Dockerfile -t <username>/<imagename>:tag . 
    #docker push <username>/<imagename>:tag
    #where tag may be latest or v1.0 etc..
#always remember to expose ports
#docker run -it -p <host_port>:<container_port> <imagename>

CMD ["python", "-m", "http.server", "8000"]