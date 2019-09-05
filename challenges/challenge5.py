import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dictionaryHelper

class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get('https://www.copart.com')
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def test_filter_for_porsche(self):
        # search for exotics
        search_input = WebDriverWait(self.driver, 10).until(
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

        # extend search to 100 results
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#serverSideDataTable_length select")))
        entries_control = self.driver.find_element_by_css_selector("#serverSideDataTable_length select")
        entries_control.click()
        entries_control.send_keys('100')
        entries_control.send_keys(Keys.ENTER)

        # Get Models
        models = WebDriverWait(self.driver, 15).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-uname="lotsearchLotmodel"]')))
        print('list count', len(models))
        model_list = []
        for item in models:
            model_name = item.text
            model_list.append(model_name)
        sorted_list = sorted(model_list)
        model_dict = {}

        for car_model in sorted_list:
            dictionaryHelper.add_pair(car_model, model_dict)

        print('***** Model-Count *****')
        for model in model_dict:
            count = model_dict[model]
            print('{0}-{1}'.format(model, count))

        # Damages
        dings = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-uname="lotsearchLotdamagedescription"]')))
        damage_list = []
        for dmg_type in dings:
            dmg_name = dmg_type.get_property('text')
            damage_list.append(dmg_name)
        print('list item 1', damage_list[0])
        dmg_dict = {}

        for dmg_type in damage_list:
            if dmg_type == 'REAR END':
                dictionaryHelper.add_pair(dmg_type, dmg_dict)
            elif dmg_type == 'FRONT END':
                dictionaryHelper.add_pair(dmg_type, dmg_dict)
            elif dmg_type == 'MINOR DENT/SCRATCHES':
                dictionaryHelper.add_pair(dmg_type, dmg_dict)
            elif dmg_type == 'UNDERCARRIAGE':
                dictionaryHelper.add_pair(dmg_type, dmg_dict)
            else:
                dmg_type = 'MISC'
                dictionaryHelper.add_pair(dmg_type, dmg_dict)

        print('***** Damage-Count *****')
        for dmg in dmg_dict:
            count = model_dict[dmg]
            print('{0}-{1}'.format(dmg, count))


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
