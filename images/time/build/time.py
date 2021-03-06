from flask import Flask
import datetime
import json
import socket


port = 7002
version = ""

app = Flask(__name__)


@app.route('/time')
def time():
    x = {
      "time": datetime.datetime.now().strftime("%H:%M:%S"),
      "hostname": socket.gethostname(),
      "version": version
    }
    return json.dumps(x)


@app.route('/status')
def status():
    x = {
      "ok": True
    }
    return json.dumps(x)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
