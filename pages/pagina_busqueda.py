from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def select_first_product(self): #Selecciona la primera imagen del producto tras la búsqueda de "iPhone"
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[3]/div/div/div[1]/a/img'))
        )
        product.click()

    def add_to_cart(self): #Hace click en el botón "Add to Cart"
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'button-cart'))
        )
        add_button.click()