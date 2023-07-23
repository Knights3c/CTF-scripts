import os
import sys
import http.server
import socketserver
import argparse


parser = argparse.ArgumentParser()

# python3 server.py -p PORT
parser.add_argument("-p", "--port", help="Port")

args = parser.parse_args()


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)


def server(port):
    httpd = socketserver.TCPServer(('', port), HTTPRequestHandler)
    return httpd


if __name__ == "__main__":
    port = args.port
    httpd = server(int(port))
    try:
        print(
            f"\nServing HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/)")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n...shutting down http server")
        httpd.shutdown()
        sys.exit()
