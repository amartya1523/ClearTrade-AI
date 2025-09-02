from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
import random

news_bp = Blueprint('news', __name__)

# Mock news data
MOCK_NEWS = [
    {
        "title": "Bluechip earnings beat expectations",
        "source": "Business Daily",
        "sentiment": "Positive",
        "timestamp": "2025-09-02T09:30:00Z",
        "summary": "Major bluechip companies reported strong quarterly results, beating analyst expectations."
    },
    {
        "title": "Sector rotation dampens mid-cap outlook",
        "source": "MarketWatch",
        "sentiment": "Neutral",
        "timestamp": "2025-09-02T08:15:00Z",
        "summary": "Institutional investors are rotating from mid-cap to large-cap stocks amid market uncertainty."
    },
    {
        "title": "Regulatory query sent to ABC Finserv",
        "source": "Exchange Filing",
        "sentiment": "Negative",
        "timestamp": "2025-09-02T07:45:00Z",
        "summary": "SEBI has sent a regulatory query to ABC Finserv regarding recent trading activities."
    },
    {
        "title": "Technology sector shows resilience",
        "source": "Tech Tribune",
        "sentiment": "Positive",
        "timestamp": "2025-09-02T06:30:00Z",
        "summary": "IT companies continue to show strong performance despite global headwinds."
    },
    {
        "title": "Banking stocks under pressure",
        "source": "Financial Express",
        "sentiment": "Negative",
        "timestamp": "2025-09-02T05:20:00Z",
        "summary": "Banking sector faces headwinds from rising NPAs and regulatory changes."
    }
]

@news_bp.route('/news/sentiment', methods=['GET'])
def get_news_sentiment():
    """Get latest news with sentiment analysis"""
    # Return recent news with sentiment
    return jsonify({
        "news": MOCK_NEWS[:3],  # Return top 3 news items
        "overall_sentiment": "Mixed",
        "sentiment_distribution": {
            "positive": 40,
            "neutral": 35,
            "negative": 25
        },
        "last_updated": datetime.utcnow().isoformat()
    })

@news_bp.route('/social/buzz', methods=['GET'])
def get_social_buzz():
    """Get social media buzz tracking"""
    buzz_data = [
        {
            "symbol": "XYZ Corp",
            "mentions": 1240,
            "change_percent": 240,
            "sentiment": "Mixed",
            "trending_keywords": ["earnings", "growth", "acquisition"]
        },
        {
            "symbol": "ABC Ltd",
            "mentions": 890,
            "change_percent": 180,
            "sentiment": "Negative",
            "trending_keywords": ["investigation", "regulatory", "concerns"]
        },
        {
            "symbol": "TCS",
            "mentions": 650,
            "change_percent": 45,
            "sentiment": "Positive",
            "trending_keywords": ["results", "dividend", "stable"]
        }
    ]
    
    return jsonify({
        "buzz_tracker": buzz_data,
        "last_updated": datetime.utcnow().isoformat()
    })

@news_bp.route('/alerts/pump-dump', methods=['GET'])
def get_pump_dump_alerts():
    """Get pump and dump alerts"""
    alerts = [
        {
            "symbol": "ABC Ltd",
            "alert_type": "High Risk",
            "description": "High-risk pattern detected: price-volume anomaly and coordinated posts.",
            "risk_factors": [
                "Unusual volume spike (300% above average)",
                "Coordinated social media mentions",
                "Price manipulation patterns detected"
            ],
            "timestamp": "2025-09-02T10:15:00Z",
            "severity": "High"
        },
        {
            "symbol": "DEF Corp",
            "alert_type": "Medium Risk",
            "description": "Suspicious trading patterns detected in recent sessions.",
            "risk_factors": [
                "Abnormal price movements",
                "Increased retail participation",
                "Limited fundamental justification"
            ],
            "timestamp": "2025-09-02T09:30:00Z",
            "severity": "Medium"
        }
    ]
    
    return jsonify({
        "pump_dump_alerts": alerts,
        "total_alerts": len(alerts),
        "last_scan": datetime.utcnow().isoformat()
    })

@news_bp.route('/market/sentiment-analysis', methods=['GET'])
def get_detailed_sentiment():
    """Get detailed market sentiment analysis"""
    sentiment_data = {
        "overall_score": random.randint(45, 75),
        "sectors": {
            "Technology": {"score": 72, "trend": "up"},
            "Banking": {"score": 45, "trend": "down"},
            "Healthcare": {"score": 68, "trend": "stable"},
            "Energy": {"score": 55, "trend": "up"},
            "FMCG": {"score": 62, "trend": "stable"}
        },
        "news_impact": {
            "positive_news": 12,
            "negative_news": 8,
            "neutral_news": 15
        },
        "social_sentiment": {
            "bullish_posts": 65,
            "bearish_posts": 35
        },
        "last_updated": datetime.utcnow().isoformat()
    }
    
    return jsonify(sentiment_data)

@news_bp.route('/news/search', methods=['POST'])
def search_news():
    """Search news by keyword or symbol"""
    data = request.get_json()
    query = data.get('query', '').lower()
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    # Filter news based on query
    filtered_news = []
    for news in MOCK_NEWS:
        if query in news['title'].lower() or query in news['summary'].lower():
            filtered_news.append(news)
    
    return jsonify({
        "query": query,
        "results": filtered_news,
        "total_results": len(filtered_news),
        "search_timestamp": datetime.utcnow().isoformat()
    })

