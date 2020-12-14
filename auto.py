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

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button = chrome_browser.find_element_by_css_selector('.btn')
print(user_button)
user_message.clear()
user_message.send_keys('Mufassa!!!')
button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'Mufassa!!!' in output_message.get_attribute('innerHTML')

chrome_browser.close()