"""Tests de pre-entrega-Jose-Flores

Flujos: login + carrito (agregar, badge, verificación en /cart.html).
Cada test es independiente (hace su propio login vía helpers).
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import (
    login_as_standard_user,
    add_first_product_to_cart,
    go_to_cart_and_get_names,
    INVENTORY_TITLE,
    APP_LOGO,
    INVENTORY_URL_FRAGMENT,
    CART_BADGE,
    CART_URL_FRAGMENT,
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


def test_carrito_agregar_producto(driver):
    """Agregar el primer producto incrementa el badge del carrito a 1."""
    login_as_standard_user(driver)

    wait = WebDriverWait(driver, TIMEOUT)

    # Agrega el primer producto (incluye espera explícita del badge == "1")
    add_first_product_to_cart(driver)

    # Verificación redundante del badge para mensaje de error claro
    badge = wait.until(EC.visibility_of_element_located(CART_BADGE)).text
    assert badge == "1", f"Badge esperado '1', actual: '{badge}'"
    print("Test OK: producto agregado, badge = 1")


def test_carrito_navegar_y_verificar_producto(driver):
    """El producto agregado aparece listado en la página del carrito."""
    login_as_standard_user(driver)

    # Agrega y guarda el nombre esperado
    expected_name = add_first_product_to_cart(driver)

    # Navega al carrito y obtiene los nombres listados
    cart_names = go_to_cart_and_get_names(driver)

    # Validación de URL del carrito
    assert CART_URL_FRAGMENT in driver.current_url, (
        f"URL esperada con {CART_URL_FRAGMENT}, actual: {driver.current_url}"
    )

    # El producto agregado debe estar en la lista del carrito
    assert expected_name in cart_names, (
        f"Producto '{expected_name}' no encontrado en carrito: {cart_names}"
    )
    print(f"Test OK: '{expected_name}' visible en el carrito")
