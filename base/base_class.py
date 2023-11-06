class Base:

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