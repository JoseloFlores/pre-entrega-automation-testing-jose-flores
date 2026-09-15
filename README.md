# Pre-Entrega Automation Testing — SauceDemo

Automatización de flujos básicos en [saucedemo.com](https://www.saucedemo.com)
con **Python + Selenium WebDriver + Pytest**.

## Propósito
- Login con credenciales válidas (`standard_user` / `secret_sauce`) y validación de redirección a `/inventory.html` + textos `Products` / `Swag Labs`.
- (En progreso) Verificación de catálogo y carrito.

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
# solo login (base actual):
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

## Estructura
```
.
├── conftest.py          # fixture driver (Chrome + screenshot en fallo)
├── tests/               # tests (test_saucedemo.py)
├── utils/               # funciones auxiliares (helpers.py: login, localizadores)
├── datos/               # datos externos CSV/JSON (si aplica)
└── reports/             # reporte HTML y capturas
```

## Commits
Mensajes descriptivos por avance (`chore:`, `feat:`, `docs:`...).
