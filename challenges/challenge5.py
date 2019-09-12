import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import helperMethods

class Challenge5(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_filter_for_porsche(self):
        wait = WebDriverWait(self.driver, 15)
        # search for exotics
        search_input = wait.until(
            ec.presence_of_element_located((By.ID, "input-search")))
        search_input.click()
        search_input.send_keys('Exotic')
        submit_button = self.driver.find_element_by_css_selector('[data-uname="homepageHeadersearchsubmit"]')
        submit_button.click()
        WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
        self.assertIn("Exotic", self.driver.title)

        # filter on porsche
        filter_input = self.driver.find_element_by_css_selector('#serverSideDataTable_filter input')
        filter_input.click()
        filter_input.send_keys('porsche')
        filter_input.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 15).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "table#serverSideDataTable tbody")))
        body = self.driver.find_element_by_css_selector("table#serverSideDataTable tbody").text
        self.assertIn("PORSCHE", body)

        # extend filter to 100 results
        WebDriverWait(self.driver, 15).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#serverSideDataTable_length select")))
        entries_control = self.driver.find_element_by_css_selector("#serverSideDataTable_length select")
        entries_control.click()
        Select(entries_control).select_by_value("100")
        WebDriverWait(self.driver, 15).until(ec.text_to_be_present_in_element((By.ID, "serverSideDataTable_info"), "1 to 100"))

        # Get Models
        models = WebDriverWait(self.driver, 15).until(
            ec.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotmodel"]')))
        model_list = []
        for item in models:
            model_name = item.text
            model_list.append(model_name)
        sorted_list = sorted(model_list)
        model_dict = {}

        for car_model in sorted_list:
            helperMethods.add_pair(car_model, model_dict)

        print('***** Model-Count *****')
        for model in model_dict:
            count = model_dict[model]
            print('{0}-{1}'.format(model, count))

        # Damages
        dings = WebDriverWait(self.driver, 15).until(
            ec.presence_of_all_elements_located((By.XPATH, '//*[@data-uname="lotsearchLotdamagedescription"]')))
        dmg_dict = {}
        for dmg in dings:
            dmg_name = dmg.text
            if dmg_name == "FRONT END":
                helperMethods.add_pair(dmg_name, dmg_dict)
            elif dmg_name == "REAR END":
                helperMethods.add_pair(dmg_name, dmg_dict)
            elif dmg_name == "MINOR DENT/SCRATCHES":
                helperMethods.add_pair(dmg_name, dmg_dict)
            elif dmg_name == "UNDERCARRIAGE":
                helperMethods.add_pair(dmg_name, dmg_dict)
            else:
                helperMethods.add_pair("MISC", dmg_dict)


        print('***** Damage-Count *****')
        for dmg in dmg_dict:
            count = dmg_dict[dmg]
            print('{0}-{1}'.format(dmg, count))


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
