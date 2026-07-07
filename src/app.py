from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    if "good" in text.lower():
        sentiment = "Positive"
    elif "bad" in text.lower():
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({
        "input": text,
        "sentiment": sentiment
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Server is running"})

if __name__ == "__main__":
    app.run(debug=True)
