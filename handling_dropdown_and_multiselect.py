import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

class HandlingSelectTag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once before the setup method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will et executed only once after the teardown method for the last test")

    def setUp(self): #pre test confir
        print("This will get executed before every test")
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\SIDDHARTHPHUKANE\PycharmProjects\durongclass\resources\chromedriver.exe")  # keyword argument and not positional argiment
        self.driver.maximize_window()

    def tearDown(self): #post test clearance
        print("This will get excuted after every test")
        #self.driver.quit()
    def test_combo(self):
        print("This test is to learn how to handle dropdown ")
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        make_element = self.driver.find_element_by_name("make")
        make_select = Select(make_element)
        time.sleep(5)
        make_select.select_by_visible_text("Mercedes")
        time.sleep(3)
        make_select.select_by_index(2)
        time.sleep(10)

    #def test_multi_select(self):
        #print("This test is to learn how to handle multiselect")

if __name__ == "__main__":
    unittest.main()
