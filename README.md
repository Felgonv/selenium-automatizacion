# 🧪 Proyecto de Automatización QA - Selenium con Python

Este proyecto automatiza casos de prueba funcionales de una aplicación web utilizando **Selenium WebDriver**, estructurado bajo el **patrón Page Object Model (POM)**.

---

## 🛠️ Tecnologías y Librerías Usadas

- **Python 3**
- **Selenium**: para la interacción con elementos web.
- **Unittest**: framework de pruebas nativo de Python.
- **ChromeDriver**: como driver del navegador para Chrome.

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

##    ESTRUCTURA DEL PROYECTO

Proyecto_autom/
├── pages/             # Clases que modelan páginas (POM)
├── tests/             # Casos de prueba
├── drivers/           # WebDriver ejecutable
├── requirements.txt   # Librerías utilizadas
├── README.md          # Documentación del proyecto
└── .gitignore         # Archivos ignorados

🎯 Elección de Selectores
Se priorizaron selectores estables y confiables

ID (By.ID): rápido y confiable.
Name (By.NAME): útil si el campo lo define.
XPath (By.XPATH): usado en casos donde no existen IDs o hay que ubicar elementos relativos.
CSS Selectors (By.CSS_SELECTOR): alternativo cuando XPath se vuelve complejo.

La elección se basa en estabilidad frente a cambios visuales, facilidad de lectura y mantenibilidad del código.

Assertions (Aserciones)
Las validaciones (assert) se usaron para comprobar:
Que los elementos esperados están presentes tras acciones (ej: login exitoso).
Que mensajes o estados del DOM coincidan con lo esperado (ej: “Producto agregado”).
Que flujos completos (ej: agregar y eliminar del carrito) cumplan su comportamiento esperado.
Se utilizó self.assertIn, self.assertTrue y self.assertEqual desde el módulo unittest.

Patrón de Diseño: Page Object Model (POM)
Este patrón permite:
Separar la lógica de las páginas de los casos de prueba.
Reutilizar código en distintas pruebas.
Mejorar la mantenibilidad ante cambios de interfaz.
Cada página tiene su propia clase con los métodos que representan acciones posibles (ej: LoginPage.login_usuario()).

PARA EJECUTAR LAS PRUEBAS
python -m unittest discover tests

---

###
