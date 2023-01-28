from flask import Flask,jsonify

import docker
import json
app = Flask(__name__)
cli = docker.from_env()
@app.route('/')
def hello():
 
    return cli.version()

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
    app.run(debug=True, host='0.0.0.0')