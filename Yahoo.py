from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path =r"C:\Users\SIDDHARTHPHUKANE\PycharmProjects\durongclass\resources\chromedriver.exe")   #keyword argument and not positional argiment
driver.maximize_window()
driver.get("https://login.yahoo.com/")
ele= driver.find_element_by_id("login-username")
ele.send_keys("siddhup1")
driver.find_element_by_id("login-signin").submit()
time.sleep(5)
driver.find_element_by_id("login-passwd").send_keys("123456")
time.sleep(5)
driver.find_element_by_id("login-signin").submit()


driver.find_element_by_xpath("//lable[contains(text(),'Username')]").text
