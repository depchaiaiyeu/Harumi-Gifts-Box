from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__, static_folder=".")

totalRequests = 0

@app.before_request
def count_request():
    global totalRequests
    if not request.path.startswith("/api/stats"):
        totalRequests += 1

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/api/stats")
def api_stats():
    return jsonify({"totalRequests": totalRequests})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
