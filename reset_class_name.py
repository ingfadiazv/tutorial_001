from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

link_reset_password = driver.find_element_by_partial_link_text("Forgot")
link_reset_password.click()

time.sleep(5)
userName = driver.find_element_by_id("securityAuthentication_userName")
userName.send_keys("admin")
time.sleep(5)
reset_password_btn = driver.find_element_by_class_name("searchValues")

reset_password_btn.click()
#driver.close()
