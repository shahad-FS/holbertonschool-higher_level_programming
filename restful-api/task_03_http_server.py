#!/usr/bin/python3
"""Module for http.server"""
import http.server
import json


PORT = 8000

class Server(http.server.BaseHTTPRequestHandler):
    """Server Class handel the http request"""
    def do_GET(self):
        """Method Handel Get requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type","text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode("utf-8"))    
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

server = http.server.HTTPServer(("", PORT), Server)
server.serve_forever()
