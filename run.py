import requests
import matplotlib.pyplot as plt
import numpy as np

HA_URL = "http://homeassistant.local:8123/api/states"
HA_TOKEN = "DEIN_TOKEN_HIER"

def fetch_homeassistant_data():
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(HA_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": float(data.get("sensor.temperature", {}).get("state", 22)),
            "humidity": float(data.get("sensor.humidity", {}).get("state", 50))
        }
    else:
        print("Fehler beim Abrufen der Daten:", response.status_code)
        return {}

def plot_garden(data):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    temp = data.get("temperature", 22)
    hum = data.get("humidity", 50)

    size = np.interp(temp, [10, 30], [0.5, 2])
    color = (hum / 100, 0.6, 0.3)

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x) * size

    ax.fill_between(x + 5, 5 + y, 5 - y, color=color, alpha=0.6)
    plt.title("Smarthome-Garten")
    plt.show()

if __name__ == "__main__":
    data = fetch_homeassistant_data()
    plot_garden(data)