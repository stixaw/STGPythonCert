import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')

    def tearDown(self):
        driver = self.driver
        driver.close()

    def test_challenge3(self):
        self.assertIn("Copart USA", self.driver.title)
        
    def test_get_popular_searches_name_and_html(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@ng-if='popularSearches']")))
        popular_array = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//ul/li/a")
        count = 0

        while count < len(popular_array):
            car_model = popular_array[count].get_property('text')
            car_url = popular_array[count].get_attribute('href')
            print(car_model + " - " + car_url)
            count += 1
        self.assertEqual(count, 20)

    def test_get_trending_searches_name_and_html(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@id='tabTrending']")))
        popular_array = self.driver.find_elements_by_xpath("//div[@id='tabTrending']//a")

        for c in popular_array:
            trend_item = c.get_property('text')
            item_url = c.get_attribute('href')
            print(trend_item + " - " + item_url)

        self.assertEqual(len(popular_array), 40)


if __name__ == '__main__':
    unittest.main()
