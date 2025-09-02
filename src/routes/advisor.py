from flask import Blueprint, request, jsonify, current_app
from src.models.user import db, ChatHistory, User
from datetime import datetime
import openai
import os

advisor_bp = Blueprint('advisor', __name__)

# SEBI compliance disclaimer
SEBI_DISCLAIMER = "Disclaimer: This is not investment advice. Please do your own research. SEBI-compliant guidance applies."

# Mock responses for common queries
MOCK_RESPONSES = {
    "xyz stock safe": "Based on risk signals and news, XYZ shows moderate risk. Consider diversified ETFs for long-term stability.",
    "abc stock": "ABC Ltd shows high risk patterns including unusual volume spikes and coordinated mentions. We recommend avoiding this stock and considering safer alternatives like NIFTY 50 ETF.",
    "tcs investment": "TCS appears to be a relatively safe investment with strong fundamentals. However, consider portfolio diversification with ETFs and mutual funds.",
    "mutual fund": "Mutual funds offer good diversification. Consider large-cap funds for stability or balanced funds for moderate growth with lower risk.",
    "etf investment": "ETFs like NIFTY 50 ETF and SENSEX ETF provide excellent diversification and are generally safer than individual stocks.",
    "portfolio diversification": "A well-diversified portfolio should include 60% large-cap stocks/ETFs, 20% debt instruments, 15% mid-cap, and 5% international exposure.",
    "risk management": "Key risk management strategies include diversification, regular portfolio review, stop-loss orders, and avoiding concentration in single stocks."
}

def get_ai_response(question):
    """Get AI response using OpenAI API or mock responses"""
    question_lower = question.lower()
    
    # Check for mock responses first
    for key, response in MOCK_RESPONSES.items():
        if key in question_lower:
            return response
    
    try:
        # Use OpenAI API for more complex queries
        openai.api_key = current_app.config['OPENAI_API_KEY']
        client = openai.OpenAI(api_key=current_app.config['OPENAI_API_KEY'])
        
        system_prompt = """You are a SEBI-compliant investment advisor for Indian retail investors. 
        Provide safe, conservative investment advice. Always recommend diversification and warn against risky investments.
        Keep responses concise and practical. Focus on ETFs, mutual funds, and established large-cap stocks.
        Never provide specific buy/sell recommendations. Always emphasize the importance of personal research."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        # Fallback to generic response
        return "I understand your question about investments. For personalized advice, please consult with a certified financial advisor. Generally, diversified ETFs and mutual funds are safer options for retail investors."

@advisor_bp.route('/advisor/chat', methods=['POST'])
def chat_with_advisor():
    """Chat with the AI advisor bot"""
    data = request.get_json()
    question = data.get('question', '').strip()
    user_id = data.get('user_id', 1)  # Default user for demo
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    # Get AI response
    answer = get_ai_response(question)
    
    # Add SEBI disclaimer
    full_answer = f"{answer}\n\n{SEBI_DISCLAIMER}"
    
    # Save to chat history
    try:
        chat_entry = ChatHistory(
            user_id=user_id,
            question=question,
            answer=full_answer
        )
        db.session.add(chat_entry)
        db.session.commit()
    except Exception as e:
        print(f"Error saving chat history: {e}")
    
    return jsonify({
        "question": question,
        "answer": full_answer,
        "timestamp": datetime.utcnow().isoformat()
    })

@advisor_bp.route('/advisor/history', methods=['GET'])
def get_chat_history():
    """Get chat history for a user"""
    user_id = request.args.get('user_id', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    chat_history = ChatHistory.query.filter_by(user_id=user_id)\
                                  .order_by(ChatHistory.timestamp.desc())\
                                  .limit(limit)\
                                  .all()
    
    return jsonify({
        "chat_history": [chat.to_dict() for chat in chat_history],
        "total_chats": len(chat_history)
    })

@advisor_bp.route('/advisor/clear-history', methods=['POST'])
def clear_chat_history():
    """Clear chat history for a user"""
    data = request.get_json()
    user_id = data.get('user_id', 1)
    
    try:
        ChatHistory.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        
        return jsonify({
            "message": "Chat history cleared successfully",
            "timestamp": datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({"error": "Failed to clear chat history"}), 500

@advisor_bp.route('/advisor/suggestions', methods=['GET'])
def get_investment_suggestions():
    """Get general investment suggestions based on user profile"""
    user_id = request.args.get('user_id', 1, type=int)
    
    # Get user profile for personalized suggestions
    user = User.query.get(user_id)
    
    suggestions = []
    
    if user:
        if user.risk_appetite == 'low':
            suggestions = [
                "Consider NIFTY 50 ETF for stable large-cap exposure",
                "Liquid funds for emergency corpus",
                "Government bonds for guaranteed returns",
                "Large-cap mutual funds for steady growth"
            ]
        elif user.risk_appetite == 'moderate':
            suggestions = [
                "Balanced portfolio with 70% equity, 30% debt",
                "Mix of large-cap and mid-cap mutual funds",
                "NIFTY 50 ETF and NIFTY Next 50 ETF",
                "SIP in diversified equity funds"
            ]
        else:  # high risk appetite
            suggestions = [
                "Diversified equity portfolio with small-cap exposure",
                "Sector-specific ETFs for targeted growth",
                "International funds for global diversification",
                "Remember to maintain 20% in safe assets"
            ]
    else:
        suggestions = [
            "Start with NIFTY 50 ETF for broad market exposure",
            "Consider SIP in large-cap mutual funds",
            "Maintain emergency fund in liquid funds",
            "Gradually increase equity exposure based on comfort"
        ]
    
    return jsonify({
        "suggestions": suggestions,
        "user_risk_profile": user.risk_appetite if user else "unknown",
        "disclaimer": SEBI_DISCLAIMER
    })

