# Pre-Entrega Automation Testing — SauceDemo

Automatización de flujos básicos en [saucedemo.com](https://www.saucedemo.com)
con **Python + Selenium WebDriver + Pytest**.

## Propósito
- Login con credenciales válidas (`standard_user` / `secret_sauce`) y validación de redirección a `/inventory.html` + textos `Products` / `Swag Labs`.
- Carrito: agregar el primer producto, verificar badge `1` con espera explícita (`WebDriverWait`), navegar a `/cart.html` y comprobar que el producto listado coincide.

## Tecnologías
- Python 3.13
- Selenium 4 + webdriver-manager (descarga automática del ChromeDriver)
- Pytest + pytest-html (reporte HTML)
- Git / GitHub

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
```bash
pytest -v --html=reports/reporte.html
# solo carrito:
pytest tests/test_saucedemo.py -v -k carrito --html=reports/reporte.html
```

## Tests
| Test | Qué valida |
| ---- | ---------- |
| `test_login_exitoso` | Redirección a `/inventory.html` + `Products` / `Swag Labs` |
| `test_carrito_agregar_producto` | Add primer producto → badge `1` (espera explícita) |
| `test_carrito_navegar_y_verificar_producto` | Navega a `/cart.html` y verifica el producto agregado |

## Estructura
```
.
├── conftest.py          # fixture driver (Chrome + screenshot en fallo)
├── tests/               # tests (test_saucedemo.py)
├── utils/               # funciones auxiliares (helpers.py: login, carrito, localizadores)
├── datos/               # (no usado: credenciales por defecto en helpers)
└── reports/             # reporte HTML y capturas
```

## Commits
Mensajes descriptivos por avance (`chore:`, `feat:`, `docs:`...).
