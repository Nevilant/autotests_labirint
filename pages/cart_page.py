from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    """Попадаем в корзину и переходим на страницу с оформлением товара"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_cart = " ul > li.b-header-b-personal-e-list-item.have-dropdown.last-child.have-dropdown-notouch > a"
    button_checkout = "#buy961816"
    bubble_checkout_button = "div.b-basket-popinfo-e-block.js-good-added > div > a"
    main_word = "span.product-title"
    button_go_to_checkout = "button.btn.btn-primary.btn-large.fright.start-checkout-js"
    checkout_word = "#app > div.checkout.set-width > div.checkout__header > h1"

    # Getters

    def get_button_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_cart)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_checkout)))

    def get_bubble_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.bubble_checkout_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_word)))

    def get_button_go_to_checkout(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_go_to_checkout)))

    def get_checkout_word(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkout_word)))

    # Actions

    def click_button_cart(self):
        ActionChains(self.driver).move_to_element(self.get_button_cart()).click().perform()
        print("Click button cart")

    def click_button_checkout(self):
        ActionChains(self.driver).move_to_element(self.get_button_checkout()).click().perform()

    def click_bubble_checkout_button(self):
        ActionChains(self.driver).move_to_element(self.get_bubble_checkout_button()).click().perform()

    def click_button_go_to_checkout(self):
        ActionChains(self.driver).move_to_element(self.get_button_go_to_checkout()).click().perform()

    # Methods

    def use_cart(self):
        self.click_button_cart()
        self.assert_words(self.get_main_word(), "Токийские мстители. Том 11")
        self.click_button_go_to_checkout()
        self.assert_words(self.get_checkout_word(), "Оформление заказа")

    def use_checkout(self):
        self.click_button_checkout()
        self.assert_words(self.get_main_word(), "Токийские мстители. Том 11")
        self.click_button_go_to_checkout()
        self.assert_words(self.get_checkout_word(), "Оформление заказа")

    def use_bubble_checkout(self):
        self.click_bubble_checkout_button()
        self.assert_words(self.get_main_word(), "Токийские мстители. Том 11")
        self.click_button_go_to_checkout()
        self.assert_words(self.get_checkout_word(), "Оформление заказа")
