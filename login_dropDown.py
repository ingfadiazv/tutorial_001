from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

#
admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
admin.click()
#Uso de los metodos de Select
userRoles = Select(driver.find_element(By.ID, "searchSystemUser_userType"))
userRoles.select_by_index(2)

#status = Select(driver.find_element(By.ID, "searchSystemUser_status"))
#status.select_by_visible_text("Enabled")

status = Select(driver.find_element(By.ID, "searchSystemUser_status"))
status.select_by_value("1")

search_btn = driver.find_element(By.ID, "searchBtn")
search_btn.click()
time.sleep(5)
driver.close()
