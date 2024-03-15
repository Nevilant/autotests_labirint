import allure

from pages.main_page import MainPage


@allure.title("Открытие магазина")
def test_open_market(driver):
    main_page = MainPage(driver)
    main_page.open_the_website()
    with allure.step("Логотип магазина отобразился"):
        main_page.get_main_word()
