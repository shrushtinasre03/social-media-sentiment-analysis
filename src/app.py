from flask import Flask, request, jsonify
from src.model import predict_sentiment

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
        <title>SentimentAI | Gracious Analytics</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
            
            :root {
                --glass-bg: rgba(255, 255, 255, 0.08);
                --glass-border: rgba(255, 255, 255, 0.15);
                --text-main: #ffffff;
                --text-muted: #b3b3b3;
                --accent: #d4af37; /* Elegant Gold */
                --accent-hover: #f3c623;
                --success: #4ade80;
                --danger: #f87171;
                --neutral: #a78bfa;
            }

            body {
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e);
                background-size: 400% 400%;
                animation: aurora 15s ease infinite;
                color: var(--text-main);
                display: flex;
                flex-direction: column;
                align-items: center;
                overflow-x: hidden;
            }

            @keyframes aurora {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* Abstract Background Shapes */
            .shape {
                position: absolute;
                filter: blur(80px);
                z-index: -1;
                opacity: 0.6;
            }
            .shape-1 {
                top: -100px; left: -100px;
                width: 400px; height: 400px;
                background: #8b5cf6;
                border-radius: 50%;
            }
            .shape-2 {
                bottom: -150px; right: -50px;
                width: 500px; height: 500px;
                background: #3b82f6;
                border-radius: 50%;
            }

            /* Navbar */
            .navbar {
                width: 100%;
                background: rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                padding: 20px 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-sizing: border-box;
                border-bottom: 1px solid var(--glass-border);
            }

            .logo {
                font-size: 1.8rem;
                font-weight: 700;
                background: linear-gradient(to right, #fff, #d4af37);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: 1px;
            }

            .status-badge {
                display: flex;
                align-items: center;
                gap: 10px;
                background: rgba(74, 222, 128, 0.1);
                color: var(--success);
                padding: 8px 16px;
                border-radius: 30px;
                font-size: 0.9rem;
                font-weight: 500;
                border: 1px solid rgba(74, 222, 128, 0.2);
                box-shadow: 0 0 15px rgba(74, 222, 128, 0.1);
            }

            .status-dot {
                width: 8px;
                height: 8px;
                background-color: var(--success);
                border-radius: 50%;
                box-shadow: 0 0 10px var(--success);
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }
                70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(74, 222, 128, 0); }
                100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
            }

            /* Main Container */
            .container {
                max-width: 1100px;
                width: 90%;
                margin: 50px auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 40px;
            }

            /* Glass Cards */
            .card {
                background: var(--glass-bg);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                padding: 40px;
                border-radius: 24px;
                border: 1px solid var(--glass-border);
                box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 40px 70px rgba(0, 0, 0, 0.4);
                border: 1px solid rgba(255, 255, 255, 0.25);
            }

            h2 {
                margin-top: 0;
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 25px;
                display: flex;
                align-items: center;
                gap: 10px;
            }

            textarea {
                width: 100%;
                height: 140px;
                background: rgba(0, 0, 0, 0.2);
                border: 1px solid var(--glass-border);
                border-radius: 12px;
                padding: 20px;
                color: #fff;
                font-family: inherit;
                font-size: 1rem;
                resize: none;
                margin-bottom: 20px;
                box-sizing: border-box;
                transition: all 0.3s ease;
            }

            textarea::placeholder { color: rgba(255, 255, 255, 0.4); }

            textarea:focus {
                outline: none;
                border-color: var(--accent);
                box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
                background: rgba(0, 0, 0, 0.3);
            }

            button {
                width: 100%;
                background: linear-gradient(135deg, var(--accent), #e6c865);
                color: #1a1a1a;
                border: none;
                padding: 16px;
                border-radius: 12px;
                font-size: 1.1rem;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
            }

            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 15px 25px rgba(212, 175, 55, 0.4);
            }

            #resultBox {
                margin-top: 25px;
                display: none;
                padding: 20px;
                border-radius: 12px;
                background: rgba(0, 0, 0, 0.3);
                border: 1px solid var(--glass-border);
                font-weight: 500;
                font-size: 1.1rem;
                text-align: center;
                animation: fadeIn 0.5s ease-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            /* History Table */
            .table-container {
                max-height: 350px;
                overflow-y: auto;
                padding-right: 10px;
            }

            /* Custom Scrollbar for the table */
            .table-container::-webkit-scrollbar { width: 6px; }
            .table-container::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.05); border-radius: 10px; }
            .table-container::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); border-radius: 10px; }

            table {
                width: 100%;
                border-collapse: collapse;
                font-size: 0.95rem;
            }

            th, td {
                text-align: left;
                padding: 16px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }

            th {
                color: var(--accent);
                font-weight: 600;
                position: sticky;
                top: 0;
                background: rgba(30, 30, 46, 0.9);
                backdrop-filter: blur(10px);
                z-index: 1;
            }

            .badge {
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .badge.positive { background: rgba(74, 222, 128, 0.15); color: var(--success); border: 1px solid rgba(74, 222, 128, 0.3); }
            .badge.negative { background: rgba(248, 113, 113, 0.15); color: var(--danger); border: 1px solid rgba(248, 113, 113, 0.3); }
            .badge.neutral { background: rgba(167, 139, 250, 0.15); color: var(--neutral); border: 1px solid rgba(167, 139, 250, 0.3); }

            .footer {
                margin-top: auto;
                padding: 30px;
                color: rgba(255, 255, 255, 0.5);
                font-size: 0.9rem;
                font-weight: 400;
                text-align: center;
                width: 100%;
                letter-spacing: 1px;
            }

            @media (max-width: 850px) {
                .container { grid-template-columns: 1fr; }
                .navbar { padding: 15px 20px; }
            }
        </style>
    </head>
    <body>
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        
        <div class="navbar">
            <div class="logo">✨ SentimentAI</div>
            <div class="status-badge" id="serverStatus">
                <div class="status-dot"></div>
                API Active
            </div>
        </div>

        <div class="container">
            <!-- Left Column: Input -->
            <div class="card">
                <h2>🔮 Analyze Sentiment</h2>
                <textarea id="userInput" placeholder="Type something fascinating..."></textarea>
                <button onclick="analyzeText()">Reveal Emotion</button>
                
                <div id="resultBox"></div>
            </div>

            <!-- Right Column: History -->
            <div class="card">
                <h2>📜 Analysis Ledger</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Insight Text</th>
                                <th>Verdict</th>
                            </tr>
                        </thead>
                        <tbody id="historyTableBody">
                            <tr><td colspan="2" style="text-align: center; color: rgba(255,255,255,0.4);">No interactions yet...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="footer">
            DEVELOPED BY SHRUSHTI | ROLL NO: 37
        </div>

        <script>
            // Check server health on load
            async function checkHealth() {
                try {
                    const res = await fetch('/health');
                    if(res.ok) {
                        document.getElementById('serverStatus').innerHTML = '<div class="status-dot"></div> API Active';
                    }
                } catch(e) {
                    let badge = document.getElementById('serverStatus');
                    badge.innerHTML = '<div class="status-dot" style="background: var(--danger); box-shadow: 0 0 10px var(--danger);"></div> API Offline';
                    badge.style.background = 'rgba(248, 113, 113, 0.1)';
                    badge.style.color = 'var(--danger)';
                    badge.style.borderColor = 'rgba(248, 113, 113, 0.2)';
                }
            }

            // Fetch history logs
            async function loadHistory() {
                try {
                    const res = await fetch('/history');
                    const data = await res.json();
                    const tbody = document.getElementById('historyTableBody');
                    
                    if (data.length === 0) return;
                    
                    tbody.innerHTML = '';
                    for (let i = data.length - 1; i >= 0; i--) {
                        let text = data[i].text.length > 35 ? data[i].text.substring(0, 35) + '...' : data[i].text;
                        let sentiment = data[i].sentiment.toLowerCase();
                        
                        tbody.innerHTML += `
                            <tr>
                                <td style="color: rgba(255,255,255,0.8);">${text}</td>
                                <td><span class="badge ${sentiment}">${sentiment}</span></td>
                            </tr>
                        `;
                    }
                } catch(e) {
                    console.error("Could not load history");
                }
            }

            // Main analyze function
            async function analyzeText() {
                const text = document.getElementById('userInput').value;
                const resultBox = document.getElementById('resultBox');
                
                if (!text.trim()) return;
                
                resultBox.style.display = 'block';
                resultBox.innerHTML = "<span style='color: var(--accent);'>✨ Processing neural network...</span>";
                
                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: text })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        let sentiment = data.sentiment.toLowerCase();
                        let color = sentiment === 'positive' ? 'var(--success)' : (sentiment === 'negative' ? 'var(--danger)' : 'var(--neutral)');
                        
                        resultBox.innerHTML = `Detected Emotion: <span style="color: ${color}; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">${sentiment}</span>`;
                        document.getElementById('userInput').value = ''; 
                        loadHistory(); 
                    }
                } catch (error) {
                    resultBox.innerHTML = "<span style='color: var(--danger);'>⚠️ Connection disruption detected.</span>";
                }
            }

            checkHealth();
            loadHistory();
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
