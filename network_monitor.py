import psutil
import time

def monitor_network():

    net1 = psutil.net_io_counters()

    time.sleep(1)

    net2 = psutil.net_io_counters()

    bytes_sent = net2.bytes_sent - net1.bytes_sent
    bytes_recv = net2.bytes_recv - net1.bytes_recv

    print("Bytes Sent:", bytes_sent)
    print("Bytes Received:", bytes_recv)

    return bytes_sent, bytes_recv


while True:

    sent,recv = monitor_network()

    if sent > 1000000 or recv > 1000000:

        print("⚠️ Suspicious network activity detected")