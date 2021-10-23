from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)
userName = driver.find_element(By.ID, "txtUsername")
userName.send_keys("Admin")
password = driver.find_element(By.ID, "txtPassword")
password.send_keys("admin123")
time.sleep(3)
login_btn = driver.find_element(By.ID, "btnLogin")
login_btn.click()

# LINK_TEXT
user = driver.find_element(By.LINK_TEXT, "Welcome Paul")
user.click()
time.sleep(3)
# PARTIAL_LINK_TEXT
link_logout = driver.find_element(By.PARTIAL_LINK_TEXT, "Log")
link_logout.click()
time.sleep(3)
driver.close()
