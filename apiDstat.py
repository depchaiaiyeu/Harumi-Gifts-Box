from flask import Flask, jsonify, send_from_directory
import threading

app = Flask(__name__, static_folder=".")

lock = threading.Lock()
totalRequests = 0

@app.before_request
def countRequests():
    global totalRequests
    with lock:
        totalRequests += 1

@app.route("/")
def serveIndex():
    return send_from_directory(".", "index.html")

@app.route("/api/stats")
def apiStats():
    return jsonify({"totalRequests": totalRequests})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
