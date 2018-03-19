import test_base
import xpath_locators
import id_locators
import time
import general_actions.locations
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

driver = test_base.driver

def click_main_navigation_link(link_name):
	link = link_name.lower()
	
	if link == 'profile':
		click_link(locations.Links.profile)
	elif link == 'my profile':
		ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.my_profile)
	elif link == 'message center':
		ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.message_center)
	elif link == 'download center':
		ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.download_center)
	elif link == 'logout':
		ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.logout)
	elif link == 'dashboard':
		click_link(locations.Links.dashboard)
	elif link == 'search':
		click_link(locations.Links.search)
	elif link == 'customer search':
		ensure_child_is_visible_before_click(locations.Links.search, locations.Links.customer_search)
	elif link == 'document search':
		ensure_child_is_visible_before_click(locations.Links.search, locations.Links.customer_search)
	elif link == 'saved searches':
		ensure_child_is_visible_before_click(locations.Links.search, locations.Links.customer_search)
	elif link == 'reports':
		click_link(locations.Links.reports)
	elif link == 'document reports':
		ensure_child_is_visible_before_click(locations.Links.reports, locations.Links.document_reports)
	elif link == 'customer reports':
		ensure_child_is_visible_before_click(locations.Links.reports, locations.Links.customer_reports)
	elif link == 'logistic reports':
		ensure_child_is_visible_before_click(locations.Links.logistics_reports, locations.Links.logistics_reports)
	elif link == 'user reports':
		ensure_child_is_visible_before_click(locations.Links.reports, locations.Links.user_reports)	
	elif link == 'data entry':
		click_link(locations.Links.data_entry)
	elif link == 'validate documents':
		ensure_child_is_visible_before_click(locations.Links.data_entry, locations.Links.validate_documents)
	elif link == 'all companies':
		ensure_child_is_visible_before_click(locations.Links.data_entry, locations.Links.all_companies)
	elif link == 'requests':
		click_link(locations.Links.requests)
	elif link == 'send request':
		ensure_child_is_visible_before_click(locations.Links.requests, locations.Links.send_requests)
	elif link == 'email templates/cover letters':
		ensure_child_is_visible_before_click(locations.Links.requests, locations.Links.email_templates_cover_letters)
	elif link == 'customers':
		click_link(locations.Links.customers)
	elif link == 'add customer':
		ensure_child_is_visible_before_click(locations.Links.customers, locations.Links.add_customer)
	elif link == 'bulk import':
		ensure_child_is_visible_before_click(locations.Links.customers, locations.Links.bulk_import)
	elif link == 'bulk delete':
		ensure_child_is_visible_before_click(locations.Links.customers, locations.Links.bulk_delete)
	elif link == 'same-as editor':
		ensure_child_is_visible_before_click(locations.Links.customers, locations.Links.same_as_editor)
	elif link == 'company content':
		click_link(locations.Links.company_content)
	elif link == 'document library':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.document_library)
	elif link == 'nexus settings':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.nexus_settings)
	elif link == 'exemption matrix':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.exemption_matrix)	
	elif link == 'company settings':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.company_settings)
	elif link == 'company details':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.company_details)
	elif link == 'company same-as':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.company_same_as)
	elif link == 'custom fields':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.custom_fields)
	elif link == 'assign users':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.assign_users)
	elif link == 'data entry sets':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.data_entry_sets)	
	elif link == 'locations':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.locations)
	elif link == 'buckets':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.buckets)
	elif link == 'public wizard':
		ensure_child_is_visible_before_click(locations.Links.company_content, locations.Links.public_wizard)
	elif link == 'account settings':
		click_link(locations.Links.account_settings)
	elif link == 'account details':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.account_details)
	elif link == 'exposure zones':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.exposure_zones)
	elif link == 'exposure zones attributes':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.exposure_zone_attributes)
	elif link == 'invalid reasons':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.invalid_reasons)
	elif link == 'document categories':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.document_categories)
	elif link == 'document attributes':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.document_attributes)
	elif link == 'customer attributes':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.customer_attributes)
	elif link == 'manage users':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.manage_users)
	elif link == 'user roles':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.user_roles)
	elif link == 'notification subscriptions':
		ensure_child_is_visible_before_click(locations.Links.account_settings, locations.Links.notification_subscriptions)
	elif link == 'retail':
		click_link(locations.Links.retail)
	else:
		print('Invalid link requested.')

def ensure_child_is_visible_before_click(parent_location, child_location):
	if driver.find_element_by_xpath(child_location).is_displayed() == False:
		click_link(parent_location)
	click_link(child_location)
	
def click_link(location):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, location))
		)
		driver.find_element_by_xpath(location).click()
	except TimeoutException as err:
		print(err)
	
# TODO - Add waits

'''
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
'''

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

	
	
	
	