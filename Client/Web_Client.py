
#!/bin/env python3
# -*- coding: utf-8 -*-

import requests
import subprocess
import time

url = "http://localhost:8000"

for i in range(10):
    response = requests.get(url)
    print(f"Request {i+1}: Response from server: {response.status_code}")
    time.sleep(1)  # wait a second between requests
