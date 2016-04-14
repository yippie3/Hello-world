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
element = driver.find_element_by_xpath('//*[@id="tab10href"]')
element.click()

driver.switch_to_frame("Home")
driver.switch_to_frame("List")

table_id = driver.find_element_by_id('ReportOutput')
rows = table_id.find_elements_by_tag_name('tr')

for row in rows[2:]: #from row 2
    col = row.find_elements_by_tag_name('td')[2]
    if col:
        if 'Closed' not in col.text:
            print col.text



#driver.close()
#driver.quit()
