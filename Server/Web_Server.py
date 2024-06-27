
#!/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver

PORT = 8000
MAX_PRINTS = 10
print_count = 0

class LimitedPrintHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global print_count
        if print_count < MAX_PRINTS:
            print("Hello, this is a simple web server!")
            print_count += 1
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><head><title>Sample Web Page</title></head>")
        self.wfile.write(b"<body><h1>Hello, this is a simple web server!</h1></body></html>")

httpd = socketserver.TCPServer(("", PORT), LimitedPrintHTTPRequestHandler)
print(f"Serving HTTP on 0.0.0.0 port {PORT} ...")
httpd.serve_forever()
