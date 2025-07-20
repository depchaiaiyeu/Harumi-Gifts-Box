from flask import Flask, jsonify, send_from_directory, request
import threading

app = Flask(__name__, static_folder=".")

lock = threading.Lock()
totalRequests = 0

def toCamelCase(s):
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

def camelizeKeys(d):
    return {toCamelCase(k): v for k, v in d.items()}

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
    data = {"total_requests": totalRequests}
    return jsonify(camelizeKeys(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
