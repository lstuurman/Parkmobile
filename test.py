from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://account.parkmobile.com/login')

user_input = browser.find_element_by_id('username')
user_input.clear()
user_input.send_keys('laurensstuurman678@hotmail.com')

password = browser.find_element_by_id('login_password')
password.clear()
password.send_keys('Boeddha1994')

submitEl = browser.find_element_by_class_name('btn btn-primary btn-block')
result = ActionChains(browser).click(submitEl).perform()
print(result)


# search_form.send_keys('real python' + Keys.RETURN)
# search_form.submit()

# results = browser.find_elements_by_class_name('result')
# print(results)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

# #This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Firefox() as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
#     print(first_result.get_attribute("textContent"))
  