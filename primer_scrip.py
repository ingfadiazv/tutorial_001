# Importar la libreria de selenium
from selenium import webdriver
# Importar time para darle una espera implicita
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
# Este metodo nos permite maximizar el browser
driver.maximize_window()
# Metodo para hacer referencia a la pagina que se desea navegar
driver.get("https://opensource-demo.orangehrmlive.com/")

# Tiempo de espera implicita
time.sleep(5)
# Metodo para cerrar la instancia de webdriver
driver.quit()
