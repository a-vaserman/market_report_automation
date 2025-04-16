from datetime import datetime

def generate_report(market_data):
    date_str = datetime.now().strftime("%A, %B, %d, %Y")
    report = f"📈 Daily Market Summary - {date_str}\n\n"

    for ticker, stats in market_data.items():
        report += (
            f"{ticker} - ${stats['price']}"
            f"({stats['change']} / {stats['percent_change']}%)\n"
        )
    return report
