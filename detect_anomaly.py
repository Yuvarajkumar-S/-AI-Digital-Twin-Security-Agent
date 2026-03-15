import pandas as pd
import joblib
import datetime
import psutil
import requests
import random
import time

MODEL_FILE = "anomaly_model.pkl"

print("Loading Digital Twin Model...")

model = joblib.load(MODEL_FILE)


# -----------------------------
# Simulated typing speed
# -----------------------------
def get_typing_speed():

    return random.randint(45, 80)


# -----------------------------
# Get IP
# -----------------------------
def get_ip():

    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "unknown"


# -----------------------------
# Get location
# -----------------------------
def get_location():

    try:
        data = requests.get("https://ipinfo.io/json").json()
        return data.get("city", "unknown")
    except:
        return "unknown"


# -----------------------------
# Running apps
# -----------------------------
def get_running_apps():

    apps = []

    for process in psutil.process_iter():

        try:
            apps.append(process.name())
        except:
            pass

    return apps


# -----------------------------
# Collect behaviour
# -----------------------------
def collect_behavior():

    timestamp = datetime.datetime.now()

    hour = timestamp.hour

    typing_speed = get_typing_speed()

    session_duration = random.randint(1, 200)

    location = get_location()

    apps = get_running_apps()

    apps_used_count = len(apps)

    data = [[
        hour,
        typing_speed,
        session_duration,
        apps_used_count,
        location
    ]]

    df = pd.DataFrame(data, columns=[
        "hour",
        "typing_speed",
        "session_duration",
        "apps_used_count",
        "location"
    ])

    return df


# -----------------------------
# Detect anomaly
# -----------------------------
def detect():

    df = collect_behavior()

    # convert location to numeric
    df["location"] = df["location"].astype("category").cat.codes

    prediction = model.predict(df)

    if prediction[0] == -1:

        print("⚠️ ANOMALY DETECTED")
        print("Possible Intruder!")

    else:

        print("✅ Normal Behavior")


# -----------------------------
# Run continuous monitoring
# -----------------------------
if __name__ == "__main__":

    print("Digital Twin Monitoring Started...")

    while True:

        detect()

        time.sleep(10)