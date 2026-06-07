import time
import requests
import psutil
import platform

SERVER_URL = "https://your-app.onrender.com/upload"

def get_data():
    return {
        "os": platform.system(),
        "os_version": platform.mac_ver()[0],
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv,
        "battery": psutil.sensors_battery().percent if psutil.sensors_battery() else None
    }

while True:
    try:
        data = get_data()
        requests.post(SERVER_URL, json=data, timeout=5)
        print("sent:", data)
    except Exception as e:
        print("error:", e)

    time.sleep(10)
