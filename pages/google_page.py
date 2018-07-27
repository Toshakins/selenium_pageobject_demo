from webbrowser import Chrome

from pages.abstract_page import AbstractPage


class GooglePage(AbstractPage):
    def __init__(self, driver: Chrome, query) -> None:
        super().__init__(driver)
        self.query = query

    def enter_query(self):
        self.driver.get('https://google.com')
        search_element = self.driver.find_element_by_name('q')
        search_element.send_keys(self.query)
        search_element.submit()