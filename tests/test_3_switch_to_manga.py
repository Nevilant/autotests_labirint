import allure

from pages.main_page import MainPage
from pages.manga_page import MangaPage


@allure.title("Переход в раздел 'Манга'")
def test_open_market(driver):
    main_page = MainPage(driver)
    manga_page = MangaPage(driver)
    main_page.open_the_website()
    with allure.step("Навестись на кнопку 'Книги'"):
        main_page.hover_books_menu()
    with allure.step("Навестись на кнопку 'Комиксы, манга, артбуки'"):
        main_page.hover_comics_manga_art_books()
    with allure.step("Нажать на кнопку 'Манга'"):
        main_page.click_manga()
    assert manga_page.get_main_word().text == 'Манга'