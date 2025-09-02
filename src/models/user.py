from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    income_range = db.Column(db.String(20), nullable=False)  # lt5, 5to10, 10to25, gt25
    investment_experience = db.Column(db.String(20), nullable=False)  # none, basic, intermediate, advanced
    risk_appetite = db.Column(db.String(20), nullable=False)  # low, moderate, high
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.full_name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'age': self.age,
            'income_range': self.income_range,
            'investment_experience': self.investment_experience,
            'risk_appetite': self.risk_appetite,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    asset_name = db.Column(db.String(100), nullable=False)
    asset_type = db.Column(db.String(50), nullable=False)  # ETF, Stock, Mutual Fund
    quantity = db.Column(db.Float, nullable=False)
    current_value = db.Column(db.Float, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('portfolio', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'asset_name': self.asset_name,
            'asset_type': self.asset_type,
            'quantity': self.quantity,
            'current_value': self.current_value,
            'purchase_price': self.purchase_price,
            'purchase_date': self.purchase_date.isoformat() if self.purchase_date else None
        }

class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('chat_history', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class RiskAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), nullable=False)
    risk_score = db.Column(db.Integer, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)  # Safe, Moderate, Risky
    reasons = db.Column(db.Text, nullable=False)  # JSON string
    alternatives = db.Column(db.Text, nullable=False)  # JSON string
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'risk_score': self.risk_score,
            'risk_level': self.risk_level,
            'reasons': json.loads(self.reasons) if self.reasons else [],
            'alternatives': json.loads(self.alternatives) if self.alternatives else [],
            'last_updated': self.last_updated.isoformat() if self.last_updated else None
        }

