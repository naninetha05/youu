import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 9000


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "service": "youu"})
        elif self.path == "/":
            self._send(200, {"message": "youu backend running"})
        else:
            self._send(404, {"error": "not found"})


if __name__ == "__main__":
    print(f"youu backend listening on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
