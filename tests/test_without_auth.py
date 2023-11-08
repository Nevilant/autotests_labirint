import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from base.base_class import Base

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.filters_page import FiltersPage
from pages.cart_page import CartPage


def test_without_auth_1():
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

    cp = CartPage(driver)
    cp.use_cart()

    screen = Base(driver)
    screen.get_screenshot()


def test_without_auth_2():
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

    cp = CartPage(driver)
    cp.use_checkout()

    screen = Base(driver)
    screen.get_screenshot()


def test_without_auth_3():
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

    cp = CartPage(driver)
    cp.use_bubble_checkout()

    screen = Base(driver)
    screen.get_screenshot()
