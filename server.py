from flask import Flask,jsonify
import socket
from flask import request
import docker
app = Flask(__name__)
cli = docker.from_env()
@app.route('/')
def hello():
    return cli.version()


@app.route('/req')
def req():
    req_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    user_request = {
        "reqlip": req_ip,
        "method": request.method,
        "url": request.url,
        "host":"request.host",
        # "headers": dict(request.headers),
        "client_ip": request.remote_addr,
    }
    return str(user_request)


@app.route('/containers', methods=['GET'])
def get_containers():
    containers = []
    for container in cli.containers.list(all=True):
        containers.append({
            "container_id": container.short_id,
            "image": container.image.tags[0],
            "command": container.attrs['Config']['Cmd'],
            "created": container.attrs['Created'],
            "status": container.status,
            "ports": container.attrs['NetworkSettings']['Ports']
        })
    return jsonify(containers)

@app.route('/containers/running',methods=['GET'])
def Runningcontainers():
    containers = cli.containers.list(filters={"status": "running"})
    container_list = []
    for container in containers:
        container_list.append(container.name)
    return jsonify(container_list)


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
