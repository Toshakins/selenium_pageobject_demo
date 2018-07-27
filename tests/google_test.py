from pages.google_page import GooglePage
from tests.abstract_test import AbstractTest


class GoogleTest(AbstractTest):
    def test_a(self):
        query = 'cats'
        google_page = GooglePage(self.driver, query)
        google_page.enter_query()
        self.assertIn(query, self.driver.title)
