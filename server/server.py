#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000


class MyHandler(SimpleHTTPRequestHandler):
    # Make sure .wasm and .bin have proper MIME types
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".wasm": "application/wasm",
        ".bin": "application/octet-stream",
        ".js": "text/javascript",
        "": "application/octet-stream",  # default
    }


if __name__ == "__main__":
    httpd = HTTPServer(("127.0.0.1", PORT), MyHandler)
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
