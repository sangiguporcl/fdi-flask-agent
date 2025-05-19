from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/agent/run", methods=["POST"])
def run_agent():
    data = request.get_json()
    scenario_id = data.get("scenario_id")
    segment_name = data.get("segment_name")

    # Example response logic
    result = {
        "scenario_id": scenario_id,
        "segment_name": segment_name,
        "recommendation": "Increase price by 10%",
        "confidence": 0.91
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
