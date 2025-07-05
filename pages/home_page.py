from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name): #Localiza el campo de búsqueda y escribe la palabra "iPhone"
        # Espera que el campo de búsqueda esté presente
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search"]/input'))
        )
        search_box.clear()
        search_box.send_keys(product_name + Keys.RETURN)