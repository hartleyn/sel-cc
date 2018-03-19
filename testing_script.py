from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xpath_generator
import test_base
import general_actions.actions

driver = test_base.driver
driver.get("https://avalara.okta.com/login/default")

time.sleep(5)

elem = driver.find_element_by_id("okta-signin-username")
elem.clear()
elem.send_keys("nick.hartley@avalara.com")

pass_field = driver.find_element_by_id("okta-signin-password")
pass_field.clear()
pass_field.send_keys("WTcc2009")
pass_field.send_keys(Keys.RETURN)
#driver.close()

time.sleep(5)

beta4 = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/ul[2]/li[12]/a") # xpath to the beta4.certcapture Okta link
beta4.click()

print(driver.window_handles)
time.sleep(4)
windows = driver.window_handles
driver.switch_to_window(windows[1])
print(driver.current_window_handle)

general_actions.actions.click_main_navigation_link('validate documents')

xpath_generator.run('button', driver, test_base.client, 'locations', 'button_/data_entry2/index/1')
