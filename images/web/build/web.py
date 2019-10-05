import argparse
import json
import requests
import socket

from flask import Flask

defaultport = 7000
version = ""

app = Flask(__name__)


parser = argparse.ArgumentParser()
parser.add_argument('--port', type=str, default=defaultport)
parser.add_argument('--dateendpoint', type=str, default='0.0.0.0:7001')
parser.add_argument('--timeendpoint', type=str, default='0.0.0.0:7002')


args = parser.parse_args()


listenport = args.port
dateendpoint = args.dateendpoint
timeendpoint = args.timeendpoint


@app.route('/')
def dateandtime():
    date_url = "http://{}/date".format(dateendpoint)
    time_url = "http://{}/time".format(timeendpoint)

    date = requests.get(date_url).json()
    time = requests.get(time_url).json()

    return "{} : {}\n{} - {}\n{} - {}\n".format(socket.gethostname(),
                                                version,
                                                date['date'],
                                                date['hostname'],
                                                time['time'],
                                                time['hostname'])


@app.route('/status')
def status():
    x = {
      "ok": True
    }
    return json.dumps(x)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=listenport)
