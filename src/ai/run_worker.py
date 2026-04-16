import time
import schedule
from src.ai.sentiment_worker import analyze_messages

def job():
    print("Running sentiment analysis...")
    analyze_messages()

# run every 10 minutes/change it to 1 min for faster testing
schedule.every(10).minutes.do(job)

print("Scheduler started...")

# run once immediately (optional but useful)
job()

while True:
    schedule.run_pending()
    time.sleep(1)