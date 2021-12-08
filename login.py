from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

def StartBrowser():
    opts = Options()
    opts.set_headless(headless=True)
    #opts.set_headless(headless=True)
    #assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)
    browser.get('https://account.parkmobile.com/login')
    time.sleep(2)
    try:
        cookie = browser.find_element_by_css_selector('button.optanon-allow-all.accept-cookies-button')
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

    submitEl = browser.find_element_by_css_selector('button.btn.btn-primary.btn-block')#.btn.btn-primary.btn-block
    submitEl.click()

    print(browser.current_url)
    browser.get('https://account.parkmobile.com/parking/parking-sessions')

    if browser.current_url != 'https://account.parkmobile.com/parking/parking-sessions':
        Login()

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
    time.sleep(2)

    # start_parking = browser.find_element_by_css_selector('button.btn.btn-success-outline.btn-block')
    # start_parking = browser.find_element_by_css_selector('button.btn.btn-primary.btn-block.ng-tns-c36-8')
    start_parking = browser.find_element_by_css_selector('span.ng-tns-c36-11.ng-trigger.ng-trigger-defaultButton.ng-star-inserted')
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
    stop_parking = browser.find_element_by_css_selector('pn-stop-parking-session.ng-star-inserted')
    stop_parking.click()
    time.sleep(.5)
    #stop_div = browser.find_element_by_css_selector('div.modal-content-wrapper.ng-tns-c124-12')
    #modal-footer centered ng-tns-c128-15
    stop_div = browser.find_element_by_css_selector('div.modal-footer.centered.ng-tns-c128-15')
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


  
