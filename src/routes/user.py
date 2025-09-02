from flask import Blueprint, request, jsonify
from src.models.user import db, User
from datetime import datetime

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/user/onboarding', methods=['POST'])
def user_onboarding():
    """Handle user onboarding with KYC and risk profiling"""
    data = request.get_json()
    
    required_fields = ['full_name', 'email', 'age', 'income_range', 'investment_experience', 'risk_appetite']
    
    # Validate required fields
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'{field} is required'}), 400
    
    # Validate age
    try:
        age = int(data['age'])
        if age < 18 or age > 100:
            return jsonify({'error': 'Age must be between 18 and 100'}), 400
    except ValueError:
        return jsonify({'error': 'Age must be a valid number'}), 400
    
    # Validate income range
    valid_income_ranges = ['lt5', '5to10', '10to25', 'gt25']
    if data['income_range'] not in valid_income_ranges:
        return jsonify({'error': 'Invalid income range'}), 400
    
    # Validate investment experience
    valid_experiences = ['none', 'basic', 'intermediate', 'advanced']
    if data['investment_experience'] not in valid_experiences:
        return jsonify({'error': 'Invalid investment experience'}), 400
    
    # Validate risk appetite
    valid_risk_appetites = ['low', 'moderate', 'high']
    if data['risk_appetite'] not in valid_risk_appetites:
        return jsonify({'error': 'Invalid risk appetite'}), 400
    
    # Check if user already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        # Update existing user
        existing_user.full_name = data['full_name']
        existing_user.age = age
        existing_user.income_range = data['income_range']
        existing_user.investment_experience = data['investment_experience']
        existing_user.risk_appetite = data['risk_appetite']
        existing_user.updated_at = datetime.utcnow()
        
        db.session.commit()
        user = existing_user
    else:
        # Create new user
        user = User(
            full_name=data['full_name'],
            email=data['email'],
            age=age,
            income_range=data['income_range'],
            investment_experience=data['investment_experience'],
            risk_appetite=data['risk_appetite']
        )
        db.session.add(user)
        db.session.commit()
    
    return jsonify({
        'message': 'User profile saved successfully',
        'user': user.to_dict(),
        'risk_profile': {
            'score': calculate_risk_score(user),
            'recommendations': get_risk_recommendations(user)
        }
    }), 201

@user_bp.route('/user/profile/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    """Get user profile"""
    user = User.query.get_or_404(user_id)
    return jsonify({
        'user': user.to_dict(),
        'risk_profile': {
            'score': calculate_risk_score(user),
            'recommendations': get_risk_recommendations(user)
        }
    })

@user_bp.route('/user/profile/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    """Update user profile"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    # Update fields if provided
    if 'full_name' in data:
        user.full_name = data['full_name']
    if 'age' in data:
        user.age = int(data['age'])
    if 'income_range' in data:
        user.income_range = data['income_range']
    if 'investment_experience' in data:
        user.investment_experience = data['investment_experience']
    if 'risk_appetite' in data:
        user.risk_appetite = data['risk_appetite']
    
    user.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'message': 'Profile updated successfully',
        'user': user.to_dict()
    })

def calculate_risk_score(user):
    """Calculate risk score based on user profile"""
    score = 0
    
    # Age factor (younger = higher risk tolerance)
    if user.age < 30:
        score += 30
    elif user.age < 45:
        score += 20
    else:
        score += 10
    
    # Income factor
    income_scores = {'lt5': 10, '5to10': 20, '10to25': 30, 'gt25': 40}
    score += income_scores.get(user.income_range, 10)
    
    # Experience factor
    exp_scores = {'none': 5, 'basic': 15, 'intermediate': 25, 'advanced': 35}
    score += exp_scores.get(user.investment_experience, 5)
    
    # Risk appetite factor
    risk_scores = {'low': 5, 'moderate': 15, 'high': 25}
    score += risk_scores.get(user.risk_appetite, 5)
    
    return min(score, 100)

def get_risk_recommendations(user):
    """Get investment recommendations based on user profile"""
    recommendations = []
    
    if user.risk_appetite == 'low':
        recommendations = [
            "Focus on large-cap mutual funds and ETFs",
            "Consider debt funds for stable returns",
            "Maintain 60% equity, 40% debt allocation",
            "Start with SIP in NIFTY 50 ETF"
        ]
    elif user.risk_appetite == 'moderate':
        recommendations = [
            "Balanced portfolio with 70% equity, 30% debt",
            "Mix of large-cap and mid-cap funds",
            "Consider sector-specific ETFs",
            "Regular portfolio review and rebalancing"
        ]
    else:  # high risk appetite
        recommendations = [
            "Diversified equity portfolio with small-cap exposure",
            "International funds for global diversification",
            "Sector rotation strategies",
            "Maintain 20% in safe assets for stability"
        ]
    
    # Add experience-based recommendations
    if user.investment_experience == 'none':
        recommendations.insert(0, "Start with basic investment education")
        recommendations.insert(1, "Begin with simple ETFs and mutual funds")
    
    return recommendations

