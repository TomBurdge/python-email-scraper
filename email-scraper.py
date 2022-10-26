import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import random as rd
from pyisemail import is_email

site_list = ["ENTER YOUR EMAILS HERE"]

class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()
    
    def get_source(self):
        return self.browser.page_source

browser = Browser(r'drivers\chromedriver.exe')

#Define regex through which will find emails
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

#Create a dataframe with company name and sites that will add emails to
df= pd.DataFrame(data={'Sites':site_list)

#Make an empty column that will add to the new dataframe
emails_column = []

for site in site_list:
    #Try to open the site. Keep a record to add to the dataframe if can't
    try:
        browser.open_page(site)
        time.sleep(rd.uniform(0.75,1.5))
    except:
        emails_column.append("Couldn't load site.")
        time.sleep(rd.uniform(0.75,1.5))
        continue

    #Try to obtain source code for site. Keep a record to add to the dataframe if can't
    try:
        page_source = browser.get_source()
        time.sleep(rd.uniform(0.75,1.5))
    except:
        emails_column.append("Couldn't find page source")
        time.sleep(rd.uniform(0.75,1.5))
        continue
    
    # Create a list and add all the emails
    list_of_emails = []

    # Finds all the emails
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        list_of_emails.append(re_match.group())

    # Removes all repeats in the list
    list_of_emails = list(dict.fromkeys(list_of_emails))

    #Check if emails that regex found are valid - additional code check
    valid_emails = []
    for email in list_of_emails:
        if is_email(email, check_dns=True) is True:
            valid_emails.append(email)
    
    #Make the list of emails into a string that can go in the output cell
    emails_str = ', '.join(valid_emails)

    #Add emails to the emails column that will add to the dataframe as a new column
    if len(emails_str)>0:
        emails_column.append(str(emails_str))
    else:
        emails_column.append("no emails found")
    time.sleep(rd.uniform(0.75,1.5))

#Add the emails list to the dataframe as a new column
df['emails'] = emails_column

df.to_csv("emails.csv", index = False)

browser.close_browser()
