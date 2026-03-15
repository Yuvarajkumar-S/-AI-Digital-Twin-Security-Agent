import pandas as pd
import datetime
import time
import psutil
import random
import requests
import os
DATA_FILE = "user_behavior.csv"
# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Track session start
SESSION_START = time.time()


# Create dataset file if not exists
if not os.path.exists(DATA_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "hour",
        "day_of_week",
        "typing_speed",
        "session_duration",
        "ip_address",
        "location",
        "active_app",
        "apps_used_count"
    ])

    df.to_csv(DATA_FILE, index=False)


# -----------------------------
# Simulated typing speed
# -----------------------------
def get_typing_speed():

    return random.randint(45, 75)


# -----------------------------
# Get Public IP
# -----------------------------
def get_ip():

    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "unknown"


# -----------------------------
# Get Location using IP
# -----------------------------
def get_location():

    try:
        response = requests.get("https://ipinfo.io/json").json()
        city = response.get("city", "unknown")
        return city
    except:
        return "unknown"


# -----------------------------
# Get running applications
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
# Get active application
# -----------------------------
def get_active_app(apps):

    common_apps = ["chrome.exe", "Code.exe", "discord.exe", "explorer.exe"]

    for app in common_apps:
        if app in apps:
            return app

    if len(apps) > 0:
        return apps[0]

    return "unknown"


# -----------------------------
# Session duration
# -----------------------------
def get_session_duration():

    return int(time.time() - SESSION_START)


# -----------------------------
# Log behaviour
# -----------------------------
def log_behavior():

    timestamp = datetime.datetime.now()

    hour = timestamp.hour
    day_of_week = timestamp.strftime("%A")

    typing_speed = get_typing_speed()

    session_duration = get_session_duration()

    ip_address = get_ip()

    location = get_location()

    apps = get_running_apps()

    apps_used_count = len(apps)

    active_app = get_active_app(apps)

    new_row = {

        "timestamp": timestamp,
        "hour": hour,
        "day_of_week": day_of_week,
        "typing_speed": typing_speed,
        "session_duration": session_duration,
        "ip_address": ip_address,
        "location": location,
        "active_app": active_app,
        "apps_used_count": apps_used_count
    }

    df = pd.read_csv(DATA_FILE)

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv(DATA_FILE, index=False)

    print("Logged Behavior:", new_row)


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":

    print("Digital Twin Learning Mode Started...")

    while True:

        log_behavior()

        time.sleep(10)