import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from base.base_class import Base
from config.links import Links
from utilities.logger import Logger


class MangaPage(Base):
    """
    Находимся на странице с мангой и выбираем товары
    """

    PAGE_URL = Links.MANGA_PAGE

    # Locators for Categories

    MAIN_TEXT = (By.CSS_SELECTOR, "[class='genre-name']")
    BUTTON_ALL_FILTERS = (By.CSS_SELECTOR, "[class='navisort-item__content']")
    ALL_FILTERS_TEXT = (By.CSS_SELECTOR, "[class='bl-name']")

    # Getters

    def get_main_word(self):
        return Wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MAIN_TEXT))

    def get_button_all_filters(self):
        return Wait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.BUTTON_ALL_FILTERS))

    def get_text_all_filters(self):
        return Wait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.ALL_FILTERS_TEXT))[0]

    # Actions

    def click_button_all_filters(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_button_all_filters()[2]).click().perform()

    def click_button_add_in_cart_product_1(self):
        ActionChains(self.driver).move_to_element(self.get_button_add_in_cart_product_1()).click().perform()
        print('Product added in cart')

    # Methods

    def select_category(self):
        with allure.step("Select category"):
            self.hover_books_menu()
            self.hover_comics_manga_artbooks()
            self.click_manga()
            self.assert_words(self.get_main_word(), 'Манга')

    def select_product(self):
        with allure.step("Select product"):
            self.click_button_add_in_cart_product_1()
