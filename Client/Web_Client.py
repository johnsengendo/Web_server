#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import subprocess
import time

def start_tcpdump():
    """Start capturing packets using tcpdump."""
    # Note: Adjust the path and capture filter as necessary
    if not os.path.exists('boxer'):
        os.makedirs('boxer')
    return subprocess.Popen(['tcpdump', '-i', 'any', '-w', 'boxer/client_capture.pcap', 'tcp and port 8000 and host 10.0.0.1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_tcpdump(process):
    """Stop the tcpdump process."""
    process.terminate()
    process.wait()

def fetch_web_page():
    """Fetch the web page."""
    try:
        # Fetch the web page
        response = requests.get("http://10.0.0.1:8000")
        print(f"Response from server: {response.status_code}\n{response.text}")
    except requests.exceptions.ConnectionError:
        print("Server shut down.")
        raise

if __name__ == "__main__":
    # Start tcpdump
    tcpdump_proc = start_tcpdump()
    time.sleep(1)  # Give tcpdump a moment to start

    try:
        # Keep fetching the web page until the server shuts down
        while True:
            try:
                fetch_web_page()
            except requests.exceptions.ConnectionError:
                print("Server shut down.")
                break
            time.sleep(1)  # Wait for 1 second before fetching the web page again
    finally:
        # Stop tcpdump
        stop_tcpdump(tcpdump_proc)
