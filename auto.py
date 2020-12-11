from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

print(chrome_browser)
# The chrome browswer opens up.

chrome_browser.maximize_window()
# The difference between the chrome_browser and the chrome_browser.maximize_window()
# is that the former opens a minimized window and the latter opens a full window.

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title
# When the assert method is used, when True, the code runs. If false, the assetion error
# occurs.  

button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML'))