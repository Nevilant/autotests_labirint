import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from config.links import Links


class MainPage(Base):
    """
    Переходим на главную страницу сайта, для подтверждения того, что мы попали на нужную страницу
        сравнивая элемент с нужной страницы и на той, куда переходим
    """
    PAGE_URL = Links.HOST
    # Locators

    MAIN_WORD = (By.CSS_SELECTOR, "[class='b-header-b-logo-e-logo']")
    SIGN_IN = (By.CSS_SELECTOR, "[data-sendto='authorize']")
    FIELD_CODE = (By.CSS_SELECTOR, "[value='+7']")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[value='Войти']")
    BOOKS_MENU = (By.CSS_SELECTOR, "[data-toggle='header-genres']")
    COMICS_MANGA_ART_BOOKS = (By.CSS_SELECTOR, "span[class*='b-menu-list-title-first']")
    MANGA = (By.CSS_SELECTOR, "[href='/genres/2684']")

    # Getters

    def get_main_word(self):
        return Wait(self.driver, 10).until(EC.visibility_of_element_located(self.MAIN_WORD))

    def get_sign_in(self):
        return Wait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.SIGN_IN))

    def get_code_field(self):
        return Wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIELD_CODE))

    def get_button_login(self):
        return Wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_LOGIN))

    def get_books_menu(self):
        return Wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOOKS_MENU))

    def get_comics_manga_art_books(self):
        return Wait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.COMICS_MANGA_ART_BOOKS))

    def get_manga(self):
        return Wait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MANGA))

    # Actions

    def click_sign_in(self):
        self.get_sign_in()[1].click()

    def click_code_field(self, code):
        self.get_code_field().click()
        self.get_code_field().send_keys(Keys.CONTROL + 'a')
        self.get_code_field().send_keys(Keys.BACKSPACE)
        self.get_code_field().send_keys(code)

    def click_button_login(self):
        self.get_button_login().click()

    def hover_books_menu(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_books_menu()).perform()

    def hover_comics_manga_art_books(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_comics_manga_art_books()[2]).perform()

    def click_manga(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_manga()).click().perform()
