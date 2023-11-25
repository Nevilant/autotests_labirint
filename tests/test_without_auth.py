import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from base.base_class import Base

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.filters_page import FiltersPage
from pages.cart_page import CartPage


@allure.description("Test without authorization 1")
@pytest.mark.run(order=1)
def test_without_auth_1(set_up, set_group):

    """Тестируем путь покупки товара с переходмо в корзину через значок корзины в хедере"""

    service = ChromeService(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)

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

    driver.quit()


@allure.description("Test without authorization 2")
@pytest.mark.run(order=2)
def test_without_auth_2(set_up):

    """Тестируем путь покупки товара с переходмо в корзину через значок корзины в карточке товара"""

    service = ChromeService(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)

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

    driver.quit()


@allure.description("Test without authorization 3")
@pytest.mark.run(order=3)
def test_without_auth_3(set_up):

    """Тестируем путь покупки товара с переходмо в корзину через значок корзины в всплывающем окне"""

    service = ChromeService(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)

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

    driver.quit()
