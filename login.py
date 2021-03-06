from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException,ElementClickInterceptedException,UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
import time

def StartBrowser():
    opts = Options()
    #opts.set_headless(headless=True)
    opts.set_headless(headless=True)
    #assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    browser.get('https://account.parkmobile.com/login')
    time.sleep(5)
    #cookie = browser.find_elements_by_xpath("//*[contains(text(), 'Cookies accepteren')]")[0]
    try:
        #cookie = browser.find_element_by_css_selector('button.optanon-allow-all.accept-cookies-button')
        cookie = browser.find_elements_by_xpath("//*[contains(text(), 'Cookies accepteren')]")[0]
        cookie.click()
    except:
        print('NO COOKIES ?')
    return browser


def Login():
    user_input = browser.find_element_by_id('username')
    user_input.clear()
    user_input.send_keys('laurensstuurman678@hotmail.com')

    password = browser.find_element_by_id('login_password')
    password.clear()
    password.send_keys('Boeddha1994')

    waiter = WebDriverWait(browser,20,ignored_exceptions=[TimeoutException]) #,ignored_exceptions=[NoSuchElementException]
    time.sleep(5)
    submitEl = waiter.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Log in')]")))
    #submitEL = waiter.until(EC.invisibility_of_element_located((By.XPATH,"//*[contains(text(),'Log in')]")))
    submitEl.click()

    # submitEl = browser.find_element_by_css_selector('button.btn.btn-primary.btn-block')#.btn.btn-primary.btn-block
    # submitEl = browser.find_elements_by_xpath("//*[contains(text(), 'Log in')]")[0]
    # submitEl.click()

    print(browser.current_url)
    browser.get('https://account.parkmobile.com/parking/parking-sessions')

    if browser.current_url != 'https://account.parkmobile.com/parking/parking-sessions':
        Login()

    print(browser.current_url)


def StartParking():

    waiter = WebDriverWait(browser,20,ignored_exceptions=[TimeoutException]) #,ignored_exceptions=[NoSuchElementException]
    submitEl = waiter.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Start a new session')]")))
    submitEl.click()

    start_parking_form = browser.find_element_by_id('zone')
    print(start_parking_form)
    child=start_parking_form.find_element(By.XPATH,'.//*')
    children=child.find_element(By.XPATH,'.//*')
    children.send_keys('15812')
    time.sleep(2)
    children.send_keys(Keys.DOWN)
    time.sleep(2)
    children.send_keys(Keys.RETURN)
    time.sleep(2)

    # start_parking = browser.find_element_by_css_selector('button.btn.btn-success-outline.btn-block')
    # start_parking = browser.find_element_by_css_selector('button.btn.btn-primary.btn-block.ng-tns-c36-8')
    #start_parking = browser.find_element_by_css_selector('span.ng-tns-c36-11.ng-trigger.ng-trigger-defaultButton.ng-star-inserted')
    start_parking = browser.find_elements_by_xpath("//*[contains(text(), 'Start this parking')]")[0]
    # ng-tns-c36-11 ng-trigger ng-trigger-defaultButton ng-star-inserted
    
    start_parking.click()
    #time.sleep(4)
    browser.delete_all_cookies()
    browser.close()
    browser.quit()



def StopParking():
    active_parking = browser.find_element_by_id('clr-dg-row1')
    active_parking.click()
    time.sleep(2)
    #stop_parking = browser.find_element_by_css_selector('button.btn.btn-danger.btn-block')
    #stop_parking = browser.find_element_by_css_selector('pn-stop-parking-session.ng-star-inserted')
    stop_parking = browser.find_elements_by_xpath("//*[contains(text(), 'Stop this session')]")[0]
    stop_parking.click()
    time.sleep(1)
    #stop_div = browser.find_element_by_css_selector('div.modal-content-wrapper.ng-tns-c124-12')
    #modal-footer centered ng-tns-c128-15
    #stop_div = browser.find_element_by_css_selector('div.modal-footer.centered.ng-tns-c128-15')
    stop_div = browser.find_elements_by_xpath("//*[contains(text(), 'Stop this session')]")[-1]
    stop_div.click()
    browser.delete_all_cookies()
    browser.close()
    browser.quit()



global browser
browser = StartBrowser()
# Login()
# time.sleep(5)
# for our in [9,12,15,19]:
# 	browser = StartBrowser()
# 	Login()
# 	time.sleep(5)
# 	# time.sleep(5)
# 	StartParking()
# 	print('Parking Started')
# 	time.sleep(10)
# 	browser.close()
# 	browser.quit()
	
# 	time.sleep(10392)#397)#50010392
# 	browser=StartBrowser()
# 	Login()
# 	time.sleep(3)
# 	StopParking()
# 	print('Stopped Parking')
# 	browser.close()
# 	browser.quit()
# 	time.sleep(297)#97)#00
# # time.sleep(10)
# #StopParking() 
# #print('Parking Stopped')
# browser.close()
# browser.quit()


  
