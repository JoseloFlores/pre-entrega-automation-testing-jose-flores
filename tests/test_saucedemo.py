"""Tests de pre-entrega: saucedemo.com.

Base inicial: solo login. Catálogo y carrito se agregan en próximos commits.
Cada test es independiente (hace su propio login vía helpers).
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import (
    login_as_standard_user,
    INVENTORY_TITLE,
    APP_LOGO,
    INVENTORY_URL_FRAGMENT,
    TIMEOUT,
)


def test_login_exitoso(driver):
    """Login con credenciales válidas redirige a /inventory.html."""
    login_as_standard_user(driver)

    wait = WebDriverWait(driver, TIMEOUT)

    # 1. Validación de URL
    assert INVENTORY_URL_FRAGMENT in driver.current_url, (
        f"URL esperada con {INVENTORY_URL_FRAGMENT}, actual: {driver.current_url}"
    )

    # 2. Validación de textos clave: "Products" y "Swag Labs"
    titulo = wait.until(EC.visibility_of_element_located(INVENTORY_TITLE)).text
    assert titulo == "Products", f"Título esperado 'Products', actual: '{titulo}'"

    logo = wait.until(EC.visibility_of_element_located(APP_LOGO)).text
    assert logo == "Swag Labs", f"Logo esperado 'Swag Labs', actual: '{logo}'"
