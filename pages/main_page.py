import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    """Переходим на главную страницу сайта, для подтверждения того, что мы попали на нужную страницу
        сравнивая элемент с нужной страницы и на той, куда переходим"""

    url = 'https://www.labirint.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_word = '[class="autodiscounts-content"] h2 a'
    sign_in = ".b-header-b-personal-wrapper > ul > li:nth-child(4) > a"
    code_field = "input[value='+7']"
    button_login = "#g-recap-0-btn"

    # Getters

    def get_main_word(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_word)))

    def get_sign_in(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in)))

    def get_code_field(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.code_field)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_login)))

    # Actions

    def click_sign_in(self):
        ActionChains(self.driver).move_to_element(self.get_sign_in()).click().perform()

    def click_code_field(self):
        ActionChains(self.driver).move_to_element(self.get_code_field()).click().perform()
        self.get_code_field().send_keys(Keys.CONTROL + 'a')
        self.get_code_field().send_keys(Keys.BACKSPACE)
        self.get_code_field().send_keys("6E3C-4307-B5DC")

    def click_button_login(self):
        ActionChains(self.driver).move_to_element(self.get_button_login()).click().perform()

    # Methods

    def open_website(self):
        with allure.step("Open website"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.assert_words(self.get_main_word(), 'Лучшая покупка дня')

    def authorization(self):
        with allure.step("Autorization"):
            self.click_sign_in()
            self.click_code_field()
            self.click_button_login()
