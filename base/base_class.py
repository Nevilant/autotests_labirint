import datetime


class Base:

    path_for_screens = "./screens/"

    def __init__(self, driver):
        self.driver = driver

    """Получаем текущий URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Проверка по тексту"""

    def assert_words(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    """Делаем скриншот"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = '_Screenshot' + now_date + '.png'

        self.driver.save_screenshot(self.path_for_screens + name_screenshot)
