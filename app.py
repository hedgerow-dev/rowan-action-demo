"""Deliberately vulnerable demo app for the Rowan GitHub Action."""
import os
import pickle

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    return str(os.system("ping -c 1 " + host))


@app.route("/load", methods=["POST"])
def load():
    return str(pickle.loads(request.data))
