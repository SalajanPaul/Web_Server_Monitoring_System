from flask import Flask, request, render_template, jsonify
import requests
import threading
import time

app = Flask(__name__)

# Global variable to store server status
server_status_global = {
    "url": "",
    "status": "unknown"
}

def server_status(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except (requests.ConnectionError, requests.Timeout):
        return False

def monitor_server(url, interval):
    global server_status_global
    while True:
        status = server_status(url)
        server_status_global["status"] = "online" if status else "offline"
        server_status_global["url"] = url
        time.sleep(interval)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        interval = int(request.form.get('interval', 60))
        server_status_global["url"] = url
        server_status_global["status"] = "checking..."

        # Start the server monitoring in a separate thread
        monitoring_thread = threading.Thread(target=monitor_server, args=(url, interval), daemon=True)
        monitoring_thread.start()

        return render_template('index.html', url=url, status=server_status_global['status'])
    return render_template('index.html', url=server_status_global["url"], status=server_status_global['status'])

@app.route('/status', methods=['GET'])
def get_server_status():
    return jsonify(server_status_global)

if __name__ == "__main__":
    app.run(debug=True)
