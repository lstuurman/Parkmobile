from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from login import *
global browser
#browser = StartBrowser()
Login()
time.sleep(5)
StartParking()
print(datetime.now().strftime("%m-%d-%Y, %H:%M:%S") + ' : Parking Started')


