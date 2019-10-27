from setup import WebDriver
import unittest
from helper.page_objects import Guest



class MainTest(unittest.TestCase):



    def setUp(self):
        self.browser = WebDriver()
        self.browser.fetchUrl()

    def tearDown(self):
        self.browser.shutdown()

    def test_buy_item(self):

        buyItem = Guest(self.browser)
        buyItem.guest_journey()