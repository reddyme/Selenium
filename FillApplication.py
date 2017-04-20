from selenium import webdriver
import requests,webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
import time


browser=webdriver.Firefox()
#browser.implicitly_wait(30)
browser.maximize_window()

# Read the browser
browser.get('http://careers.bankofamerica.com/job-detail/17023664/united-states/us/java-developer')
#browser.get('https://ghr.wd1.myworkdayjobs.com/Lateral-US/job/Plano/Java-Developer_17023664')
# Click on Apply for this job
applyNowForJob=browser.find_element_by_id('PlhContentWrapper_linkApply')
applyNowForJob.click()


try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "WFXG"))
    WebDriverWait(browser, 3).until(element_present)
    print 'page ready'
    #print browser.page_source
except TimeoutException:
    print "Timed out waiting for page to load"


#time.sleep(30)
for handle in browser.window_handles:
    browser.switch_to.window(handle)
#print browser.page_source

#open tab
browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# Click on Apply button
#<span class="WFXG" title="Apply">Apply</span>
browser.find_element_by_css_selector(".WFXG").click()
#browser.find_element_by_class_name("WFXG").click()

#WCMG
#<div class="WCMG" data-automation-id="userName"><div class="gwt-Label WFMG">Email Address</div><input class="gwt-TextBox WEMG" autocapitalize="none" autocorrect="off" autocomplete="off" aria-label="Email Address" type="text"></div>
print browser.page_source


#time.sleep(10)
userName=browser.find_element_by_class_name("WFVK")
print userName.text
print type(userName)
uuu=browser.find_element_by_id('userName')

userName.send_keys("mahesh.sehwag@gmail.com")
#gwt-Label WFMG
#password=userName=browser.find_element_by_class_name('gwt-Label WFMG')
#password.send_keys('Rockstar#')