# Clear Trade AI Backend

A comprehensive Flask backend for the Clear Trade AI investment advisory platform designed for Indian retail investors.

## Features

- **User Onboarding & KYC**: Complete user profile management with risk assessment
- **Portfolio Management**: Real-time portfolio tracking and risk analysis
- **AI-Powered Risk Analysis**: Stock/fund risk scoring with ML models
- **News & Social Media Analysis**: Real-time sentiment analysis and pump & dump detection
- **AI Advisory Bot**: SEBI-compliant investment recommendations using OpenAI
- **Reports & Compliance**: Weekly risk reports and portfolio diversification analysis

## API Endpoints

### User Management
- `POST /api/user/onboarding` - User registration and profile setup
- `GET /api/user/profile/<user_id>` - Get user profile
- `PUT /api/user/profile/<user_id>` - Update user profile

### Portfolio APIs
- `GET /api/portfolio/snapshot` - Portfolio overview with holdings
- `GET /api/portfolio/risk-meter` - Portfolio risk assessment
- `GET /api/portfolio/alerts` - AI-generated alerts
- `GET /api/portfolio/diversification` - Diversification analysis

### Risk Analysis
- `POST /api/risk/analyze` - Analyze risk for stocks/funds
- `GET /api/risk/history/<symbol>` - Historical risk data
- `GET /api/risk/market-sentiment` - Market sentiment grid

### News & Social Media
- `GET /api/news/sentiment` - Latest news with sentiment
- `GET /api/social/buzz` - Social media buzz tracking
- `GET /api/alerts/pump-dump` - Pump & dump alerts
- `POST /api/news/search` - Search news by keyword

### AI Advisory Bot
- `POST /api/advisor/chat` - Chat with AI advisor
- `GET /api/advisor/history` - Chat history
- `POST /api/advisor/clear-history` - Clear chat history
- `GET /api/advisor/suggestions` - Investment suggestions

### Reports & Compliance
- `GET /api/reports/weekly` - Weekly risk report data
- `POST /api/reports/generate-pdf` - Generate PDF report
- `GET /api/reports/diversification` - Diversification report
- `GET /api/reports/compliance-check` - SEBI compliance check

## Setup Instructions

### 1. Install Dependencies
```bash
cd clear-trade-backend
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Keys
Edit `src/config.py` and add your API keys:

```python
# Required API Keys
OPENAI_API_KEY = 'your-openai-api-key-here'
NEWS_API_KEY = 'your-news-api-key-here'  # Optional
ALPHA_VANTAGE_API_KEY = 'your-alpha-vantage-key-here'  # Optional
```

### 3. Run the Server
```bash
python src/main.py
```

The server will start on `http://localhost:5000`

### 4. Test the API
```bash
# Health check
curl http://localhost:5000/api/health

# Test portfolio snapshot
curl http://localhost:5000/api/portfolio/snapshot

# Test risk analysis
curl -X POST http://localhost:5000/api/risk/analyze \
  -H "Content-Type: application/json" \
  -d '{"symbol": "TCS"}'
```

## API Key Requirements

### Essential APIs:
1. **OpenAI API** (Required for AI Advisory Bot)
   - Get from: https://platform.openai.com/api-keys
   - Used for: Investment advice and chat responses

### Optional APIs (for enhanced features):
2. **News API** (For real-time news)
   - Get from: https://newsapi.org/
   - Used for: News sentiment analysis

3. **Alpha Vantage** (For stock data)
   - Get from: https://www.alphavantage.co/support/#api-key
   - Used for: Real-time stock prices

4. **Polygon.io** (For market data)
   - Get from: https://polygon.io/
   - Used for: Advanced market data

## Frontend Integration

To connect with your frontend, update the API base URL in your frontend code:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';

// Example API call
fetch(`${API_BASE_URL}/portfolio/snapshot`)
  .then(response => response.json())
  .then(data => console.log(data));
```

## Database

The backend uses SQLite by default. The database file is created automatically at `src/database/app.db`.

## CORS Configuration

CORS is enabled for all origins to allow frontend integration. In production, update the CORS configuration in `src/main.py`:

```python
CORS(app, origins=["https://your-frontend-domain.com"])
```

## Deployment

For production deployment:

1. Update `src/config.py` with production settings
2. Use environment variables for API keys
3. Consider using PostgreSQL instead of SQLite
4. Set up proper logging and monitoring

## Sample API Responses

### Portfolio Snapshot
```json
{
  "holdings": [
    {
      "asset": "NIFTY 50 ETF",
      "type": "ETF",
      "qty": 10,
      "value": "₹18,500",
      "change_percent": 2.3
    }
  ],
  "total_value": "₹81,500",
  "gain_loss_percent": 3.2
}
```

### Risk Analysis
```json
{
  "symbol": "TCS",
  "risk_score": 35,
  "risk_level": "Safe",
  "reasons": [
    "Strong fundamentals and consistent performance",
    "Low volatility compared to sector average"
  ],
  "alternatives": ["NIFTY 50 ETF", "SENSEX ETF"]
}
```

### AI Chat Response
```json
{
  "question": "Is TCS safe for investment?",
  "answer": "TCS appears to be a relatively safe investment with strong fundamentals...",
  "timestamp": "2025-09-02T12:00:00Z"
}
```

## Security & Compliance

- All investment advice includes SEBI disclaimers
- User data is stored securely in the database
- API keys are managed through configuration
- CORS is properly configured for security

## Support

For issues or questions, refer to the API documentation or check the logs in the console when running the server.

