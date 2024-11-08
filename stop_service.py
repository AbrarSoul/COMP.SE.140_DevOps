from flask import Flask, jsonify
import docker
import os
import sys


app = Flask(__name__)


@app.route('/stop', methods=['POST'])
def stop():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            print(f"Closing container: {container.name}")
            container.stop()

        os._exit(0)  # Exits the service, ending docker-compose
        return jsonify({'message': 'All services stopped'}), 200
    except Exception as e:
        print(f"Error stopping services: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting stop_service...")
    app.run(host="0.0.0.0", port=5000, debug=True)