from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import excel_logic as ex
import inquirer_logic as inq
import calc_time as ct

ct.start_time

if inq.answers['platform'] == 'Linkedin':
    url = 'https://www.linkedin.com/'
elif inq.answers['platform'] == 'Instagram':
    url = 'https://www.instagram.com/'
elif inq.answers['platform'] == 'Twitter':
    url = 'https://twitter.com/'

driver = webdriver.Chrome()
driver.get(url)


def navigateToHome():
    driver.get(url)


def launchBrowser():
    wait = WebDriverWait(driver, 10)

    # ex.wb.save("sample.xlsx")
    ct.calc_total_time()

    while (True):
        pass


launchBrowser()
