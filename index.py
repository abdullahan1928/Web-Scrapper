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
    userName = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'session_key')))
    password = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'session_password')))
    # signInBtn = wait.until(EC.element_to_be_clickable(
    #     (By.CLASS_NAME, 'sign-in-form__submit-button')))

    userName.send_keys(inq.answers['username'])
    password.send_keys(inq.answers['password'])
    password.send_keys(Keys.ENTER)

    # Navigate to home page
    searchBox = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'search-global-typeahead__input')))
    searchBox.send_keys('jamshaid khalid')
    searchBox.send_keys(Keys.ENTER)
    idLink = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'entity-result__title-text')))
    idLink.click()

    # name = parser.findAll('h1', attrs={'class': 'text-heading-xlarge'})[0]
    # details = parser.findAll('div', attrs={'class': 'text-body-medium'})[0]

    # parser = BeautifulSoup(driver.page_source, 'html.parser')

    # app = parser.find('div', attrs={'class': 'application-outlet'})
    # app = app.find('main', attrs={'id': 'main'})
    # print(app)
    # name = app.findAll('h1', attrs={'class': 'text-heading-xlarge'})
    # details = app.findAll('div')

    # print('-----------------Name-----------------')
    # print(name)
    # print(details)

    # ex.ws.cell(row=2, column=1,
    #            value=str(name))
    # ex.ws.cell(row=2,
    #            column=2, value=str(details))

    ex.wb.save("sample.xlsx")
    ct.calc_total_time()

    while (True):
        pass


launchBrowser()