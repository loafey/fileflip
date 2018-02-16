# pylint: disable=E0401, E0611
import os
from flask_autoindex import AutoIndex
from stem.control import Controller
from flask import Flask
# from flask.ext.autoindex import AutoIndex


def start_server(port, directory):
    print("Starting server normal")
    # output_file.write("Starting server normal")
    os.chdir(directory)
    app = Flask("Files")
    AutoIndex(app, browse_root=os.path.curdir)
    port = int(port)
    try:
        app.run(port=port)
    finally:
        print("Closing Server")


def start_server_tor(port, directory, output_fileer):
    print("Starting server TOR")
    os.chdir(directory)
    app = Flask(__name__)
    AutoIndex(app, browse_root=os.path.curdir)
    print('Connecting to tor')
    with Controller.from_port() as controller:
        controller.authenticate()
        response = controller.create_ephemeral_hidden_service(
            {80: 5000}, await_publication=True)
        print("%s.onion" % response.service_id)
        output_fileer = str(output_fileer)
        output_fileer = output_fileer.replace("\\\\", "/")
        print(output_fileer)
        temp = open(output_fileer, "w")
        temp.write("%s.onion" % response.service_id)
        temp.close()
        try:
            app.run()
        finally:
            print("Stopping server")


def check_tor():
    try:
        with Controller.from_port() as controller:
            controller.authenticate()
            return True
    except Exception:
        return False


if __name__ == "__main__":
    start_server_tor(8000, "c:\\", "hiddenservice.txt")
    start_server(8000, "c:\\")
