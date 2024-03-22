import time
from bot import post
from scraper import scrape

SCRAPING_INTERVAL = 12 * 60 * 60 # 12 hours in seconds
POSTING_INTERVAL = 6 * 60 * 60 # 6 hours in seconds

# run program indefinitely as a daemon 
while True:
	scrape()
	time.sleep(SCRAPING_INTERVAL)

	post()
	time.sleep(POSTING_INTERVAL)
