# Funciones auxiliares para los tests de saucedemo.com

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")       # id único
PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")       # id único
LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")      # id único
INVENTORY_TITLE = (By.CSS_SELECTOR, ".title")          # "Products"
APP_LOGO = (By.CSS_SELECTOR, ".app_logo")             # "Swag Labs"


INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")              # tarjetas de producto
FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")      # nombre dentro de cada tarjeta
FIRST_ADD_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")  # botón Add to cart
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")             # contador del carrito
CART_LINK = (By.CLASS_NAME, "shopping_cart_link")               # ícono del carrito
CART_ITEM = (By.CLASS_NAME, "cart_item")                        # fila de producto en /cart.html

BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL_FRAGMENT = "/inventory.html"
CART_URL_FRAGMENT = "/cart.html"
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


def add_first_product_to_cart(driver):
    """Agrega el primer producto del catálogo al carrito.

    Requiere haber hecho login antes (ver login_as_standard_user).
    Espera explícitamente a que el badge del carrito sea visible
    y muestre "1".

    Args:
        driver: instancia de Selenium WebDriver ya en /inventory.html.

    Returns:
        str: nombre del producto agregado (para verificar luego en el carrito).
    """
    wait = WebDriverWait(driver, TIMEOUT)

    # Asegura que el catálogo cargó (al menos 1 producto visible)
    wait.until(EC.visibility_of_element_located(INVENTORY_ITEMS))

    # Guarda el nombre del primer producto antes de agregarlo
    product_name = driver.find_elements(*FIRST_PRODUCT_NAME)[0].text

    # Click en el primer botón "Add to cart"
    wait.until(EC.element_to_be_clickable(FIRST_ADD_BUTTON)).click()

    # Espera explícita del badge con texto "1" (consigna Clase 8)
    wait.until(EC.visibility_of_element_located(CART_BADGE))
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, "1"))

    return product_name


def go_to_cart_and_get_names(driver):
    """Navega al carrito y retorna los nombres de productos listados.

    Args:
        driver: instancia de Selenium WebDriver.

    Returns:
        list[str]: nombres de productos visibles en /cart.html.
    """
    wait = WebDriverWait(driver, TIMEOUT)

    driver.find_element(*CART_LINK).click()

    # Espera explícita: redirección al carrito + al menos 1 item visible
    wait.until(EC.url_contains(CART_URL_FRAGMENT))
    wait.until(EC.visibility_of_element_located(CART_ITEM))

    return [el.text for el in driver.find_elements(*FIRST_PRODUCT_NAME)]
