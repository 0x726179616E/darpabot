import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

# scraping job
def scrape():
    # set up the selenium webdriver (chrome)
    driver = webdriver.Chrome()

    # sam.gov search page filtering for DARPA proposals, including both active and inactive status
    url = "https://sam.gov/search/?index=_all&sort=-modifiedDate&page=1&pageSize=50&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5Bstatus%5D%5Bis_inactive%5D=true&sfm%5BagencyPicker%5D%5B0%5D%5BorgKey%5D=300000412&sfm%5BagencyPicker%5D%5B0%5D%5BorgText%5D=97AE%20-%20DEFENSE%20ADVANCED%20RESEARCH%20PROJECTS%20AGENCY%20%20(DARPA)&sfm%5BagencyPicker%5D%5B0%5D%5BlevelText%5D=Subtier&sfm%5BagencyPicker%5D%5B0%5D%5Bhighlighted%5D=true"

    driver.get(url) 

    timeout = 5
    proposals = []

    # loop through all 50 proposals on the search page
    for i in range(1, 50): 
        try:
            header_element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[1]/div[1]/div/h3/a'))
            )

            title = header_element.text.strip()
            link = header_element.get_attribute("href")

            notice_id = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[1]/div[2]/h3'))
            ).text.strip()

            date = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[2]/div[3]/div/div[4]/div/div[2]'))
            ).text.strip()

            description = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[1]/div[3]/div/p'))
            ).text.strip()

            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Completed scraping proposal {i}...")

            proposal = { 
                "title": title.upper(),
                "notice_id": notice_id,
                "date": date,
                "description": description,
                "link": link
            }

            # append proposal to list of proposals
            proposals.append(proposal)

        # handle timeout when scraping proposal
        except TimeoutException:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Element for proposal {i} not found within the specified timeout")

    # save list of scraped proposals to json file
    with open("proposals.json", "w") as f:
        json.dump(proposals, f, indent=2)

    # close the browser
    driver.quit()

    return
