from playwright.sync_api import sync_playwright
import time

# Esquema de navegação

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://dgg.gg')

    time.sleep(1)

    page.goto('http://google.com')

    time.sleep(1)

    page.go_back() # Voltar a pagina anterior

    time.sleep(1)

    page.go_forward() # Ir para uma próxima página

    time.sleep(1)

    browser.close() # Fecha o Browser