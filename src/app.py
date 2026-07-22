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
        <title>Sentiment Analysis Web App</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
            
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #ffffff;
            }
            .container {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                padding: 40px;
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 25px 45px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 550px;
                width: 90%;
            }
            h1 { 
                margin-bottom: 15px; 
                font-weight: 600;
                background: -webkit-linear-gradient(45deg, #e0c3fc, #8ec5fc);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 2.2em;
            }
            p { 
                color: #b2bec3; 
                margin-bottom: 30px; 
                font-weight: 300; 
                font-size: 1.1em;
            }
            
            textarea {
                width: 100%;
                height: 120px;
                padding: 15px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
                color: #ffffff;
                font-family: inherit;
                font-size: 1em;
                margin-bottom: 25px;
                box-sizing: border-box;
                resize: none;
                transition: all 0.3s ease;
            }
            textarea::placeholder { color: #636e72; }
            textarea:focus { 
                outline: none; 
                border-color: #8ec5fc; 
                background: rgba(255, 255, 255, 0.1);
                box-shadow: 0 0 15px rgba(142, 197, 252, 0.3);
            }
            
            button {
                background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
                color: white;
                border: none;
                padding: 15px 35px;
                border-radius: 30px;
                font-size: 1.1em;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                box-shadow: 0 4px 15px rgba(108, 92, 231, 0.4);
            }
            button:hover { 
                transform: translateY(-3px); 
                box-shadow: 0 8px 25px rgba(108, 92, 231, 0.6); 
            }
            
            #resultBox {
                margin-top: 30px;
                padding: 15px;
                border-radius: 12px;
                background: rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
                font-size: 1.3em;
                font-weight: 600;
                display: none; 
                animation: fadeIn 0.5s ease-out;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .footer {
                margin-top: 40px;
                padding-top: 15px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
                font-size: 0.85em;
                color: #636e72;
                letter-spacing: 1px;
                text-transform: uppercase;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✨ Sentiment AI</h1>
            <p>Type a sentence below to instantly analyze its emotional sentiment!</p>
            
            <textarea id="userInput" placeholder="Enter text here... (e.g., The new layout is absolutely stunning!)"></textarea>
            <br>
            <button onclick="analyzeText()">Analyze Sentiment</button>
            
            <div id="resultBox"></div>
            
            <div class="footer">
                Developed by Shrushti | Roll No: 37
            </div>
        </div>

        <script>
            async function analyzeText() {
                const text = document.getElementById('userInput').value;
                const resultBox = document.getElementById('resultBox');
                
                if (!text.trim()) {
                    resultBox.style.display = 'block';
                    resultBox.innerHTML = "<span style='color: #ff7675;'>Please enter some text first!</span>";
                    return;
                }
                
                resultBox.style.display = 'block';
                resultBox.innerHTML = "⏳ Analyzing...";
                
                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: text })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        let sentimentText = data.sentiment || JSON.stringify(data);
                        let displayColor = '#74b9ff'; // default blue
                        
                        // Add color coding based on the prediction word
                        if (sentimentText.toLowerCase().includes('positive')) {
                            displayColor = '#55efc4'; // green
                        } else if (sentimentText.toLowerCase().includes('negative')) {
                            displayColor = '#ff7675'; // red
                        }
                        
                        resultBox.innerHTML = `Sentiment: <span style='color: ${displayColor}; text-shadow: 0 0 10px ${displayColor};'>${sentimentText.toUpperCase()}</span>`;
                    } else {
                        resultBox.innerHTML = "<span style='color: #ff7675;'>Error processing request.</span>";
                    }
                } catch (error) {
                    resultBox.innerHTML = "<span style='color: #ff7675;'>Server error. Make sure the API is running.</span>";
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    sentiment = predict_sentiment(text)
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
