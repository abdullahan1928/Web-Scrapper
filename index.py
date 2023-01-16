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

    #targeting username and password fields
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    #clearing the fields and filling them with the data from the inquirer
    username.clear()
    username.send_keys(inq.answers['username'])

    password.clear()
    password.send_keys(inq.answers['password'])


    #targeting the login button and clicking it
    Login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #targeting the not now button on the save login info popup and clicking it
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    
    ex.wb.save("sample.xlsx")
    ct.calc_total_time()

    while (True):
        pass


launchBrowser()