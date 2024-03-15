import allure
import pytest

from pages.main_page import MainPage


@allure.title("Авторизация")
@pytest.mark.parametrize("datas", ["6E3C-4307-B5DC"])
def test_open_market(driver, datas):
    main_page = MainPage(driver)
    main_page.open_the_website()
    with allure.step("Нажать кнопку 'Мой лабиринт'"):
        main_page.click_sign_in()
    with allure.step("Ввести код авторизации"):
        main_page.click_code_field(datas)
    with allure.step("Нажать кнопку 'Войти'"):
        main_page.click_button_login()
