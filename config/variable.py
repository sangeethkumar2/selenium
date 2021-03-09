from selenium import webdriver
browser = "chrome"

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()

browser_url = "https:"

#### Login #######
username = ''
password = '123456'



