import pandas as pd
import joblib
import random
import datetime
import time

from security_actions import allow_access, challenge_user, block_user, send_alert


MODEL_FILE = "anomaly_model.pkl"

print("Loading Digital Twin Model...")

model = joblib.load(MODEL_FILE)


# simulate behavior
def collect_behavior():

    hour = datetime.datetime.now().hour

    typing_speed = random.randint(40, 120)

    session_duration = random.randint(1, 200)

    apps_used_count = random.randint(1, 10)

    location = random.randint(0, 2)

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


def agent_decision():

    behavior = collect_behavior()

    prediction = model.predict(behavior)

    if prediction[0] == -1:

        print("\n⚠️ Anomaly detected!")

        risk_score = random.random()

        if risk_score < 0.4:

            challenge_user()

        else:

            send_alert()
            block_user()

    else:

        allow_access()


if __name__ == "__main__":

    print("Agentic AI Security System Started...")

    while True:

        agent_decision()

        time.sleep(10)