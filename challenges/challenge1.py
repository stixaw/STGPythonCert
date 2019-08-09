import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome('../chromedriver')
        self.var = {}

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge1(self):
        self.driver.get('https://www.google.com')
        self.assertIn("Google", self.driver.title)

    def test_challenge2(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon", self.driver.title)

    def test_challenge3(self):
        self.driver.get("https://www.yahoo.com")
        self.assertIn("Yahoo", self.driver.title)

    def test_challenge4(self):
        self.driver.get("https://www.msn.com")
        self.assertIn("MSN", self.driver.title)


if __name__ == '__main__':
    unittest.main()


