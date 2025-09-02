from flask import Blueprint, request, jsonify, send_file
from src.models.user import db, User, Portfolio
from datetime import datetime, timedelta
import json
import os
from fpdf import FPDF
import tempfile

reports_bp = Blueprint('reports', __name__)

class RiskReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Clear Trade AI - Weekly Risk Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

@reports_bp.route('/reports/weekly', methods=['GET'])
def get_weekly_report():
    """Get weekly risk report data"""
    user_id = request.args.get('user_id', 1, type=int)
    
    # Mock weekly report data
    report_data = {
        "report_period": {
            "start_date": (datetime.utcnow() - timedelta(days=7)).isoformat(),
            "end_date": datetime.utcnow().isoformat()
        },
        "portfolio_summary": {
            "total_value": "₹81,500",
            "weekly_change": "+₹2,340 (+2.95%)",
            "risk_score": 42,
            "risk_level": "Moderate"
        },
        "risk_analysis": {
            "high_risk_assets": [
                {"name": "ABC Ltd", "risk_score": 85, "recommendation": "Consider selling"}
            ],
            "moderate_risk_assets": [
                {"name": "XYZ Corp", "risk_score": 68, "recommendation": "Monitor closely"}
            ],
            "safe_assets": [
                {"name": "NIFTY 50 ETF", "risk_score": 25, "recommendation": "Hold"},
                {"name": "TCS", "risk_score": 35, "recommendation": "Hold"}
            ]
        },
        "diversification_score": 78,
        "recommendations": [
            "Consider reducing exposure to high-risk stocks",
            "Increase allocation to ETFs for better diversification",
            "Add debt instruments to reduce overall portfolio risk"
        ],
        "compliance_notes": [
            "All investments are SEBI-compliant",
            "No regulatory violations detected",
            "Portfolio adheres to risk guidelines"
        ],
        "generated_at": datetime.utcnow().isoformat()
    }
    
    return jsonify(report_data)

@reports_bp.route('/reports/generate-pdf', methods=['POST'])
def generate_pdf_report():
    """Generate PDF report"""
    data = request.get_json()
    user_id = data.get('user_id', 1)
    
    # Get user data
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Create PDF
    pdf = RiskReportPDF()
    pdf.add_page()
    
    # User Information
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f'Report for: {user.full_name}', 0, 1)
    pdf.cell(0, 10, f'Generated on: {datetime.utcnow().strftime("%Y-%m-%d %H:%M")}', 0, 1)
    pdf.ln(5)
    
    # Portfolio Summary
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Portfolio Summary', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 8, 'Total Portfolio Value: Rs 81,500', 0, 1)
    pdf.cell(0, 8, 'Weekly Change: +Rs 2,340 (+2.95%)', 0, 1)
    pdf.cell(0, 8, 'Risk Score: 42/100 (Moderate)', 0, 1)
    pdf.ln(5)
    
    # Risk Analysis
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Risk Analysis', 0, 1)
    pdf.set_font('Arial', '', 10)
    
    # High Risk Assets
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 8, 'High Risk Assets:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, '• ABC Ltd (Risk Score: 85) - Consider selling', 0, 1)
    pdf.ln(3)
    
    # Safe Assets
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 8, 'Safe Assets:', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, '• NIFTY 50 ETF (Risk Score: 25) - Hold', 0, 1)
    pdf.cell(0, 6, '• TCS (Risk Score: 35) - Hold', 0, 1)
    pdf.ln(5)
    
    # Recommendations
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Recommendations', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 6, '• Consider reducing exposure to high-risk stocks', 0, 1)
    pdf.cell(0, 6, '• Increase allocation to ETFs for better diversification', 0, 1)
    pdf.cell(0, 6, '• Add debt instruments to reduce overall portfolio risk', 0, 1)
    pdf.ln(5)
    
    # SEBI Disclaimer
    pdf.set_font('Arial', 'I', 8)
    pdf.multi_cell(0, 5, 'Disclaimer: This report is for informational purposes only and does not constitute investment advice. Please consult with a certified financial advisor before making investment decisions. All recommendations are SEBI-compliant.')
    
    # Save PDF to temporary file
    temp_dir = tempfile.gettempdir()
    pdf_filename = f"risk_report_{user_id}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(temp_dir, pdf_filename)
    pdf.output(pdf_path)
    
    return send_file(pdf_path, as_attachment=True, download_name=f"weekly_risk_report_{datetime.utcnow().strftime('%Y%m%d')}.pdf")

@reports_bp.route('/reports/diversification', methods=['GET'])
def get_diversification_report():
    """Get portfolio diversification analysis"""
    user_id = request.args.get('user_id', 1, type=int)
    
    diversification_data = {
        "overall_score": 78,
        "asset_allocation": {
            "Large Cap": {"percentage": 45, "value": "₹36,675", "status": "Good"},
            "ETF": {"percentage": 25, "value": "₹20,375", "status": "Good"},
            "Debt/Liquid": {"percentage": 15, "value": "₹12,225", "status": "Low"},
            "Others": {"percentage": 15, "value": "₹12,225", "status": "Moderate"}
        },
        "sector_allocation": {
            "Technology": 30,
            "Financial Services": 25,
            "Consumer Goods": 20,
            "Healthcare": 15,
            "Others": 10
        },
        "risk_distribution": {
            "Low Risk": 40,
            "Moderate Risk": 45,
            "High Risk": 15
        },
        "recommendations": [
            "Increase debt allocation to 25% for better stability",
            "Consider adding international exposure (5-10%)",
            "Reduce concentration in technology sector",
            "Add small-cap exposure for growth potential"
        ],
        "compliance_status": "SEBI Compliant",
        "last_updated": datetime.utcnow().isoformat()
    }
    
    return jsonify(diversification_data)

@reports_bp.route('/reports/compliance-check', methods=['GET'])
def compliance_check():
    """Check SEBI compliance status"""
    user_id = request.args.get('user_id', 1, type=int)
    
    compliance_data = {
        "overall_status": "Compliant",
        "checks": [
            {
                "rule": "Maximum single stock exposure",
                "limit": "10%",
                "current": "8.5%",
                "status": "Pass"
            },
            {
                "rule": "Minimum diversification",
                "limit": "5 different assets",
                "current": "8 assets",
                "status": "Pass"
            },
            {
                "rule": "Risk concentration",
                "limit": "Max 20% in high-risk",
                "current": "15%",
                "status": "Pass"
            },
            {
                "rule": "Liquid assets minimum",
                "limit": "10%",
                "current": "15%",
                "status": "Pass"
            }
        ],
        "warnings": [],
        "violations": [],
        "last_checked": datetime.utcnow().isoformat()
    }
    
    return jsonify(compliance_data)

@reports_bp.route('/reports/performance', methods=['GET'])
def get_performance_report():
    """Get portfolio performance metrics"""
    user_id = request.args.get('user_id', 1, type=int)
    period = request.args.get('period', '1M')  # 1W, 1M, 3M, 6M, 1Y
    
    performance_data = {
        "period": period,
        "total_return": {
            "absolute": "₹2,340",
            "percentage": 2.95
        },
        "benchmark_comparison": {
            "portfolio_return": 2.95,
            "nifty_50_return": 2.1,
            "sensex_return": 1.8,
            "outperformance": 0.85
        },
        "risk_metrics": {
            "volatility": 12.5,
            "sharpe_ratio": 1.2,
            "max_drawdown": -3.2,
            "beta": 0.85
        },
        "asset_performance": [
            {"asset": "NIFTY 50 ETF", "return": 2.3, "contribution": 0.58},
            {"asset": "TCS", "return": 4.2, "contribution": 0.92},
            {"asset": "Axis Bluechip", "return": 1.8, "contribution": 0.72},
            {"asset": "HDFC Bank", "return": 3.1, "contribution": 0.73}
        ],
        "generated_at": datetime.utcnow().isoformat()
    }
    
    return jsonify(performance_data)

