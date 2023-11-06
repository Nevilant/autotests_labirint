import time

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
    comics_manga_artbooks = "#header-genres > div > ul > li:nth-child(6) > span"
    manga = "#header-genres > div > ul > li:nth-child(6) > ul > li:nth-child(7) > a"
    main_word = "h1[class='genre-name']"
    all_filters = "div.navisort-line-one.swiper-slide.swiper-slide-active span:nth-child(3) .navisort-item__content"
    list_publ_house = "#section-search-form > div:nth-child(4) > div.bl-name.block-pubhouse-bl-name"
    publ_house = "#section-search-form > div:nth-child(4) .b-search-e-list-item:nth-child(2) label"
    list_cover = "#section-search-form > div:nth-child(6) .bl-name"
    cover = "#section-search-form > div:nth-child(6) .inputs div:first-child"
    button_show = ".show-goods > input.show-goods__button"

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

    def get_all_filters(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.all_filters)))

    def get_list_publ_house(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.list_publ_house)))

    def get_publ_house(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.publ_house)))

    def get_list_cover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.list_cover)))

    def get_cover(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cover)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.button_show)))

    # Actions

    def hover_books_menu(self):
        ActionChains(self.driver).move_to_element(self.get_books_menu()).perform()
        print('Dropdown menu is open')

    def hover_comics_manga_artbooks(self):
        ActionChains(self.driver).move_to_element(self.get_comics_manga_artbooks()).perform()
        print('Dropdown menu is open')

    def click_manga(self):
        ActionChains(self.driver).move_to_element(self.get_manga()).click().perform()
        print('Page is open')

    def click_all_filters(self):
        ActionChains(self.driver).move_to_element(self.get_all_filters()).click().perform()
        print('Filters is open')

    def click_list_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_list_publ_house()).click().perform()

    def click_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_publ_house()).click().perform()
        print('Select publishing house')

    def close_list_publ_house(self):
        ActionChains(self.driver).move_to_element(self.get_list_publ_house()).click().perform()

    def click_list_cover(self):
        ActionChains(self.driver).move_to_element(self.get_list_cover()).click().perform()
        print('Open filter of cover')

    def click_cover(self):
        ActionChains(self.driver).move_to_element(self.get_cover()).click().perform()
        print('Select type cover')

    def close_list_cover(self):
        ActionChains(self.driver).move_to_element(self.get_list_cover()).click().perform()

    def click_button_show(self):
        ActionChains(self.driver).move_to_element(self.get_button_show()).click().perform()
        print('Click button')
        time.sleep(10)
    # Methods

    def select_products(self):
        self.hover_books_menu()
        self.hover_comics_manga_artbooks()
        self.click_manga()
        self.assert_words(self.get_main_word(), 'Манга')
        self.click_all_filters()
        self.click_list_publ_house()
        self.click_publ_house()
        self.close_list_publ_house()
        self.click_list_cover()
        self.click_cover()
        self.close_list_cover()
        self.click_button_show()
