# Clear Trade AI - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently, the API doesn't require authentication for demo purposes. In production, implement JWT tokens.

## API Endpoints

### 1. User Management

#### POST /user/onboarding
Register a new user or update existing user profile.

**Request Body:**
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "age": 30,
  "income_range": "10to25",
  "investment_experience": "intermediate",
  "risk_appetite": "moderate"
}
```

**Response:**
```json
{
  "message": "User profile saved successfully",
  "user": {
    "id": 1,
    "full_name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "income_range": "10to25",
    "investment_experience": "intermediate",
    "risk_appetite": "moderate"
  },
  "risk_profile": {
    "score": 65,
    "recommendations": [
      "Balanced portfolio with 70% equity, 30% debt",
      "Mix of large-cap and mid-cap funds"
    ]
  }
}
```

#### GET /user/profile/{user_id}
Get user profile and risk assessment.

**Response:**
```json
{
  "user": {
    "id": 1,
    "full_name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "risk_appetite": "moderate"
  },
  "risk_profile": {
    "score": 65,
    "recommendations": ["..."]
  }
}
```

### 2. Portfolio Management

#### GET /portfolio/snapshot
Get complete portfolio overview.

**Response:**
```json
{
  "holdings": [
    {
      "asset": "NIFTY 50 ETF",
      "type": "ETF",
      "qty": 10,
      "value": "₹18,500",
      "current_price": 1850.0,
      "change_percent": 2.3
    },
    {
      "asset": "TCS",
      "type": "Stock",
      "qty": 5,
      "value": "₹18,200",
      "current_price": 3640.0,
      "change_percent": 0.8
    }
  ],
  "total_value": "₹81,500",
  "total_gain_loss": "₹2,340",
  "gain_loss_percent": 3.2
}
```

#### GET /portfolio/risk-meter
Get portfolio risk assessment.

**Response:**
```json
{
  "risk_score": 42,
  "risk_level": "Moderate",
  "factors": [
    "Portfolio diversification: Good",
    "Asset allocation: Balanced",
    "Volatility exposure: Moderate"
  ]
}
```

#### GET /portfolio/alerts
Get AI-generated portfolio alerts.

**Response:**
```json
{
  "alerts": [
    {
      "title": "Pump & Dump Warning - ABC Ltd",
      "description": "Unusual volume spike and coordinated mentions detected.",
      "severity": "High",
      "type": "pump_dump",
      "timestamp": "2025-09-02T10:30:00Z"
    }
  ]
}
```

### 3. Risk Analysis

#### POST /risk/analyze
Analyze risk for a specific stock or fund.

**Request Body:**
```json
{
  "symbol": "TCS"
}
```

**Response:**
```json
{
  "symbol": "TCS",
  "risk_score": 35,
  "risk_level": "Safe",
  "reasons": [
    "Strong fundamentals and consistent performance",
    "Low volatility compared to sector average",
    "Stable dividend history"
  ],
  "alternatives": ["NIFTY 50 ETF", "SENSEX ETF", "Large Cap Mutual Fund"],
  "analysis_date": "2025-09-02T12:00:00Z"
}
```

#### GET /risk/market-sentiment
Get market sentiment overview grid.

**Response:**
```json
{
  "sentiment_grid": [
    ["pos", "pos", "neu", "neg", "pos", "neu"],
    ["neg", "neu", "pos", "pos", "neu", "neg"],
    ["pos", "pos", "pos", "neu", "neg", "pos"]
  ],
  "sentiment_score": 61.1,
  "last_updated": "2025-09-02T12:00:00Z"
}
```

### 4. News & Social Media

#### GET /news/sentiment
Get latest news with sentiment analysis.

**Response:**
```json
{
  "news": [
    {
      "title": "Bluechip earnings beat expectations",
      "source": "Business Daily",
      "sentiment": "Positive",
      "timestamp": "2025-09-02T09:30:00Z",
      "summary": "Major bluechip companies reported strong quarterly results..."
    }
  ],
  "overall_sentiment": "Mixed",
  "sentiment_distribution": {
    "positive": 40,
    "neutral": 35,
    "negative": 25
  }
}
```

#### GET /social/buzz
Get social media buzz tracking.

**Response:**
```json
{
  "buzz_tracker": [
    {
      "symbol": "XYZ Corp",
      "mentions": 1240,
      "change_percent": 240,
      "sentiment": "Mixed",
      "trending_keywords": ["earnings", "growth", "acquisition"]
    }
  ]
}
```

#### GET /alerts/pump-dump
Get pump and dump alerts.

**Response:**
```json
{
  "pump_dump_alerts": [
    {
      "symbol": "ABC Ltd",
      "alert_type": "High Risk",
      "description": "High-risk pattern detected: price-volume anomaly and coordinated posts.",
      "risk_factors": [
        "Unusual volume spike (300% above average)",
        "Coordinated social media mentions"
      ],
      "severity": "High"
    }
  ]
}
```

### 5. AI Advisory Bot

#### POST /advisor/chat
Chat with the AI investment advisor.

**Request Body:**
```json
{
  "question": "Is XYZ stock safe for long-term investment?",
  "user_id": 1
}
```

**Response:**
```json
{
  "question": "Is XYZ stock safe for long-term investment?",
  "answer": "Based on risk signals and news, XYZ shows moderate risk. Consider diversified ETFs for long-term stability.\n\nDisclaimer: This is not investment advice. Please do your own research. SEBI-compliant guidance applies.",
  "timestamp": "2025-09-02T12:00:00Z"
}
```

#### GET /advisor/history?user_id=1
Get chat history for a user.

**Response:**
```json
{
  "chat_history": [
    {
      "id": 1,
      "question": "Is XYZ stock safe?",
      "answer": "Based on analysis...",
      "timestamp": "2025-09-02T12:00:00Z"
    }
  ],
  "total_chats": 1
}
```

#### GET /advisor/suggestions?user_id=1
Get personalized investment suggestions.

**Response:**
```json
{
  "suggestions": [
    "Balanced portfolio with 70% equity, 30% debt",
    "Mix of large-cap and mid-cap mutual funds",
    "Consider sector-specific ETFs"
  ],
  "user_risk_profile": "moderate",
  "disclaimer": "This is not investment advice..."
}
```

### 6. Reports & Compliance

#### GET /reports/weekly?user_id=1
Get weekly risk report data.

**Response:**
```json
{
  "report_period": {
    "start_date": "2025-08-26T00:00:00Z",
    "end_date": "2025-09-02T00:00:00Z"
  },
  "portfolio_summary": {
    "total_value": "₹81,500",
    "weekly_change": "+₹2,340 (+2.95%)",
    "risk_score": 42,
    "risk_level": "Moderate"
  },
  "risk_analysis": {
    "high_risk_assets": [
      {
        "name": "ABC Ltd",
        "risk_score": 85,
        "recommendation": "Consider selling"
      }
    ],
    "safe_assets": [
      {
        "name": "NIFTY 50 ETF",
        "risk_score": 25,
        "recommendation": "Hold"
      }
    ]
  },
  "recommendations": [
    "Consider reducing exposure to high-risk stocks",
    "Increase allocation to ETFs for better diversification"
  ]
}
```

#### POST /reports/generate-pdf
Generate and download PDF report.

**Request Body:**
```json
{
  "user_id": 1
}
```

**Response:** PDF file download

#### GET /reports/diversification?user_id=1
Get portfolio diversification analysis.

**Response:**
```json
{
  "overall_score": 78,
  "asset_allocation": {
    "Large Cap": {"percentage": 45, "value": "₹36,675", "status": "Good"},
    "ETF": {"percentage": 25, "value": "₹20,375", "status": "Good"},
    "Debt/Liquid": {"percentage": 15, "value": "₹12,225", "status": "Low"}
  },
  "recommendations": [
    "Increase debt allocation to 25% for better stability",
    "Consider adding international exposure (5-10%)"
  ]
}
```

## Error Responses

All endpoints return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (validation errors)
- `404` - Not Found
- `500` - Internal Server Error

**Error Response Format:**
```json
{
  "error": "Error message description"
}
```

## Rate Limiting

Currently no rate limiting is implemented. In production, implement rate limiting to prevent abuse.

## Data Validation

All endpoints validate input data and return appropriate error messages for invalid inputs.

## SEBI Compliance

All investment advice includes appropriate SEBI disclaimers and compliance notes.

