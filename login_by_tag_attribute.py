from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

userName=driver.find_element_by_css_selector("input[name='txtUsername']")
userName.send_keys("Admin")
#password= driver.find_element_by_css_selector("input#txtPassword")

password= driver.find_element_by_css_selector("input[name='txtPassword']")

password.send_keys("admin123")

# Insertar los valores

time.sleep(5)

login_btn = driver.find_element_by_css_selector("input[type='submit']")
# Hacer clic sobre el boton login
login_btn.click()
#Cierre de la instancia del driver
driver.close()