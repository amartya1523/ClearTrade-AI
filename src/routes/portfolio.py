from flask import Blueprint, request, jsonify
from src.models.user import db, Portfolio, User
import random

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/portfolio/snapshot', methods=['GET'])
def get_portfolio_snapshot():
    """Get portfolio snapshot for dashboard"""
    # Mock data for demonstration
    holdings = [
        {
            "asset": "NIFTY 50 ETF",
            "type": "ETF",
            "qty": 10,
            "value": "₹18,500",
            "current_price": 1850.0,
            "change_percent": 2.3
        },
        {
            "asset": "Axis Bluechip",
            "type": "Mutual Fund",
            "qty": 120,
            "value": "₹32,000",
            "current_price": 266.67,
            "change_percent": -1.2
        },
        {
            "asset": "TCS",
            "type": "Stock",
            "qty": 5,
            "value": "₹18,200",
            "current_price": 3640.0,
            "change_percent": 0.8
        },
        {
            "asset": "HDFC Bank",
            "type": "Stock",
            "qty": 8,
            "value": "₹12,800",
            "current_price": 1600.0,
            "change_percent": 1.5
        }
    ]
    
    total_value = sum([float(h["value"].replace("₹", "").replace(",", "")) for h in holdings])
    
    return jsonify({
        "holdings": holdings,
        "total_value": f"₹{total_value:,.0f}",
        "total_gain_loss": "₹2,340",
        "gain_loss_percent": 3.2
    })

@portfolio_bp.route('/portfolio/risk-meter', methods=['GET'])
def get_risk_meter():
    """Get portfolio risk meter data"""
    # Calculate risk based on portfolio composition
    risk_score = random.randint(35, 75)  # Mock calculation
    
    risk_level = "Low"
    if risk_score >= 40:
        risk_level = "Moderate"
    if risk_score >= 70:
        risk_level = "High"
    
    return jsonify({
        "risk_score": risk_score,
        "risk_level": risk_level,
        "factors": [
            "Portfolio diversification: Good",
            "Asset allocation: Balanced",
            "Volatility exposure: Moderate",
            "Sector concentration: Low"
        ]
    })

@portfolio_bp.route('/portfolio/alerts', methods=['GET'])
def get_ai_alerts():
    """Get AI-generated alerts for the portfolio"""
    alerts = [
        {
            "title": "Pump & Dump Warning - ABC Ltd",
            "description": "Unusual volume spike and coordinated mentions detected.",
            "severity": "High",
            "type": "pump_dump",
            "timestamp": "2025-09-02T10:30:00Z"
        },
        {
            "title": "Misinformation Flag",
            "description": "Conflicting earnings rumors; official filing pending.",
            "severity": "Moderate",
            "type": "misinformation",
            "timestamp": "2025-09-02T09:15:00Z"
        },
        {
            "title": "Sector Rotation Alert",
            "description": "Technology sector showing weakness, consider rebalancing.",
            "severity": "Low",
            "type": "sector_rotation",
            "timestamp": "2025-09-02T08:45:00Z"
        }
    ]
    
    return jsonify({"alerts": alerts})

@portfolio_bp.route('/portfolio/diversification', methods=['GET'])
def get_diversification():
    """Get portfolio diversification analysis"""
    diversification_data = {
        "score": 78,
        "breakdown": {
            "Large Cap": 45,
            "ETF": 25,
            "Debt/Liquid": 15,
            "Others": 15
        },
        "recommendations": [
            "Consider adding international exposure",
            "Increase debt allocation for stability",
            "Add small-cap exposure for growth"
        ]
    }
    
    return jsonify(diversification_data)

