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
        submit_button = self.driver.find_element_by_css_selector('[data-uname="homepageHeadersearchsubmit"]')
        submit_button.click()
        WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
        body = self.driver.find_element_by_css_selector("#serverSideDataTable tbody").get_property('text')
        self.assertIn("PORSCHE", body)


if __name__ == '__main__':
    unittest.main()
