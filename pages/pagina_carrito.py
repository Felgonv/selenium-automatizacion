from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def view_cart(self): #Abre la pestaña del carrito y entra en el detalle con "View Cart"
        # Clic en el total del carrito (ícono del carrito)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'cart-total'))
        ).click()

        # Clic en "View Cart"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[1]/strong'))
        ).click()

    def remove_product(self):
        # Clic en el ícono de eliminar producto
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]/i'))
        ).click()

        # Esperar a que la fila del producto desaparezca
         WebDriverWait(self.driver, 10).until(
             EC.invisibility_of_element_located((By.CSS_SELECTOR, ".table-responsive tbody tr"))
             )