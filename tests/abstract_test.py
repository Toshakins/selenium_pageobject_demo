import unittest

from selenium.webdriver import Chrome


class AbstractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
