from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    """Переходим на главную страницу сайта, для подтверждения того, что мы попали на нужную страницу
        сравнивая элемент с нужной страницы и на той, куда переходим"""

    url = 'https://www.labirint.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_word = '[class="autodiscounts-content"] h2 a'

    # Getters

    def get_main_word(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_word)))

    # Actions

    # Methods

    def open_website(self):

        Logger.add_start_step(method="open_website")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_words(self.get_main_word(), 'Лучшая покупка дня')
        Logger.add_end_step(url=self.driver.current_url, method="open_website")
