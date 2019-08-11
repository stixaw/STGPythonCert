import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')

    def tearDown(self):
        driver = self.driver
        driver.close()

    def test_challenge2(self):
        self.assertIn("Copart USA", self.driver.title)

    def test_search_for_exotic(self):
        search_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "input-search")))
        search_input.click()
        search_input.send_keys('exotic')
        search_input.send_keys(Keys.ENTER)
        body = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, "serverSideDataTable")))
        body_text = body.get_attribute("innerHTML")
        self.assertIn("PORSCHE", body_text)


if __name__ == '__main__':
    unittest.main()
