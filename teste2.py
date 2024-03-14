from playwright.sync_api import sync_playwright
import time

# Esquema de Eventos

def event_handler(request):
    print(request.url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.on('request' , event_handler)

    browser.close()