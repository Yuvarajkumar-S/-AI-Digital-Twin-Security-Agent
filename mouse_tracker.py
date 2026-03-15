from pynput import mouse
import time
import csv
import os
import math

DATA_FILE = "data/user_behavior.csv"

positions = []

def on_move(x, y):
    positions.append((x,y,time.time()))

def calculate_mouse_features():

    if len(positions) < 2:
        return 0,0

    distance = 0

    for i in range(1,len(positions)):

        x1,y1,t1 = positions[i-1]
        x2,y2,t2 = positions[i]

        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        distance += dist

    duration = positions[-1][2] - positions[0][2]

    speed = distance/duration if duration > 0 else 0

    return speed, distance


def track_mouse():

    with mouse.Listener(on_move=on_move) as listener:

        time.sleep(10)

        listener.stop()

    speed,distance = calculate_mouse_features()

    print("Mouse Speed:",speed)
    print("Mouse Distance:",distance)

track_mouse()