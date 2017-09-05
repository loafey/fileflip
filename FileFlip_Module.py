import os
from stem.control import Controller
from flask import Flask
from flask.ext.autoindex import AutoIndex
import time
tor_running = False
tor_address = None

def start_server(port, directory):
    print("Starting server normal")
    #output_file.write("Starting server normal")
    os.chdir(directory)
    app = Flask("Files")
    AutoIndex(app, browse_root=os.path.curdir)
    port = port
    host = "127.0.0.1"
    try:
        app.run(port=port)
    finally:
        print("Closing Server")

def start_server_tor(port, directory):
    print("Starting server TOR")
    os.chdir(directory)
    app = Flask(__name__)
    AutoIndex(app, browse_root=os.path.curdir)
    print('Connecting to tor')
    with Controller.from_port() as controller:
        controller.authenticate()
        response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
        print("%s.onion" % response.service_id)
        tor_address = "%s.onion"
        tor_running = True

        try:
            app.run()
        finally:
            print("Stopping server")
start_server_tor(8000, "c:\\")
#start_server(8000, "c:\\")