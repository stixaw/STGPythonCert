import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import helperMethods


 # why not build a map of all the links on a certain section.
 # X For this challenge, take a look at https://www.copart.com main page.
 # X Go to the Makes/Models section of the page.
 # X Create a 2 dimensional array that stores all the values displayed on the page along w/ the URL for that link.
 # X Once you have this array, you can verify all the elements in the array navigates to the correct page.
 # X Don’t forget to verify some piece of data on the page.
 # To get started, inspect the code and notice the section of the page is built using angular.
 # There is no static id or element class that identifies each element in this section.
 # Everything is generic.
 # The only way to build a function/object for this section is to loop through each element.
 # Hint: xpath is easiest.  ***Note, you did part of this in challenge 3.

class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')

    def test_walk_the_urls(self):
        car_url_dict = []
        wait = WebDriverWait(self.driver, 20)

        self.driver.get('https://www.copart.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[@ng-if='popularSearches']")))
        popular_array = self.driver.find_elements_by_xpath("//div[@ng-if='popularSearches']//ul/li/a")
        count = 0

        while count < len(popular_array):
            pair_list = []
            car_model = popular_array[count].text
            pair_list.append(car_model)

            href = popular_array[count].get_attribute("href")
            pair_list.append(href)

            # add pair_array to array of arrays
            car_url_dict.append(pair_list)
            count += 1
        print(car_url_dict)

        count = 0
        while count < len(car_url_dict):
            pair = car_url_dict[count]
            # print(pair)
            car_model = pair[0]
            car_url = pair[1]

            try:
                # print('Url {0} - {1}'.format(count, car_url))
                self.driver.get(car_url)
                self.driver.implicitly_wait(10)

                WebDriverWait(self.driver, 15).until(
                    ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
                body = self.driver.find_element_by_css_selector("table#serverSideDataTable tbody").text
                self.assertIn(car_model, body)

            except:
                screen_name = "{0}-{1}Error".format(car_model, car_url)
                self.driver.save_screenshot("{0}.png".format(screen_name))
                err = car_model + 'NotFound!'
                print('Error Thrown: ', err)
            count += 1

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
