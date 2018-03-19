import test_base
import data_entry.locations as locations
import time
import general_actions.actions
import xpath_locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

'''
	Created by Nick Hartley
	12/12/2017
'''


driver = test_base.driver
client = test_base.client

def click(button_name):
	button = button_name.lower()
	print('Attempting to click ' + button_name + '...\n')
	
	if button[0:14] == 'claim document':
		ensure_child_is_visible_before_click(locations.Buttons.action, locations.Links.claim_documents)
		general_actions.actions.close_new_window()
	elif button[0:16] == 'release document':
		ensure_child_is_visible_before_click(locations.Buttons.action, locations.Links.claim_documents)
	elif button == 'download document':
		ensure_child_is_visible_before_click(locations.Buttons.action, locations.Links.claim_documents)
	elif button == 'page selector':
		xpath_click_helper(locations.Links.page_selector)
	elif button == 'upload document':
		xpath_click_helper(locations.Buttons.upload_document)
	elif button == 'search':
		xpath_click_helper(locations.Buttons.search)
	elif button == 'clear':
		xpath_click_helper(locations.Buttons.clear)
	elif button == 'action':
		xpath_click_helper(locations.Buttons.action)
	elif button == 'upload stack modal close':
		xpath_click_helper(locations.Buttons.upload_stack_modal_close)
	elif button == 'upload stack':
		xpath_click_helper(locations.Buttons.upload_stack)
	else:
		print('Invalid action requested')
		

def ensure_child_is_visible_before_click(parent_location, child_location):
	if driver.find_element_by_xpath(child_location).is_displayed() == False:
		xpath_click_helper(parent_location)
		time.sleep(2)
	xpath_click_helper(child_location)
	
def xpath_click_helper(location):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, location))
		)
		driver.find_element_by_xpath(location).click()
		time.sleep(3)
	except TimeoutException as err:
		print(err)		
		

def search(field_name, value): # TODO
	field = field_name.lower()
	
	if field == 'filename':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_filename).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_filename).send_keys(value)
			time.sleep(2)
	elif field == 'customer number':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_customer_number).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_customer_number).send_keys(value)
			time.sleep(2)
	elif field == 'exposure zone':
		if driver.find_element_by_id(id_locators.select_exposure_zone).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).click()
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).send_keys(value)
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).send_keys(Keys.RETURN)
			time.sleep(2)
	elif field == 'document category':
		if driver.find_element_by_id(id_locators.exempt_reason).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exempt_reasons_div_tag).click()
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exempt_reasons_input_tag).send_keys(value)
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exempt_reasons_list_tag).click()
			time.sleep(2)
	elif field == 'stage':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status).click()
			time.sleep(2)
			box = Select(driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status))
			box.select_by_visible_text(value)
			time.sleep(2)
	elif field == 'certificate id':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).send_keys(value)
			time.sleep(2)
	elif field == 'priority':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority).click()
			time.sleep(2)
			box = Select(driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority))
			box.select_by_visible_text(value)
			time.sleep(2)
	elif field == 'source':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source).click()
			time.sleep(2)
			box = Select(driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source))
			box.select_by_visible_text(value)
			time.sleep(2)
	elif field == 'created date':
		if driver.find_element_by_id(id_locators.data_entry_search_field_created_date).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_search_field_created_date).click()
			time.sleep(2)
			driver.find_element_by_id(id_locators.data_entry_search_field_created_date).send_keys(value)
			time.sleep(2)
			driver.find_element_by_id(id_locators.data_entry_search_field_created_date).send_keys(Keys.RETURN)
			time.sleep(2)
	elif field == 'document type':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).click()
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(value)
			time.sleep(2)
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(Keys.RETURN)
			time.sleep(2)
	elif field == 'bucket':
		select_helper(xpath_locators.data_entry_search_field_certificate_location, value)
	elif field == 'location':
		select_helper(xpath_locators.data_entry_search_field_certificate_location, value)
	elif field == 'document type list':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed():
			for type in value:
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).click()
				time.sleep(2)
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(type)
				time.sleep(2)
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(Keys.RETURN)
				time.sleep(2)
	elif field == 'exposure zone list':
		if driver.find_element_by_id(id_locators.select_exposure_zone).is_displayed():
			for zone in value:
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).click()
				time.sleep(2)
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).send_keys(zone)
				time.sleep(2)
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exposure_zone).send_keys(Keys.RETURN)
				time.sleep(2)
	elif field == 'document category list':
		if driver.find_element_by_id(id_locators.exempt_reason).is_displayed():
			count = 1
			for cat in value:
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exempt_reasons_div_tag).click()
				time.sleep(2)
				driver.find_element_by_xpath('//div[@id="exempt_reason_chosen"]/ul[1]/li[' + str(count) + ']/input[1]').send_keys(cat)
				time.sleep(2)
				driver.find_element_by_xpath(xpath_locators.data_entry_search_field_exempt_reasons_list_tag).click()
				time.sleep(2)
				count += 1
	else:
		print('Invalid field name entered.')


def select_helper(location, value):
	if driver.find_element_by_xpath(location).is_displayed():
		driver.find_element_by_xpath(location).click()
		time.sleep(2)
		box = Select(driver.find_element_by_xpath(location))
		box.select_by_visible_text(value)
		time.sleep(2)
		
def id_select_helper(location, value):
	if driver.find_element_by_id(location).is_displayed():
		driver.find_element_by_id(location).click()
		time.sleep(2)
		box = Select(driver.find_element_by_id(location))
		box.select_by_visible_text(value)
		time.sleep(2)

		
# Jump to the desired stack filter page
def filter_documents(filter):
	act = filter.lower()

	if act == 'available documents' or act == 'my unfinished documents' or act == 'documents claimed by others':
		id_select_helper(locations.IDs.select_stack_filter, filter)
	else:
		print('Invalid stack filter requested.')

	
def select_single_document_in_row(row_num):
	row_num += 1
	time.sleep(2)
	driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[1]/input').click()
	time.sleep(2)
		#if act == 'claim documents':
		#	general_actions.close_new_window()

		
def select_multiple_documents_in_rows(row_arr):
	if row_arr == 'all':
		driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[1]/td[1]/input').click()
		time.sleep(2)
	else:
		for number in row_arr:
			number += 1
			driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(number) + ']/td[1]/input').click()
			time.sleep(1)
		time.sleep(2)


def sort_search_results(field_name):
	time.sleep(5)
	field = field_name.lower()

	if field == 'filename' or field == 'certificate id':
		id_click_helper(locations.IDs.data_entry_certificate_id_table_header_link)
	elif field == 'customer number':
		id_click_helper(locations.IDs.data_entry_customer_number_table_header_link)
	elif field == 'exposure zone':
		id_click_helper(locations.IDs.data_entry_status_table_header_link)
	elif field == 'pages':
		id_click_helper(locations.IDs.data_entry_pages_table_header_link)
	elif field == 'stage':
		id_click_helper(locations.IDs.data_entry_stage_table_header_link)
	elif field == 'priority':
		id_click_helper(locations.IDs.data_entry_priority_table_header_link)
	elif field == 'source':
		id_click_helper(locations.IDs.data_entry_source_table_header_link)
	elif field == 'account':
		id_click_helper(locations.IDs.data_entry_account_table_header_link)
	elif field == 'age':
		id_click_helper(locations.IDs.data_entry_age_table_header_link)
	else:
		print('Invalid field name entered.')
	

def search_results_navigate_to_page(selection):
	if type(selection) == type('n'):
		selection = selection.lower()
	
		if selection == 'first':
			id_click_helper(locations.IDs.search_first_page)
		if selection[0:4] == 'prev':
			id_click_helper(locations.IDs.search_prev_page)	
		if selection == 'next':
			id_click_helper(locations.IDs.search_next_page)
		if selection == 'last':
			id_click_helper(locations.IDs.search_last_page)
	elif type(selection) == type(1):
		xpath_click_helper(page_selector)
		
		driver.find_element_by_xpath('//td[@id="DataEntrySearch_toppager_center"]/table/tbody/tr/td[4]/div/ul/li/a[' + str(selection) + ']').click()
	else:
		print('Invalid search results navigation request.')
		
def id_click_helper(location):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, location))
		)
		driver.find_element_by_id(location).click()
		time.sleep(3)
	except TimeoutException as err:
		print(err)

def search_type_toggle(type_name):
	time.sleep(3)
	type = type_name.lower()
	label = driver.find_element_by_xpath(locations.Buttons.search_type_label).text.lower()
	
	if type != label:
		xpath_click_helper(locations.Buttons.search_type_selection)		
		
		