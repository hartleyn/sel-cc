import test_base
import xpath_locators
import id_locators
import time
from selenium.webdriver.common.keys import Keys

driver = test_base.driver

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