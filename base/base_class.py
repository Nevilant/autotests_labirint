from config.links import Links


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.PAGE_URL = Links.HOST

    def open_the_website(self):
        self.driver.get(self.PAGE_URL)
