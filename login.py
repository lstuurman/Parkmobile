from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

def StartBrowser():
    opts = Options()
    #opts.headless = True
    #assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    browser.get('https://account.parkmobile.com/login')
    time.sleep(3)
    cookie = browser.find_element_by_css_selector('button.optanon-allow-all.accept-cookies-button')
    cookie.click()
    return browser


def Login():
    user_input = browser.find_element_by_id('username')
    user_input.clear()
    user_input.send_keys('laurensstuurman678@hotmail.com')

    password = browser.find_element_by_id('login_password')
    password.clear()
    password.send_keys('Boeddha1994')

    submitEl = browser.find_element_by_css_selector('button.btn.btn-primary.btn-block')#.btn.btn-primary.btn-block
    submitEl.click()

    print(browser.current_url)
    browser.get('https://account.parkmobile.com/parking/parking-sessions')
    print(browser.current_url)


def StartParking():
    start_parking_form = browser.find_element_by_id('zone')
    print(start_parking_form)
    child=start_parking_form.find_element(By.XPATH,'.//*')
    children=child.find_element(By.XPATH,'.//*')
    children.send_keys('15812')
    time.sleep(2)
    children.send_keys(Keys.DOWN)
    time.sleep(2)
    children.send_keys(Keys.RETURN)
    # time.sleep(2)
    # children.send_keys(Keys.RETURN)

def StopParking():
    active_parking = browser.find_element_by_id('clr-dg-row1')
    active_parking.click()
    time.sleep(2)
    #stop_parking = browser.find_element_by_css_selector('button.btn.btn-danger.btn-block')
    stop_parking = browser.find_element_by_css_selector('pn-stop-parking-session.ng-star-inserted')
    stop_parking.click()
    time.sleep(.5)
    stop_div = browser.find_element_by_css_selector('div.modal-content-wrapper.ng-tns-c124-12')
    stop_div = browser.find_element_by_css_selector('div.modal-footer.centered.ng-tns-c124-12')
    stop_div.click()
    #stop_parking.click()
    # stop_div.send_keys(Keys.TAB)
    # stop_div.send_keys(Keys.TAB)
    # stop_div.send_keys(Keys.TAB)
    # stop_div.send_keys(Keys.ENTER)
    # time.sleep(2)
    # stop_parking = browser.find_element_by_css_selector('button.btn.btn-danger')
    # stop_parking.click()

global browser
browser = StartBrowser()
Login()
time.sleep(1)
# time.sleep(5)
# StartParking()
# print('Parking Started')
# time.sleep(10)
StopParking()
# browser.close()
# browser.quit()


  