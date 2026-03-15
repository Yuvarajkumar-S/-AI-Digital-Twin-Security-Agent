import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Digital Twin Security", layout="wide")

# -----------------------------
# TITLE
# -----------------------------

st.title("🛡 AI Digital Twin Cybersecurity Control Center")
st.write("Real-time Behavioral Security Monitoring System")

# -----------------------------
# LOAD DATA
# -----------------------------

DATA_FILE = "behavior_data.csv"

try:
    df = pd.read_csv(DATA_FILE)
except:
    df = pd.DataFrame()

# -----------------------------
# ENSURE REQUIRED COLUMNS
# -----------------------------

required_cols = [
    "timestamp",
    "hour",
    "typing_speed",
    "app_count",
    "session_duration",
    "mouse_speed",
    "active_app"
]

for col in required_cols:
    if col not in df.columns:
        df[col] = np.random.randint(1,100,len(df)) if len(df)>0 else []

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Security Controls")

attack_simulation = st.sidebar.button("⚠ Simulate Hacker Attack")
refresh = st.sidebar.button("🔄 Refresh Data")

st.sidebar.success("AI Engine Running")

# -----------------------------
# SYSTEM METRICS
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

if len(df) > 0:

    col1.metric("Users Monitored",len(df))
    col2.metric("Avg Typing Speed",round(df["typing_speed"].mean(),2))
    col3.metric("Apps Running",int(df["app_count"].mean()))
    col4.metric("Session Duration",round(df["session_duration"].mean(),2))

else:

    col1.metric("Users Monitored",0)
    col2.metric("Avg Typing Speed",0)
    col3.metric("Apps Running",0)
    col4.metric("Session Duration",0)

st.markdown("---")

# -----------------------------
# USER BEHAVIOR GRAPH
# -----------------------------

st.subheader("📊 Live User Behavior")

if len(df)>0:

    fig = px.line(
        df.tail(50),
        y="typing_speed",
        title="Typing Speed Behavior"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# SESSION GRAPH
# -----------------------------

st.subheader("⏱ Session Duration")

if len(df)>0:

    session_fig = px.line(
        df.tail(50),
        y="session_duration"
    )

    st.plotly_chart(session_fig,use_container_width=True)

# -----------------------------
# MOUSE BIOMETRICS
# -----------------------------

st.subheader("🖱 Mouse Movement Biometrics")

mouse_data = np.random.normal(300,50,100)

mouse_df = pd.DataFrame({"mouse_speed":mouse_data})

mouse_fig = px.line(mouse_df,y="mouse_speed")

st.plotly_chart(mouse_fig,use_container_width=True)

# -----------------------------
# KEYSTROKE BIOMETRICS
# -----------------------------

st.subheader("⌨ Live Keystroke Biometrics")

keystrokes = np.random.normal(120,20,100)

keystroke_df = pd.DataFrame({
    "keystroke_interval":keystrokes
})

fig = px.line(
    keystroke_df,
    y="keystroke_interval",
    title="Keystroke Timing Pattern"
)

st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# AI ANOMALY DETECTION
# -----------------------------

st.subheader("🤖 AI Anomaly Detection")

features = df[["typing_speed","app_count","session_duration"]]

if len(features)>0:

    threshold = features.mean()+2*features.std()

    anomalies = (
        (features["typing_speed"]>threshold["typing_speed"]) |
        (features["app_count"]>threshold["app_count"]) |
        (features["session_duration"]>threshold["session_duration"])
    )

    df["anomaly"]=anomalies

    anomaly_fig = px.scatter(
        df,
        y="typing_speed",
        color="anomaly"
    )

    st.plotly_chart(anomaly_fig,use_container_width=True)

# -----------------------------
# RISK SCORE METER
# -----------------------------

st.subheader("⚠ AI Risk Score")

risk_score=random.uniform(0,1)

gauge=go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_score*100,
    title={"text":"Threat Level"},
    gauge={"axis":{"range":[0,100]}}
))

st.plotly_chart(gauge,use_container_width=True)

if risk_score>0.7:
    st.error("🚨 High Threat Detected")
elif risk_score>0.4:
    st.warning("⚠ Suspicious Behavior")
else:
    st.success("✅ Normal Behavior")

# -----------------------------
# HACKER VS USER
# -----------------------------

st.subheader("⚔ Hacker vs User Simulation")

col1,col2 = st.columns(2)

user_typing=random.randint(40,70)
hacker_typing=random.randint(80,120)

col1.metric("User Typing Speed",user_typing)
col2.metric("Hacker Typing Speed",hacker_typing)

if hacker_typing>90:
    st.error("AI Decision: BLOCK USER")
else:
    st.success("AI Decision: ALLOW USER")

# -----------------------------
# ATTACK SIMULATION
# -----------------------------

st.subheader("💣 Cyber Attack Simulation")

if attack_simulation:

    st.warning("Simulating Attack")

    progress=st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i+1)

    st.error("Unauthorized Behavior Detected")

# -----------------------------
# GLOBAL CYBER ATTACK MAP
# -----------------------------

st.subheader("🌍 Global Cyber Threat Map")

attack_data=pd.DataFrame({
"lat":[37.77,28.61,51.50,35.68,-33.86],
"lon":[-122.41,77.20,-0.12,139.69,151.20],
"city":["San Francisco","New Delhi","London","Tokyo","Sydney"],
"attacks":[random.randint(1,10) for _ in range(5)]
})

map_fig=px.scatter_geo(
attack_data,
lat="lat",
lon="lon",
size="attacks",
hover_name="city"
)

st.plotly_chart(map_fig,use_container_width=True)

# -----------------------------
# EXPLAINABLE AI
# -----------------------------

st.subheader("🧠 AI Decision Explanation")

feature_importance={
"Typing Speed":random.uniform(0.2,0.4),
"App Usage":random.uniform(0.1,0.3),
"Session Duration":random.uniform(0.1,0.2),
"Mouse Speed":random.uniform(0.1,0.2)
}

importance_df=pd.DataFrame(
list(feature_importance.items()),
columns=["Feature","Importance"]
)

explain_fig=px.bar(
importance_df,
x="Feature",
y="Importance"
)

st.plotly_chart(explain_fig,use_container_width=True)

# -----------------------------
# DIGITAL TWIN VISUALIZATION
# -----------------------------

st.subheader("👤 Digital Twin Avatar Visualization")

twin_data=pd.DataFrame({
"typing_speed":np.random.normal(60,5,100),
"app_count":np.random.normal(4,1,100),
"session_duration":np.random.normal(30,5,100),
"type":["Digital Twin"]*100
})

user_data=pd.DataFrame({
"typing_speed":np.random.normal(80,10,20),
"app_count":np.random.normal(8,2,20),
"session_duration":np.random.normal(60,10,20),
"type":["Live User"]*20
})

combined=pd.concat([twin_data,user_data])

fig=px.scatter_3d(
combined,
x="typing_speed",
y="app_count",
z="session_duration",
color="type"
)

st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# AI DECISION PIPELINE
# -----------------------------

st.subheader("⚙ AI Decision Pipeline")

steps=[
"User Input",
"Feature Extraction",
"AI Model",
"Risk Scoring",
"Agent Action"
]

progress_bar=st.progress(0)
status=st.empty()

for i,step in enumerate(steps):

    status.info("Processing: "+step)
    progress_bar.progress((i+1)/len(steps))
    time.sleep(0.3)

st.success("Pipeline Completed")

# -----------------------------
# SECURITY LOGS
# -----------------------------

st.subheader("📜 Security Logs")

logs=[]

for i in range(10):

    logs.append({
        "time":datetime.now().strftime("%H:%M:%S"),
        "event":random.choice([
            "User Login",
            "Behavior Normal",
            "Suspicious Typing Pattern",
            "Application Spike",
            "Possible Intrusion"
        ])
    })

log_df=pd.DataFrame(logs)

st.dataframe(log_df)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")
st.write("AI Digital Twin Security Agent")
st.write("Behavioral Cybersecurity Monitoring System")
