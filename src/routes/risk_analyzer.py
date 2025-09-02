from flask import Blueprint, request, jsonify
from src.models.user import db, RiskAnalysis
import random
import json
from datetime import datetime

risk_bp = Blueprint('risk', __name__)

# Mock data for different stocks/funds
MOCK_RISK_DATA = {
    "TCS": {
        "risk_score": 35,
        "risk_level": "Safe",
        "reasons": [
            "Strong fundamentals and consistent performance",
            "Low volatility compared to sector average",
            "Stable dividend history"
        ],
        "alternatives": ["NIFTY 50 ETF", "SENSEX ETF", "Large Cap Mutual Fund"]
    },
    "INFY": {
        "risk_score": 42,
        "risk_level": "Safe",
        "reasons": [
            "Established IT services company",
            "Good corporate governance",
            "Moderate volatility"
        ],
        "alternatives": ["NIFTY IT ETF", "Technology Mutual Fund", "SENSEX ETF"]
    },
    "ABC": {
        "risk_score": 85,
        "risk_level": "Risky",
        "reasons": [
            "High volatility in recent weeks",
            "Negative news sentiment from multiple sources",
            "Unusual trading patterns vs historical baseline",
            "Regulatory concerns pending"
        ],
        "alternatives": ["NIFTY 50 ETF", "SENSEX ETF", "Diversified Large-Cap MF", "Liquid Fund (Short-term)"]
    },
    "XYZ": {
        "risk_score": 68,
        "risk_level": "Moderate",
        "reasons": [
            "Elevated volatility over the last 2 weeks",
            "Mixed news sentiment from multiple sources",
            "Unusual trading patterns vs historical baseline"
        ],
        "alternatives": ["NIFTY 50 ETF", "SENSEX ETF", "Diversified Large-Cap MF", "Liquid Fund (Short-term)"]
    },
    "RELIANCE": {
        "risk_score": 45,
        "risk_level": "Safe",
        "reasons": [
            "Large market cap with stable business",
            "Diversified business portfolio",
            "Strong financial position"
        ],
        "alternatives": ["NIFTY 50 ETF", "Energy Sector ETF", "Large Cap Fund"]
    }
}

@risk_bp.route('/risk/analyze', methods=['POST'])
def analyze_risk():
    """Analyze risk for a given stock or fund"""
    data = request.get_json()
    symbol = data.get('symbol', '').upper().strip()
    
    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400
    
    # Check if we have mock data for this symbol
    if symbol in MOCK_RISK_DATA:
        risk_data = MOCK_RISK_DATA[symbol]
    else:
        # Generate random risk data for unknown symbols
        risk_score = random.randint(30, 90)
        if risk_score < 40:
            risk_level = "Safe"
        elif risk_score < 70:
            risk_level = "Moderate"
        else:
            risk_level = "Risky"
        
        risk_data = {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "reasons": [
                "Market volatility analysis pending",
                "Limited historical data available",
                "General market conditions apply"
            ],
            "alternatives": ["NIFTY 50 ETF", "SENSEX ETF", "Diversified Large-Cap MF"]
        }
    
    # Store in database for future reference
    existing_analysis = RiskAnalysis.query.filter_by(symbol=symbol).first()
    if existing_analysis:
        existing_analysis.risk_score = risk_data["risk_score"]
        existing_analysis.risk_level = risk_data["risk_level"]
        existing_analysis.reasons = json.dumps(risk_data["reasons"])
        existing_analysis.alternatives = json.dumps(risk_data["alternatives"])
        existing_analysis.last_updated = datetime.utcnow()
    else:
        new_analysis = RiskAnalysis(
            symbol=symbol,
            risk_score=risk_data["risk_score"],
            risk_level=risk_data["risk_level"],
            reasons=json.dumps(risk_data["reasons"]),
            alternatives=json.dumps(risk_data["alternatives"])
        )
        db.session.add(new_analysis)
    
    db.session.commit()
    
    return jsonify({
        "symbol": symbol,
        "risk_score": risk_data["risk_score"],
        "risk_level": risk_data["risk_level"],
        "reasons": risk_data["reasons"],
        "alternatives": risk_data["alternatives"],
        "analysis_date": datetime.utcnow().isoformat()
    })

@risk_bp.route('/risk/history/<symbol>', methods=['GET'])
def get_risk_history(symbol):
    """Get historical risk analysis for a symbol"""
    analysis = RiskAnalysis.query.filter_by(symbol=symbol.upper()).first()
    
    if not analysis:
        return jsonify({"error": "No analysis found for this symbol"}), 404
    
    return jsonify(analysis.to_dict())

@risk_bp.route('/risk/market-sentiment', methods=['GET'])
def get_market_sentiment():
    """Get overall market sentiment grid"""
    # Generate a 3x6 sentiment grid
    sentiments = ['pos', 'neg', 'neu']
    sentiment_grid = []
    
    for i in range(3):
        row = []
        for j in range(6):
            # Bias towards positive sentiment (60% pos, 25% neu, 15% neg)
            rand = random.random()
            if rand < 0.6:
                sentiment = 'pos'
            elif rand < 0.85:
                sentiment = 'neu'
            else:
                sentiment = 'neg'
            row.append(sentiment)
        sentiment_grid.append(row)
    
    # Calculate overall sentiment score
    total_cells = 18
    pos_count = sum(row.count('pos') for row in sentiment_grid)
    sentiment_score = (pos_count / total_cells) * 100
    
    return jsonify({
        "sentiment_grid": sentiment_grid,
        "sentiment_score": round(sentiment_score, 1),
        "last_updated": datetime.utcnow().isoformat()
    })

