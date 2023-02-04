import variables
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from parsel import Selector
from webdriver_manager.chrome import ChromeDriverManager



# Chrome driver install
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com/')
sleep(3)
# getting the variables name and login
username = driver.find_element(By.CLASS_NAME, 'input__input')
username.send_keys(variables.my_username) # username field

password = driver.find_element(By.NAME, 'session_password')
password.send_keys(variables.my_password) # password field
sleep(1)
log_in_button = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button') # submit button
log_in_button.click() # click the submit button
sleep(2)


# Saving the linkedin users urls in an array to do the scraping

profile_urls = variables.contactList

# To check the list content we run the following command
# [profile_urls.append(users.get_attribute("href")) for users in linkedin_users_urls_list]

fields = ['Name','Job Title','Company','University','Location','name two','name three','URL']
sel = Selector(text=driver.page_source)
# What we need from the profile


with open(variables.file_name, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)
    for profiles in profile_urls:
        driver.get(profiles)
        sleep(6)
        sel = Selector(text=driver.page_source)
        sleep(6)
        name = sel.xpath('//*[starts-with(@class, "text-heading-xlarge")]/text()').extract_first()
        if name:
            name = name.strip()
        else:
            name = 'No Result'
        job_title = sel.xpath('//*[starts-with(@class, "text-body-medium")]/text()').extract_first()
        if job_title:
            job_title = job_title.strip()
        else:
            job_title = 'No Result'
        company = sel.xpath('//*[starts-with(@aria-label, "Current company")]/text()').extract_first()
        if company:
            company = company.strip()
        else:
            company = 'No Result'
        university = sel.xpath('//*[starts-with(@aria-label, "Education")]/text()').extract_first()
        if university:
            university = university.strip()
        else:
            university = 'No Result'
        location = sel.xpath('//*[starts-with(@class, "text-body-small")]/text()').extract_first()
        if location:
            location = location.strip()
        else:
            location = 'No Result'
        info = driver.find_element(By.ID, 'top-card-text-details-contact-info')
        info.click()
        sleep(8)
        name_two = sel.xpath('//*[starts-with(@id, "pv-contact-info")]/text()')
        if name_two:
            name_two = name_two.strip()
        else:
            name_two = 'found?'
        sleep(6)
        name_three = sel.xpath('//*[starts-with(@class, "text-body-large-open mb4")]/text()')
        sleep(6)
        if name_three:
            name_three = name_three.strip()
        else:
            name_three = 'again?'
        linkedin_url = driver.current_url
        writer.writerow([name, job_title, company, university, location, name_two, name_three, linkedin_url])

    