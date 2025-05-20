from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/agent/run", methods=["POST"])
def run_agent():
    # Hardcoded input values
    region = "APAC"
    deal_size = "30000"

    print("Received hardcoded request for region:", region, "deal size:", deal_size)

    # Simulated agent output
    result = {
        "region": region,
        "deal_size": deal_size,
        "recommendation": "Increase price by 10%",
        "confidence": 0.91
    }

    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return "FDI Flask Agent is running."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
