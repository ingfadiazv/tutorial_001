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


pim_menu = driver.find_element(By.ID, "menu_pim_viewPimModule")
pim_menu.click()
time.sleep(3)
menu_pim_conf = driver.find_element(By.ID, "menu_pim_Configuration")
menu_pim_conf.click()
time.sleep(1)

menu_pim_conf_pim = driver.find_element(By.ID, "menu_pim_configurePim")
menu_pim_conf_pim.click()

# Lista de checkbox
list_checkbox = driver.find_elements(By.CSS_SELECTOR,"li[class='checkbox']>input")

edit_btn = driver.find_element( By.ID, "btnSave" )

for checkbox in list_checkbox:
    if checkbox.is_displayed() is True and checkbox.is_enabled() is False:
        edit_btn.click()
        time.sleep(3)
# para ver si estan en pantalla las opciones
    if checkbox.is_displayed() is True and checkbox.is_selected() is False:
        time.sleep(1)
        checkbox.click()
    else:
        checkbox.click()

edit_btn.click()






