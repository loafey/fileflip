import os
import http.server
import socketserver

def start_server(port, directory):
    if os.path.isdir(directory) == False:
        print("Not a directory")
        exit()

    os.chdir(directory)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("",port), Handler) as httpd:
        print("serving att port", port)
        httpd.serve_forever()

def stop_server():
    httpd.stop_server()
