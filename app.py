import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8080

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        env = os.getenv("ENV", "unknown")

        message = f"Hello from Kubernetes! Version 5.\nEnvironment: {env}\n"

        self.wfile.write(message.encode())

if __name__ == "__main__":
    print(f"Server starting on {HOST}:{PORT}")
    HTTPServer((HOST, PORT), SimpleHandler).serve_forever()

