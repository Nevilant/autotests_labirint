from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base


class ProductPage(Base):

    """Прописываем локаторы нужнных нам элементов чтобы перейти в выбранный раздел
        и добавляем выбранный товар в корзину """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    books_menu = "span.b-header-b-menu-e-link.top-link-menu.first-child"

    # Getters

    def get_books_menu(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.books_menu)))

    # Actions

    def hover_books_menu(self):
        ActionChains(self.driver).move_to_element(self.get_books_menu()).perform()
        print('Dropdown menu is open')

    # Methods

    def select_products(self):
        self.hover_books_menu()
