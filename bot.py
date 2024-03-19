import requests
import tweepy
import json
import os
import schedule
import time
from selenium import webdriver
from scrape import scrape_sam_page

# twitter api credentials
from config import consumer_key, consumer_secret, access_token, access_token_secret

# authenticate twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# write proposals to the JSON file
def update_doc(file, proposals):
	with open(file, "w") as f:
		json.dump(proposals, f, indent=2)


# TODO: schedule job to run every three hours
# TODO: run the scheduled job independently 

if __name__ == "__main__":
	# json file path
	file_path = "proposals.json"

	# Set up the Selenium WebDriver (e.g., Chrome)
	driver = webdriver.Chrome()

	base_url = f"https://sam.gov/search/?index=_all&sort=-modifiedDate&page=1&pageSize=100&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5Bstatus%5D%5Bis_inactive%5D=true&sfm%5BagencyPicker%5D%5B0%5D%5BorgKey%5D=300000412&sfm%5BagencyPicker%5D%5B0%5D%5BorgText%5D=97AE%20-%20DEFENSE%20ADVANCED%20RESEARCH%20PROJECTS%20AGENCY%20%20(DARPA)&sfm%5BagencyPicker%5D%5B0%5D%5BlevelText%5D=Subtier&sfm%5BagencyPicker%5D%5B0%5D%5Bhighlighted%5D=true" 

	proposals = scrape_sam_page(base_url, driver, 2)
	update_doc(file_path, proposals)
	print(f"updated json doc with proposals from page {page}")

	print("DONE")
	# close the browser
	driver.quit()
