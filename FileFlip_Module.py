import os
from stem.control import Controller
from flask import Flask
from flask.ext.autoindex import AutoIndex
import os

def start_server(port, directory):
    os.chdir(directory)
    app = Flask("Files")
    AutoIndex(app, browse_root=os.path.curdir)
    port = port
    host = "127.0.0.1"
    app.run(port=port)

def start_server_tor(port, directory):
    os.chdir(directory)
    app = Flask("Files")
    AutoIndex(app, browse_root=os.path.curdir)
    #port = 5000
    host = "127.0.0.1"
    hidden_svc_dir = "c:/temp/"

    print (" * Getting controller")
    controller = Controller.from_port(address="127.0.0.1", port=9151)
    try:
        controller.authenticate(password="")
        controller.set_options([
            ("HiddenServiceDir", hidden_svc_dir),
            ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
            ])
        svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
        print (" * Created host: %s" % svc_name)
    except Exception as e:
        print ("e")
    
    app.run(port=port)


start_server_tor(8000, "c:\\")
#start_server(8000, "c:\\")