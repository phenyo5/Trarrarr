import sys
import os
# Modify the environment to prevent dotenv from loading .env files
os.environ["FLASK_SKIP_DOTENV"] = "1"

from flask import Flask, send_from_directory, jsonify
import datetime

# Configure app without loading any .env file
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key_12345')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')

# Sample data for trading signals
SAMPLE_SIGNALS = [
    {
        "id": 1,
        "asset": "BTC/USD",
        "type": "BUY",
        "entryPrice": 48950,
        "stopLoss": 48500,
        "takeProfit": 50000,
        "timestamp": datetime.datetime.now().isoformat(),
        "confidence": "HIGH",
        "timeframe": "1H",
        "analysis": "Strong bullish momentum with support at $48,500."
    },
    {
        "id": 2,
        "asset": "EUR/USD",
        "type": "SELL",
        "entryPrice": 1.0845,
        "stopLoss": 1.0875,
        "takeProfit": 1.0800,
        "timestamp": datetime.datetime.now().isoformat(),
        "confidence": "MEDIUM",
        "timeframe": "4H",
        "analysis": "Weak economic data suggesting bearish pressure."
    },
    {
        "id": 3,
        "asset": "ETH/USD",
        "type": "BUY",
        "entryPrice": 3245,
        "stopLoss": 3200,
        "takeProfit": 3350,
        "timestamp": datetime.datetime.now().isoformat(),
        "confidence": "HIGH",
        "timeframe": "1D",
        "analysis": "Breaking out of consolidation pattern."
    }
]

# Serve static files
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

# API endpoint for signals
@app.route('/api/signals')
def get_signals():
    return jsonify({
        'signals': SAMPLE_SIGNALS,
        'total': len(SAMPLE_SIGNALS),
        'pages': 1,
        'page': 1
    })

# Health check endpoint
@app.route('/api/health')
def health_check():
    return jsonify({'status': 'ok', 'message': 'Trading Signals API is running'})

# Direct run without environment variables
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Only use debug mode in development
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
