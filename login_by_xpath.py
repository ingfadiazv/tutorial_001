from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

userName=driver.find_element_by_xpath("//input[@name='txtUsername']")
password= driver.find_element_by_xpath("//input[@name='txtPassword']")




# Insertar los valores

userName.send_keys("Admin")
password.send_keys("admin123")
time.sleep(5)

login_btn=driver.find_element_by_xpath("//input[@type='submit']")
# Hacer clic sobre el boton login
login_btn.click()
#Cierre de la instancia del driver
driver.close()