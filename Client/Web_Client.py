#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import subprocess
import time

def start_tcpdump():
    """Start capturing packets using tcpdump."""
    # Note: Adjust the path and capture filter as necessary
    return subprocess.Popen(['tcpdump', '-i', 'any', '-w', 'pcap/client_capture.pcap', 'tcp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_tcpdump(process):
    """Stop the tcpdump process."""
    process.terminate()
    process.wait()

def fetch_web_page():
    """Fetch the web page and manage tcpdump."""
    tcpdump_proc = start_tcpdump()
    time.sleep(1)  # Give tcpdump a moment to start
    
    try:
        # Capturing traffic for 10 seconds while accessing the web server
        response = requests.get("http://10.0.0.1:8000")
        print(f"Response from server: {response.status_code}\n{response.text}")
        time.sleep(10)  # Keep the session open for 10 seconds to capture packets
    finally:
        stop_tcpdump(tcpdump_proc)

if __name__ == "__main__":
    fetch_web_page()
