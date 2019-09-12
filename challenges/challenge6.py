import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import helperMethods

class Challenge6(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_error_handling(self):
        wait = WebDriverWait(self.driver, 10)

        # search for Nissan
        search_input = wait.until(
            ec.presence_of_element_located((By.ID, "input-search")))
        search_input.click()
        search_input.send_keys('Nissan')
        submit_button = self.driver.find_element_by_css_selector('[data-uname="homepageHeadersearchsubmit"]')
        submit_button.click()
        wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
        self.assertIn("Nissan", self.driver.title)

        # get Model filter
        model_filter = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@data-uname="ModelFilter"]')))
        model_filter.click()

        # try catch for skyline
        try:
            model_search = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#collapseinside4 [placeholder="Search"]')))
            model_search.send_keys('skyline')

            self.driver.find_element_by_css_selector("input#lot_model_descSKYLINE").click()
            wait.until(
               ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
            body = self.driver.find_element_by_css_selector("table#serverSideDataTable tbody").text
            self.assertIn("SKYLINE", body)

        except:
            print('ERROR skyline not found')
            self.driver.save_screenshot("screenshot.png")




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
