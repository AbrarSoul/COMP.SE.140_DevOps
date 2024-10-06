# service1.py
import os
import json
import subprocess
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_system_info():
    info = {
        "IP_address": os.popen('hostname -I').read().strip(),
        "Processes": subprocess.check_output(['ps', '-ax']).decode('utf-8'),
        "Disk_space": subprocess.check_output(['df', '-h']).decode('utf-8'),
        "Uptime": subprocess.check_output(['uptime', '-p']).decode('utf-8')
    }
    return info

@app.route('/')
def index():
    try:
        response = requests.get('http://service2:8200/service2')
        response.raise_for_status()  # Raise an error for bad responses
        service2_info = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except ValueError:
        return jsonify({"error": "Received non-JSON response from service2"}), 500

    return jsonify(service2_info)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)
