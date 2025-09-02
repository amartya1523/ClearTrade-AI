import os

class Config:
    """Configuration class for Clear Trade AI Backend"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdf#FGSgvasgf$5$WGT'
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Keys - Add your API secrets here
    # OpenAI API for AI Advisory Bot
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'YOUR_OPENAI_API_KEY_HERE'
    
    # News API for real-time news (optional)
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') or 'YOUR_NEWS_API_KEY_HERE'
    
    # Alpha Vantage API for stock data (optional)
    ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY') or 'YOUR_ALPHA_VANTAGE_API_KEY_HERE'
    
    # Polygon.io API for market data (optional)
    POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY') or 'YOUR_POLYGON_API_KEY_HERE'
    
    # Twitter API for social sentiment (optional)
    TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN') or 'YOUR_TWITTER_BEARER_TOKEN_HERE'
    
    # NSE/BSE API keys (if available)
    NSE_API_KEY = os.environ.get('NSE_API_KEY') or 'YOUR_NSE_API_KEY_HERE'
    BSE_API_KEY = os.environ.get('BSE_API_KEY') or 'YOUR_BSE_API_KEY_HERE'
    
    # Email configuration for reports
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOUR_EMAIL@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'YOUR_EMAIL_PASSWORD'

# API Endpoints for external services
API_ENDPOINTS = {
    'news_api': 'https://newsapi.org/v2/',
    'alpha_vantage': 'https://www.alphavantage.co/query',
    'polygon': 'https://api.polygon.io/v2/',
    'twitter': 'https://api.twitter.com/2/',
    'openai': 'https://api.openai.com/v1/'
}

# Market data configuration
MARKET_CONFIG = {
    'trading_hours': {
        'start': '09:15',
        'end': '15:30',
        'timezone': 'Asia/Kolkata'
    },
    'exchanges': ['NSE', 'BSE'],
    'indices': ['NIFTY', 'SENSEX', 'NIFTY_BANK', 'NIFTY_IT'],
    'update_frequency': 300  # seconds
}

