from flask import Flask, jsonify
import os
import psutil
import time

app = Flask(__name__)

@app.route('/service1')
def service1():
    # Collect system information
    disk_usage = psutil.disk_usage('/').percent
    hostname = os.uname()[1]
    ip = os.popen('hostname -I').read().strip()
    uptime = os.popen('uptime -p').read().strip()

    # Send the response
    response = jsonify(disk_usage=disk_usage, hostname=hostname, ip=ip, uptime=uptime)
    
    # Sleep for 2 seconds after responding
    time.sleep(2)

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
