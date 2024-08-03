from flask import Flask, request, jsonify
import random
from .interminal import inConsole
import os

def select(items: list = []):
    return random.choice(items)

locate = Flask(__name__)
console = inConsole()
best_ports = [
    80,
    443,
    8080,
    3000
]

@locate.route("/", methods=["GET", "POST",
                         "PATCH", "PUT", "DELETE"])
def onMain():
    pathes = request.args.get("path")
    if os.path.exists(pathes):
        if os.path.isfile(pathes):
            return open(pathes, 'r').read()
        else:
            return jsonify({
                "path": pathes,
                "exists": True,
                "isfile": False
            })
    else:
        return jsonify({
                "path": pathes,
                "exists": False
            })

def lunchMain():
    port = select(best_ports)
    console.update_message(f"127.0.0.1:{port}")
    locate.run(host="127.0.0.1", port=port)