from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/dark-hack/index.html")

        # Scroll down to trigger animations if any, and ensure full page is loaded
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1) # Wait for animations

        page.screenshot(path="jules-scratch/verification/dark_hack_verification.png", full_page=True)
        browser.close()

run()