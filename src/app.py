from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)
history=[]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    sentiment = predict_sentiment (text)
    history.append({
        "text": text,
        "sentiment": sentiment
    })

    return jsonify({
        "input": text,
        "sentiment": sentiment
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Server is running"})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(history)
if __name__ == "__main__":
    app.run(debug=True)
