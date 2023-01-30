# flask-dockerengine
 basic flask server that communicate with local docker engine(windows)
 init the server
 1) py -m venv env
 2) .\env\Scripts\activate
 3) pip install requests
 4) exit deactivate


run the docker container with

docker run -p 5000:5000  -v /var/run/docker.sock:/var/run/docker.sock flask-server:1.0 -> Exposes the Docker socket from the host to the container.


 