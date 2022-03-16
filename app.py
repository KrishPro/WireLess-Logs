"""
Written by KrishPro @ KP
"""

from pyngrok import ngrok
from flask import Flask, render_template

# Uncomment below line to authenticate your ngrok
# ngrok.set_auth_token("<NGROK_AUTH_TOKEN>")

def start_server(port=5000):
    app = Flask(__name__)

    @app.route("/")
    def home_page():
        return render_template("index.html")

    @app.route("/msg/<string:message>")
    def log_message(message):
        print(message)
        return "[OK] [Message Sent]"

    app.run(port=port)


if __name__ == "__main__":
    PORT = 5000
    
    print(ngrok.connect(PORT))
    start_server(PORT)

