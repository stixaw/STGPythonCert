import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')

    def tearDown(self):
        driver = self.driver
        driver.close()

    def test_challenge3(self):
        self.assertIn("Copart USA", self.driver.title)

