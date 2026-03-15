import os
import time


def allow_access():

    print("✅ Access Granted")


def challenge_user():

    print("⚠️ Suspicious activity detected")
    print("Verification required!")

    code = "1234"

    user_input = input("Enter verification code: ")

    if user_input == code:
        print("User verified. Access granted.")
    else:
        block_user()


def block_user():

    print("🚨 Intruder detected")
    print("Blocking session...")

    time.sleep(2)

    print("Session terminated")


def send_alert():

    print("📢 ALERT: Suspicious login attempt detected!")