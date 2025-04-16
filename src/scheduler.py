import schedule
import time
from main import run_report

def start_scheduler():
    schedule.every().day.at("08:00").do(run_report)

    while True:
        schedule.run_pending()
        time.sleep(60)
