from http.server import HTTPServer, BaseHTTPRequestHandler
from time import sleep
import socket
import datetime
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


    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        print(data_dict)

        now=str(datetime.datetime.now())
        dict2read=""
        path2write = os.getcwd() + '/Web_24/front-init/storage/data.json'
        with open (path2write, 'r') as fr:
            dict2read = fr.read ()
        dict2read = eval (dict2read)
        dict2read[now] = data_dict
        str_2_file = self.parsestr(dict2read)
        with open (path2write, 'w') as fw:
            fw.write (str_2_file)

        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def parsestr(self, dict_from_file):
        string = str (dict_from_file)
        string = string[1:-2]
        string = string.replace(': {',': {\n      ')
        string = string.replace('},','\n   },\n   ')
        string = string.replace(", '",",\n      '")
        string = "{\n   " + string + "\n   }\n}"
        return string


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


def run_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(0)
    server = ip, port
    sock.bind(server)
    try:
        while True:
            data, address = sock.recvfrom(1024)
            print(f'Received data: {data.decode()} from: {address}')
            sock.sendto(data, address)
            print(f'Send data: {data.decode()} to: {address}')

    except KeyboardInterrupt:
        print(f'Destroy server')
    finally:
        sock.close()

def run_client(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    MESSAGE = "Python Web development"
    for line in MESSAGE.split(' '):
        data = line.encode()
        sock.sendto(data, server)
        print(f'Send data: {data.decode()} to server: {server}')
        response, address = sock.recvfrom(1024)
        print(f'Response data: {response.decode()} from address: {address}')
    sock.close()

if __name__ == '__main__':

    UDP_IP = '127.0.0.1'
    UDP_PORT = 5000


    thread_http = Thread(target=run())
    thread_http.start()

    thread_UDP = Thread(target=run_server, args=(UDP_IP,  UDP_PORT))
    thread_UDP.start()

