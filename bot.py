import tweepy
import json
from selenium import webdriver
from scraper import scrape

# twitter api credentials
from config import consumer_key, consumer_secret, access_token, access_token_secret

# authenticate twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# write proposals to the JSON file
def save_json(file, proposals):
	with open(file, "w") as f:
		json.dump(proposals, f, indent=2)


# TODO: schedule job to run every three hours
# TODO: run the scheduled job independently 

if __name__ == "__main__":
	# json file path
	file_path = "proposals.json"

	# Set up the Selenium WebDriver (e.g., Chrome)
	driver = webdriver.Chrome()

    # sam.gov search page filtering for DARPA proposals, including both active and inactive status
	base_url = "https://sam.gov/search/?index=_all&sort=-modifiedDate&page=1&pageSize=1000&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5Bstatus%5D%5Bis_inactive%5D=true&sfm%5BagencyPicker%5D%5B0%5D%5BorgKey%5D=300000412&sfm%5BagencyPicker%5D%5B0%5D%5BorgText%5D=97AE%20-%20DEFENSE%20ADVANCED%20RESEARCH%20PROJECTS%20AGENCY%20%20(DARPA)&sfm%5BagencyPicker%5D%5B0%5D%5BlevelText%5D=Subtier&sfm%5BagencyPicker%5D%5B0%5D%5Bhighlighted%5D=true"

	proposals = scrape(base_url, driver)
	save_json(file_path, proposals)

	print("DONE")
	# close the browser
	driver.quit()
