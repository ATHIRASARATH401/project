from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory('.', filename)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory('.', 'favicon.ico'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
