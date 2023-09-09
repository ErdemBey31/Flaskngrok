import os
os.system("pip install flask flask-ngrok")
# flask_ngrok_example.py
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
    return "Hello World!"
oc = "boc"
if oc == "boc":
    app.run()
