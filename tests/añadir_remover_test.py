import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.pagina_busqueda import SearchResultsPage
from pages.pagina_carrito import CartPage
from utils.screenshots import take_screenshot

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        driver_path = os.path.abspath("drivers/chromedriver.exe")
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://opencart.abstracta.us/")

    def test_add_and_remove_product(self):
        try:
            home = HomePage(self.driver)
            search = SearchResultsPage(self.driver)
            cart = CartPage(self.driver)

            # Paso 1: Buscar producto
            home.search_product("iPhone")
            take_screenshot(self.driver, "01_busqueda")

            # Paso 2: Seleccionar y agregar al carrito
            search.select_first_product()
            search.add_to_cart()
            take_screenshot(self.driver, "02_agregado_carrito")

            #Asersión (Validación) de agregado exitoso
            success_alert = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
            )
            self.assertIn("Success: You have added", success_alert.text) #Esto está en inglés debido al lenguaje de la página

            # Paso 3: Ir al carrito y eliminar el producto agregado
            cart.view_cart()
            take_screenshot(self.driver, "03_vista_carrito")
            cart.remove_product()
            take_screenshot(self.driver, "04_eliminado_carrito")

            #Asersión confirmación de carrito vacío
            cart_rows = self.driver.find_elements(By.CSS_SELECTOR, ".table-responsive tbody tr")
            self.assertEqual(len(cart_rows), 0, "El carrito aún contiene productos")


        except Exception as e:
            take_screenshot(self.driver, "error")
            self.fail(f"Test falló por: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()