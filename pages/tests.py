from splinter import Browser
import time

with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    time.sleep(30)
    button = browser.find_by_name('btnK')
    # Interact with elements
    button.click()