import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select


chromedriver = "/home/zzhao/tool_folder/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

rqm = "https://clmprod.brocade.com/qm/web/console"
driver.get(rqm)
driver.implicitly_wait(10) # seconds, this is important, otherwise the chrome page are not ready to find element and input any 
driver.maximize_window()

element = driver.find_element_by_id('jazz_app_internal_LoginWidget_0_userId')
element.send_keys('zzhao')

element = driver.find_element_by_id('jazz_app_internal_LoginWidget_0_password')
element.send_keys('vitaminc2016')

#element.send_keys(Keys.RETURN) #no need for this, there is no RETURN involved
driver.find_element_by_xpath('//*[@id="jazz_app_internal_LoginWidget_0"]/div[1]/div[1]/div[3]/form/button').click()
print driver.title


time.sleep(1)
element = driver.find_element_by_id('jazz_ui_ResourceLink_0')
element.click()
element = driver.find_element_by_id('jazz_ui_MenuPopup_8')
element.click()
element = driver.find_element_by_id('jazz_ui_menu_MenuItem_0_text')
element.click()

element = driver.find_element_by_id('table-groupby-select-com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0')
select = Select(element)
select.select_by_visible_text("Owner")

element = driver.find_element_by_id('com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0-filter-input')
element.send_keys(sys.argv[1])
time.sleep(10)

element = driver.find_element_by_id('com_ibm_asq_common_web_ui_internal_widgets_tableViewer_TableViewer_0-select-page-range')
select = Select(element)
select.select_by_visible_text('100')
time.sleep(10)

#raw_input("Press Enter to continue...")
#driver.close()
#driver.quit()
