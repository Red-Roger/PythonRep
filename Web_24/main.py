from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import urllib.parse
import mimetypes
import pathlib
import os


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        self.path = os.getcwd() + '/Web_24/front-init'
        if pr_url.path == '/':
            self.send_html_file(self.path + '/index.html')
        else:
            if pathlib.Path(self.path).joinpath(pr_url.path[1:]).exists():
                self.path = pathlib.Path(self.path).joinpath(pr_url.path[1:])
                self.send_static()
            else:
                self.send_html_file(self.path + '/error.html', 404)

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(self.path, 'rb') as file:
            self.wfile.write(file.read())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    thread_http = Thread(target=run())
    thread_http.start()

