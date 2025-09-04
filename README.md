📌 Clear Trade AI
🛡️ Empowering Indian Retail Investors with Safe & Transparent Investment Decisions
🌍 Problem Statement

Indian retail investors often:

Follow social media hype and unverified tips → fall into pump & dump scams.

Lack proper understanding of risk, diversification, and compliance.

Have limited access to transparent tools that flag risky assets or scams in real time.

This leads to financial losses, erosion of trust, and reduced participation in capital markets.

💡 Solution: Clear Trade AI

Clear Trade AI is an AI-powered investment advisory platform designed to:

Analyze investor risk appetite & profile.

Provide AI-driven risk scoring of stocks, funds, and portfolios.

Use NLP & sentiment analysis to detect misinformation, pump & dump activity, and scam signals.

Offer safe, SEBI-compliant alternatives like ETFs, mutual funds, and diversified index options.

Generate easy-to-read reports to guide investors with transparency.

👉 In short: Your AI guardian against risky investments.

🚀 Key Features

Investor Onboarding & Risk Profiling → Builds personalized investor profiles.

Portfolio Management → Tracks holdings, overall portfolio health, and diversification.

AI Risk Analysis → Assigns risk scores with reasons + safer alternatives.

News & Social Media Monitoring → Real-time detection of hype & pump/dump schemes.

AI Advisory Bot → SEBI-compliant investment suggestions in plain language.

Reports & Compliance → Weekly portfolio/risk reports with SEBI disclaimers.

🛠️ Technology Stack

Backend: Python (Flask)

Frontend: React (dashboard + chatbot interface)

Database: SQLite (development) / PostgreSQL (production-ready)

AI/ML: OpenAI LLMs, Sentiment Analysis models, Risk Scoring models

Data Sources: Alpha Vantage / Polygon.io (market), NewsAPI (news sentiment)

Security: CORS, encryption, SEBI-compliant disclaimers

📊 Impact & Alignment with SEBI’s Mandate

Investor Protection → Prevents losses from scams & misinformation.

Market Development → Builds trust, encourages more retail participation.

Supervision & Transparency → AI-powered fraud/risk detection aligns with SEBI’s regulatory goals.

Scalability → Can handle thousands of users, portfolios, and transactions.

Feasibility → Built on existing APIs + secure AI integration → ready for real-world deployment.

⚙️ Setup (for Developers)

Clone the repo & install dependencies

git clone https://github.com/your-repo/clear-trade-ai.git
cd clear-trade-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Configure API Keys
Add your keys in src/config.py:

OPENAI_API_KEY → for AI chatbot

NEWS_API_KEY → for news sentiment

ALPHA_VANTAGE_API_KEY → for stock data

Run the server

python src/main.py


Server starts at → http://localhost:5000

🔒 Security & Compliance

All advice includes SEBI disclaimers.

Strong data privacy & encryption for user data.

APIs secured via keys and CORS configuration.

📅 Roadmap

Multi-language support (Hindi + regional).

Deeper fraud detection via graph-based ML models.

DigiLocker + UPI integration for seamless investor access.

Mobile app version for wider retail adoption.

🤝 Support

For issues, refer to logs or documentation in the docs/ folder.
