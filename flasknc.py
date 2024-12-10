from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/connect', methods=['POST'])
def connect():
    target_ip = request.form['ip']
    port = request.form['port']
    os.system(f'nc {target_ip} {port}')
    return f"Connecting to {target_ip}:{port}"

if name == '__main__':
    app.run(port=8080)