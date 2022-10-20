from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/copilot_internal/v2/token")
def get_copilot_token():
    response = {"token": "1", "expires_at": 2600000000, "refresh_in": 900}
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=5001)
