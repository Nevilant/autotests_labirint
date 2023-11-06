import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.main_page import MainPage


def test_with_auth():
    service = ChromeService(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)

    print('Start test')


time.sleep(5)
