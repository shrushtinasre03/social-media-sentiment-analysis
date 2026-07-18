from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)
history=[]
@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sentiment Analysis API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background-color: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 15px;
            }
            p {
                color: #596275;
                line-height: 1.6;
                font-size: 1.1em;
            }
            .endpoints {
                margin-top: 30px;
                text-align: left;
                background-color: #f4f6f9;
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid #8ec5fc;
            }
            .endpoints h3 {
                margin-top: 0;
                color: #2c3e50;
            }
            .endpoints ul {
                list-style-type: none;
                padding: 0;
            }
            .endpoints li {
                margin-bottom: 10px;
                color: #34495e;
            }
            .endpoints code {
                background-color: #dfe6e9;
                padding: 5px 8px;
                border-radius: 5px;
                color: #d63031;
                font-weight: bold;
                font-size: 0.9em;
            }
            .footer {
                margin-top: 30px;
                padding-top: 15px;
                border-top: 1px solid #eee;
                font-size: 0.9em;
                color: #a4b0be;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✨ Sentiment Analysis API</h1>
            <p>Welcome! The natural language processing engine is successfully deployed and running. Use the endpoints below to interact with the model.</p>
            
            <div class="endpoints">
                <h3>Available Routes</h3>
                <ul>
                    <li><code>GET /health</code> : Verify server status</li>
                    <li><code>POST /predict</code> : Analyze the sentiment of input text</li>
                    <li><code>GET /history</code> : View previously analyzed text</li>
                </ul>
            </div>
            
            <div class="footer">
                Developed by Shrushti | Roll No: 37
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

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
