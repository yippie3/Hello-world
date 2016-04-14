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


time.sleep(5)
element = driver.find_element_by_xpath('//*[@id="brocadebar"]/table/tbody/tr/td[2]/a')
element.click()

driver.switch_to_frame("Home")
driver.switch_to_frame("view")


'''
#-----------------------------this part is for showing all the option------------------------------
mat = '(F\d+)'
src = driver.page_source

g = re.findall(mat,src)

g = set(g)

for i in g:
    print i
    try: 
        element = driver.find_element_by_name("{}".format(i))
    except:
        print "cant find {}".format(i)
    else:
        try:
            select = Select(element)
        except:
            print "cant do select on {}".format(i)
        else:
            print "options we have are:\n"
            print [o.text for o in select.options]
            if i == "F1359": 
                select.select_by_visible_text("SQA")
            elif i == "F1347":
                select.select_by_visible_text("Medium")
            elif i == "F1515":
                select.select_by_visible_text("Nightly")
'''

element = driver.find_element_by_name("F1359")
select = Select(element)
select.select_by_visible_text("SQA")

element = driver.find_element_by_name("F1347")
select = Select(element)
select.select_by_visible_text("Medium")

element = driver.find_element_by_name("F2128")
select = Select(element)
select.select_by_visible_text("Easy to Reproduce")

element = driver.find_element_by_name("F1372")
select = Select(element)
select.select_by_visible_text("Medium")

element = driver.find_element_by_name("F4422")
select = Select(element)
select.select_by_visible_text("Not Sure")

#summary
element = driver.find_element_by_name("F1337")
element.send_keys("sum")
#syptoms
element = driver.find_element_by_name("F2101")
element.send_keys("syp")

element = driver.find_element_by_name("F1350")
select = Select(element)
select.select_by_visible_text("Brocade SLX-OS")

element = driver.find_element_by_name("F1351")
select = Select(element)
select.select_by_visible_text("SLXOS 16r.1.00")

element = driver.find_element_by_name("F1515")
select = Select(element)
select.select_by_visible_text("Nightly")


raw_input("Press Enter to continue...")

#driver.close()
#driver.quit()
