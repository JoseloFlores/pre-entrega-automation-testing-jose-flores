"""Funciones auxiliares para los tests de saucedemo.com."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Localizadores (estrategia: id único > CSS estable, sin XPaths absolutos) ---
USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")       # id único
PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")       # id único
LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")      # id único
INVENTORY_TITLE = (By.CSS_SELECTOR, ".title")          # "Products"
APP_LOGO = (By.CSS_SELECTOR, ".app_logo")             # "Swag Labs"

BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL_FRAGMENT = "/inventory.html"
TIMEOUT = 10


def login_as_standard_user(driver, username="standard_user", password="secret_sauce"):
    """Navega al login, ingresa credenciales válidas y espera el inventario.

    Args:
        driver: instancia de Selenium WebDriver.
        username: usuario (default standard_user).
        password: contraseña (default secret_sauce).
    """
    wait = WebDriverWait(driver, TIMEOUT)
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located(USERNAME_INPUT)).send_keys(username)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

    # Espera explícita: redirección al inventario
    wait.until(EC.url_contains(INVENTORY_URL_FRAGMENT))
