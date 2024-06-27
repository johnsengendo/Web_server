
#!/bin/env python3
# -*- coding: utf-8 -*-

import requests
import subprocess
import time

def start_tcpdump():
    """Start capturing packets using tcpdump."""
    return subprocess.Popen(['tcpdump', '-i', 'any', '-w', '/path/to/save/client_capture.pcap', 'tcp and port 8000 and host 10.0.0.1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_tcpdump(process):
    """Stop the tcpdump process."""
    process.terminate()
    process.wait()

def fetch_web_page():
    """Fetch the web page and manage tcpdump."""
    tcpdump_proc = start_tcpdump()
    time.sleep(1)  # Give tcpdump a moment to start
    
    try:
        response = requests.get("http://10.0.0.1:8000")
        print(f"Response from server: {response.status_code}\n{response.text}")
    finally:
        stop_tcpdump(tcpdump_proc)

if __name__ == "__main__":
    fetch_web_page()
