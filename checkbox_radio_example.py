from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path =r"C:\Users\SIDDHARTHPHUKANE\PycharmProjects\durongclass\resources\chromedriver.exe")   #keyword argument and not positional argiment
driver.maximize_window()
driver.get("http://cookbook.seleniumacademy.com/Config.html")
print("test")
print("test2")

make = driver.find_element_by_xpath("//select[@name='make']")


fuel_type = driver.find_element_by_xpath("//input[@name='fuel_type'][@value='Diesel']")
fuel_type.click()

airbags = driver.find_element_by_name("airbags")

if not airbags.is_selected(): #unchecking the checkbox
    airbags.click()
time.sleep(3)

if airbags.is_selected(): #unchecking the checkbox
    airbags.click()




