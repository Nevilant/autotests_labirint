import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from base.base_class import Base

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.filters_page import FiltersPage


def test_with_auth():
    service = ChromeService(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)

    print('Start test')

    mp = MainPage(driver)
    mp.open_website()

    pp = ProductPage(driver)
    pp.select_category()

    fp = FiltersPage(driver)
    fp.filters_fields()

    pp.select_product()

    screen = Base(driver)
    screen.get_screenshot()


time.sleep(5)
