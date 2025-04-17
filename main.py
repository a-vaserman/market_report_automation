from src.fetch_data import fetch_market_data
from src.generate_report import generate_report
from src.email_utils import send_email_report
from datetime import datetime
import os

def run_report():
    tickers = ["^GSPC", "^IXIC", "AAPL", "TSLA"]
    market_data = fetch_market_data(tickers)
    report = generate_report(market_data)

    # Save to local .txt file
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(f"data/market_summary_{date_str}.txt", "w") as f:
        f.write(report)

    # Email report
    recipient = os.getenv("EMAIL_ADDRESS")  # Or set a specific address
    send_email_report("Daily Market Summary", report, recipient)

if __name__ == "__main__":
    run_report()