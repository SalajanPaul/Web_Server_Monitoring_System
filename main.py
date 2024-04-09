import requests
import time

def server_status(url):
    try:
        response = requests.get(url, timeout=10)
        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    except (requests.ConnectionError, requests.Timeout):
        return False

def server_monitoring(url_server, verification_interval):
    while True:
        if server_status(url_server):
            print(f"Server {url_server} is online.")
        else:
            print(f"Server {url_server} is offline.")
        time.sleep(verification_interval)


if __name__ == "__main__":
    url_server = "https://www.motocicletekawasaki.ro/"
    verification_interval = 60

    print(f"Monitoring {url_server}...")
    server_monitoring(url_server, verification_interval)