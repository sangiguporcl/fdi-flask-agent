from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/agent/run", methods=["POST"])
def run_agent():
    # Read from form-encoded input
    region = request.form.get("region")
    deal_size = request.form.get("deal_size")

    print("Received region :", region)
    print("Received deal size:", deal_size)

    response = {
        "region": region,
        "deal_size": deal_size,
        "recommendation": "Increase price by 10%",
        "confidence": 0.91
    }

    return jsonify(response)

@app.route("/", methods=["GET"])
def home():
    return "FDI Flask Agent is running."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

