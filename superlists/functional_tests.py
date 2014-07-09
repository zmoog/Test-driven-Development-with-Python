from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-DO' in browser.title

# She is invited to enter a to-do item straight away

# ...

# Satisfied, she goes back to sleep

browser.quit()
