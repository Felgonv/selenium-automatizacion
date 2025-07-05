import os
import time

def take_screenshot(driver, name="screenshots"):
    # Crea un nombre único usando fecha y hora
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name}_{timestamp}.png"
    
    # Se crea una carpeta screenshots si no existe
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    # Ruta final de la imagen
    path = os.path.join(screenshots_dir, filename)
    
    # Guarda la captura
    driver.save_screenshot(path)
    print(f" Captura guardada: {path}")