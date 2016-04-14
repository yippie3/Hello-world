import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select


chromedriver = "/home/zzhao/tool_folder/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

teamtrack = "https://qms.brocade.com/tmtrack/tmtrack.dll?"
driver.get(teamtrack)
driver.implicitly_wait(10) # seconds, this is important, otherwise the chrome page are not ready to find element and input any 
driver.maximize_window()

element = driver.find_element_by_id('authUID')
element.send_keys('zzhao')

element = driver.find_element_by_id('authPWD')
element.send_keys('vitaminc2016')

#element.send_keys(Keys.RETURN) #no need for this, there is no RETURN involved

driver.find_element_by_id('logonButton').click()
print driver.title


time.sleep(1)
#element = driver.find_element_by_xpath('//*[@id="brocadebar"]/table/tbody/tr/td[2]/a')
#element.click()


#driver.close()
#driver.quit()
