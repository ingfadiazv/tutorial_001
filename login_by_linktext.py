from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Se debe colocar todo el texto del hipervinculo
link_rest_pasword= driver.find_element_by_link_text("Forgot your password?")
link_rest_pasword.click()
time.sleep(5)

driver.close()