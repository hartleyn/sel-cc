import test_base
import xpath_locators
import id_locators
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

driver = test_base.driver

# TODO - Add waits

def go_to_sys_admin_page():
	driver.find_element_by_xpath(xpath_locators.sys_admin_link).click()
	
def go_to_company_settings_page():
	driver.find_element_by_xpath(xpath_locators.company_settings_link).click()
	

def go_to_company_details_page():
	driver.find_element_by_xpath(xpath_locators.company_settings_link).click()
	driver.find_element_by_xpath(xpath_locators.company_details_link).click()	

def go_to_client_settings_page():
	driver.find_element_by_xpath(xpath_locators.client_settings_link).click()
	
def go_to_edit_client_settings_page():
	driver.find_element_by_xpath(xpath_locators.company_settings_link).click()
	time.sleep(2)
	driver.find_element_by_xpath(xpath_locators.company_details_link).click()
	time.sleep(2)
	driver.find_element_by_xpath(xpath_locators.client_settings_link).click()
	time.sleep(2)
	driver.find_element_by_id(id_locators.edit_client_settings_button).click()
	time.sleep(3)
	
def go_to_data_entry_page():
	driver.find_element_by_xpath(xpath_locators.data_entry_link).click()
	time.sleep(3)
	
def go_to_validate_documents_page():
	driver.find_element_by_xpath(xpath_locators.data_entry_link).click()
	time.sleep(2)
	driver.find_element_by_xpath(xpath_locators.validate_documents_link).click()
	time.sleep(3)

def go_to_retail_page():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.retail_link))
		)
		driver.find_element_by_xpath(xpath_locators.retail_link).click()
	except TimeoutException as err:
		print(err)
		
		time.sleep(4)
	
def change_company(company):
	company_picker = driver.find_element_by_id('dropdownCompanyButton')
	company_picker.click()
	time.sleep(3)
	
	input = driver.find_element_by_id('companyInput')
	input.send_keys(company)
	input.send_keys(Keys.RETURN)
	time.sleep(5)
	
def change_client(client):
	client_picker = driver.find_element_by_id('dropdownDivisionButton')
	client_picker.click()
	time.sleep(3)
	
	input = driver.find_element_by_id('divisionInput')
	input.send_keys(client)
	input.send_keys(Keys.RETURN)
	time.sleep(5)
	
def close_new_window():
	# Switch to and close pop up window. The return to original window.
	print(driver.window_handles)
	time.sleep(4)
	windows = driver.window_handles
	driver.switch_to_window(windows[1])
	print(driver.current_window_handle)
	time.sleep(2)
	driver.close()
	driver.switch_to_window(windows[0])
	time.sleep(2)
	print(driver.window_handles)	
	
	
	
	
	