import allure

from pages.manga_page import MangaPage


def test_open_all_filters(driver):
    manga_page = MangaPage(driver)
    manga_page.open_the_website()
    with allure.step("Нажать на кнопку 'Все фильтры'"):
        manga_page.get_button_all_filters()
    assert manga_page.get_text_all_filters().text == "НАЛИЧИЕ"
