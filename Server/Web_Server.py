#!/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver

PORT = 8000
MAX_REQUESTS = 10
request_count = 0

class LimitedRequestHTTPServer(socketserver.TCPServer):
    # This flag will allow the server to shut down after handling a certain number of requests
    allow_reuse_address = True

class LimitedRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global request_count
        request_count += 1
        if request_count >= MAX_REQUESTS:
            print("Reached maximum number of requests, shutting down.")
            self.server.shutdown()
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><head><title>Sample Web Page</title></head>")
        self.wfile.write(b"<body><h1>Hello, this is a simple web server!</h1></body></html>")
        print("Hello, this is a simple web server!")

httpd = LimitedRequestHTTPServer(("", PORT), LimitedRequestHandler)
print(f"Serving HTTP on 0.0.0.0 port {PORT} ...")
httpd.serve_forever()