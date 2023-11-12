import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ProductPage(Base):
    """Выбираем нужную категорию товаров и сами товары"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for Categories

    books_menu = "span.b-header-b-menu-e-link.top-link-menu.first-child"
    comics_manga_artbooks = "#header-genres > div > ul > li:nth-child(6) > span"
    manga = "#header-genres > div > ul > li:nth-child(6) > ul > li:nth-child(7) > a"
    main_word = "h1[class='genre-name']"

    # Locators for Products

    button_add_in_cart_product_1 = "[id='buy961816']"

    # Getters

    def get_books_menu(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.books_menu)))

    def get_comics_manga_artbooks(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.comics_manga_artbooks)))

    def get_manga(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.manga)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_word)))

    def get_button_add_in_cart_product_1(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_add_in_cart_product_1)))

    # Actions

    def hover_books_menu(self):
        ActionChains(self.driver).move_to_element(self.get_books_menu()).perform()

    def hover_comics_manga_artbooks(self):
        ActionChains(self.driver).move_to_element(self.get_comics_manga_artbooks()).perform()

    def click_manga(self):
        ActionChains(self.driver).move_to_element(self.get_manga()).click().perform()

    def click_button_add_in_cart_product_1(self):
        ActionChains(self.driver).move_to_element(self.get_button_add_in_cart_product_1()).click().perform()
        print('Product added in cart')

    # Methods

    def select_category(self):
        self.hover_books_menu()
        self.hover_comics_manga_artbooks()
        self.click_manga()
        self.assert_words(self.get_main_word(), 'Манга')

    def select_product(self):
        self.click_button_add_in_cart_product_1()
