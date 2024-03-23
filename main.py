import time
from datetime import datetime
from bot import post
from scraper import scrape

TIME_INTERVAL = 24 * 60 * 60 # 24 hours in seconds

# run program indefinitely as a daemon 
while True:
	print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: SCRAPING NOW\n")
	scrape()

	print(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: POSTING NOW\n")
	post()

	time.sleep(TIME_INTERVAL)
