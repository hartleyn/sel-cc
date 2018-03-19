import time
import test_base
import general_actions.locations as locations
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException


'''
	Created by Nick Hartley
	3/6/2018
'''


driver = test_base.driver

def hover_settings_link_helper(link_name):
	link = link_name.lower()
	
	if link == 'sysadmin':
		try:
			link_element = driver.find_element_by_partial_link_text('SysAdmin')
		except NoSuchElementException as err:
			click_helper(locations.Links.settings)
			link_element = driver.find_element_by_partial_link_text('SysAdmin')
		
		ActionChains(driver).move_to_element(link_element).perform()
		
	elif link == 'account':
		try:
			link_element = driver.find_element_by_partial_link_text('Account Settings')
		except NoSuchElementException as err:
			click_helper(locations.Links.settings)
			link_element = driver.find_element_by_partial_link_text('Account Settings')
		
		ActionChains(driver).move_to_element(link_element).perform()
		
	
	elif link == 'company':
		try:
			link_element = driver.find_element_by_partial_link_text('Company Settings')
		except NoSuchElementException as err:
			click_helper(locations.Links.settings)
			link_element = driver.find_element_by_partial_link_text('Company Settings')
		
		ActionChains(driver).move_to_element(link_element).perform()
	
	else:
		print('Invalid settings submenu requested.')

def ensure_child_is_visible_before_click_helper(parent_location, child_location):
	if driver.find_element_by_xpath(child_location).is_displayed() == False:
		click_helper(parent_location)
		time.sleep(2)
	click_helper(child_location)
	
def ensure_child_is_visible_before_click_find_by_link_helper(parent_location, link):
	try:
		link_element = driver.find_element_by_link_text(link)
	except NoSuchElementException as err:
		click_helper(parent_location)
		time.sleep(5)
		link_element = driver.find_element_by_link_text(link)
	click_find_by_link_helper(link_element.text)

def ensure_child_is_visible_before_click_find_by_link_document_or_certificate_helper(parent_location):
	options = ('Document Search', 'Certificate Search')
	
	x = 0
	check = True
	while x < len(options) and check:
		try:
			link_element = driver.find_element_by_link_text(options[x])
			check = False
		except NoSuchElementException as err:
			if x == 0:
				click_helper(parent_location)
				time.sleep(5)
		try:
			link_element = driver.find_element_by_link_text(options[x])
			check = False
		except NoSuchElementException as err:
			x += 1
	click_find_by_link_helper(options[x])
	
def click_helper(location):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, location))
		)
		driver.find_element_by_xpath(location).click()	
		time.sleep(3)
		return driver.find_element_by_xpath(location)
	except TimeoutException as err:
		print(err)

def click_find_by_link_helper(link_name):
	time.sleep(2)
	driver.find_element_by_link_text(link_name).click()
	
def select_helper(location, value):
	if driver.find_element_by_xpath(location).is_displayed():
		driver.find_element_by_xpath(location).click()
		time.sleep(2)
		box = Select(driver.find_element_by_xpath(location))
		box.select_by_visible_text(value)
		time.sleep(2)

def close_new_window_helper():
	# Switch to and close pop up window. Then return to original window.
	print(driver.window_handles)
	time.sleep(2)
	windows = driver.window_handles
	if len(windows) > 1:
		driver.switch_to_window(windows[1])
		#print(driver.current_window_handle)
		time.sleep(2)
		driver.close()
		driver.switch_to_window(windows[0])
		time.sleep(2)
		#print(driver.window_handles)
		
def close_old_window_helper():
	# Switch to and close pop up window. Then return to original window.
	print(driver.window_handles)
	time.sleep(2)
	windows = driver.window_handles
	if len(windows) > 1:
		driver.switch_to_window(windows[1])
		#print(driver.current_window_handle)
		time.sleep(2)
		driver.close()
		driver.switch_to_window(windows[0])
		time.sleep(2)
		
		
		
		