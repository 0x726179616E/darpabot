from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import copy


# /html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[1]/div/app-opportunity-result/div/div[2]/div[3]/div/div[4]/div/div[2]

# /html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[2]/div/app-opportunity-result/div/div[2]/div[3]/div/div[4]/div/div[2]

# scrape search page 
def scrape_sam_page(url, driver, pages):
    driver.get(url)

    next_button = driver.find_element(By.XPATH, "/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/sds-pagination/div[1]/div[1]/button[2]")

    # list of proposals
    final_proposals = []

    # outer loop: interate through pages
    for j in range(1, pages+1):
        page_proposals = []

        timeout = 3

        # inner loop: iterate through proposals on each page
        for i in range(1, 101):
            try:
                header_element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[1]/div[1]/div/h3/a'))
                )

                # header_copy = copy.copy(header_element)

                title = header_element.text.strip()
                # link = header_copy.get_attribute("href")
                link = header_element.get_attribute("href")

                notice_id = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[1]/div/app-opportunity-result/div/div[1]/div[2]/h3'))
                ).text.strip()

                date = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[2]/div[3]/div/div[4]/div/div[2]'))
                ).text.strip()

                description = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/app-frontend-search-root/section/app-frontend-search-home/div/div/div/div[2]/search-list-layout/div[2]/div/div/sds-search-result-list/div[{i}]/div/app-opportunity-result/div/div[1]/div[3]/div/p'))
                ).text.strip()

                print(f"{title.upper()}")
                print(f"{notice_id}")
                print(f"Date Originally Published: {date}")
                print(f"Description: {description}")
                print(f"Link: {link}")
                print()

                proposal = { 
                    "title": title.upper(),
                    "notice_id": notice_id,
                    "date": date,
                    "description": description,
                    "link": link
                }

                # append indiviudal proposal to page's list of proposals
                page_proposals.append(proposal)

            except TimeoutException:
                print("Element not found within the specified timeout")
        # append page's proposals to final list
        final_proposals.append({f"Page {i}": page_proposals})
        try: 
            next_button.click()
        except NoSuchElementException:
            break;

    return final_proposals


        
