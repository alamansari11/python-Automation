from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import os
#
# driver = webdriver.Chrome(executable_path="C:/Users/Alam/Desktop/internship/chromedriver.exe")
#
# driver.get("https://www.atg.party/")
# print(driver.title)
# driver.close()
import json
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




def get_status(logs):
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            try:
                content_type = 'text/html' in d['message']['params']['response']['headers']['content-type']
                response_received = d['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    return d['message']['params']['response']['status']
            except:
                pass

chromedriver_path = "C:/Users/Alam/Desktop/internship/chromedriver.exe"
url = "https://www.atg.party/"
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

browser = WebDriver(chromedriver_path, desired_capabilities=capabilities)
browser.get(url)
logs = browser.get_log('performance')
print(get_status(logs))

#
# driver = webdriver.Chrome(executable_path="C:/Users/Alam/Desktop/internship/chromedriver.exe")
# driver.get("https://www.atg.party/")
navigationStart = browser.execute_script("return window.performance.timing.navigationStart")
responseStart = browser.execute_script("return window.performance.timing.responseStart")
domComplete = browser.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)
browser.implicitly_wait(10)   #this will keep the program to wait for 10 seconds before throwing exception
# time.sleep(2)
login = browser.find_element_by_xpath("/html/body/div[5]/header/div[1]/div[2]/div/ul/li[2]/a")
login.click()

# time.sleep(2)
emailAddress = "wiz_saurabh@rediffmail.com"
pas = "Pass@123"
email = browser.find_element_by_id('email_landing')
email.send_keys(emailAddress)
password = browser.find_element_by_id('password_landing')
password.send_keys(pas)
# time.sleep(3)
signin = browser.find_element_by_xpath("/html/body/div[5]/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button")
signin.click()

# time.sleep(3)
dropdown =  browser.find_element_by_id('create-btn-dropdown')
dropdown.click()
# time.sleep(3)
article = browser.find_element_by_xpath("//*[@id='create_post-user__info']/div[1]/div/div/a[1]")
article.click()


# cover =  browser.find_element_by_id("cover_image")
# cover.send_keys(os.getcwd()+"/Pictures/Saved Pictures/image.jpg")


# time.sleep(5)
title = browser.find_element_by_id('title')
title.click()
title.send_keys("IRON MAN")
description = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div")
description.click()
description.send_keys("Genius,Billionaire,Philanthropist.")

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/input").send_keys("C:/Users/Alam/Pictures/Saved Pictures/image.jpg")


time.sleep(5)
post = browser.find_element_by_xpath("/html/body/div[2]/div[1]/nav/div/div[3]/div/div[2]/button")
post.click()
# time.sleep(8)
print(browser.title)
# browser.quit()