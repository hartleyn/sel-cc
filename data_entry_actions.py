import time
import unittest
import gspread
import datetime
import test_base
import xpath_locators
import id_locators
import data_entry_actions_data
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

'''
	Created by Nick Hartley
	11/22/2017
'''

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\nick.hartley\\Desktop\\Auto\\client_secret.json', scope)
client = gspread.authorize(creds)

driver = test_base.driver
	
def data_entry_search_count():
	time.sleep(3)
	count = 0
	
	if driver.find_element_by_xpath('//td[@id="DataEntrySearch_toppager_right"]/div').is_displayed():
		results = driver.find_element_by_xpath('//td[@id="DataEntrySearch_toppager_right"]/div').text
		
		if results == 'No records to view':
			return count
		else:
			get_count = results.split(' ')
			count = get_count[len(get_count) - 1]
			return int(count)
	
def verify_search_count(expected_count):
	actual_count = data_entry_search_count()
	assert expected_count == actual_count
	
def verify_search_grid(row_num, cert_id, cust_num, stage, exposure_zone, source, priority, pages, age):
	actual_cert_id = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[4]').text
	print('Extracted Certificate ID:', actual_cert_id, '     |     Expected:', cert_id)
	assert actual_cert_id == cert_id
	time.sleep(2)
	actual_cust_num = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[5]').text
	print('Extracted Customer Number:', actual_cust_num, '     |     Expected:', cust_num)
	assert actual_cust_num == cust_num
	time.sleep(2)
	actual_stage = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[6]').text
	print('Extracted Stage:', actual_stage, '     |     Expected:', stage)
	assert actual_stage == stage
	time.sleep(2)
	actual_exposure_zone = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[9]').text
	print('Extracted Exposure Zone:', actual_exposure_zone, '     |     Expected:', exposure_zone)
	assert actual_exposure_zone == exposure_zone
	time.sleep(2)
	actual_source = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[10]').text
	print('Extracted Source:', actual_source, '     |     Expected:', source)
	assert actual_source == source
	time.sleep(2)
	actual_priority = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[11]').text
	print('Extracted Priority:', actual_priority, '     |     Expected:', priority)
	assert actual_priority == priority
	time.sleep(2)
	actual_pages = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[12]').text
	print('Extracted Pages:', actual_pages, '     |     Expected:', pages)
	assert actual_pages == pages
	time.sleep(2)
	actual_age = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[13]').text
	print('Extracted Age:', actual_age, '     |     Expected:', calculate_age(age))
	assert actual_age == calculate_age(age)
	time.sleep(2)
	
	
def calculate_age(date):
	today = datetime.date.today()
	
	try:
		parsed_date = date.split('-')
		final_date = datetime.date(int(parsed_date[0]), int(parsed_date[1]), int(parsed_date[2]))
		time = today - final_date
		days = time.days
		age = str(days)
		
		return age
	except TypeError as err:
		print('Handling run-time error:', err)

def compare_results(filename, sheetname):
	sheet = client.open(filename).worksheet(sheetname)
	
	rows = sheet.row_count
	cols = sheet.col_count
	
	print('row count: ' + str(rows))
	print('col count: ' + str(cols))
	
	verify_search_count(rows - 1)
	
	# Start loop in row 2 to avoid header row
	for x in range(2, rows + 1):
		cert_id = str(sheet.cell(x, 1).value)
		cust_num = str(sheet.cell(x, 2).value)
		stage = str(sheet.cell(x, 3).value)
		exposure_zone = str(sheet.cell(x, 4).value)
		source = str(sheet.cell(x, 5).value)
		priority = str(sheet.cell(x, 6).value)
		pages = str(sheet.cell(x, 7).value)
		age	= str(sheet.cell(x, 8).value)
		
		verify_search_grid(x, cert_id, cust_num, stage, exposure_zone, source, priority, pages, age)
		
def compare_results_with_row_numbers(filename, sheetname, rows_arr):
	sheet = client.open(filename).worksheet(sheetname)
	
	rows = sheet.row_count
	cols = sheet.col_count
	
	print('row count: ' + str(rows))
	print('col count: ' + str(cols))
	
	# Start loop in row 2 to avoid header row
	for x in range(2, len(rows_arr) + 2):
		cert_id = str(sheet.cell(x, 1).value)
		cust_num = str(sheet.cell(x, 2).value)
		stage = str(sheet.cell(x, 3).value)
		exposure_zone = str(sheet.cell(x, 4).value)
		source = str(sheet.cell(x, 5).value)
		priority = str(sheet.cell(x, 6).value)
		pages = str(sheet.cell(x, 7).value)
		age	= str(sheet.cell(x, 8).value)
		
		# Increment each row number to avoid accessing the row DOM in verify_search_grid
		row = rows_arr[x-2] + 1
		
		verify_search_grid(row, cert_id, cust_num, stage, exposure_zone, source, priority, pages, age)
		
def ready_for_validation_date_formatter(filename, sheetname, row_num):
	sheet = client.open(filename).worksheet(sheetname)
	today = datetime.date.today()
	
	try:
		# Get date from the 8th column ['escalation_date'] of sheet
		sheet_date = sheet.cell(row_num, 8).value
		
		stage = 'Ready For Validation (Escalated ' + calculate_age(sheet_date) + ' days ago)'
		
		return stage
	except TypeError as err:
		print('Handling run-time error:', err)
	
		
def ready_for_validation_compare_results(filename, sheetname):
	sheet = client.open(filename).worksheet(sheetname)
	
	rows = sheet.row_count
	cols = sheet.col_count
	
	print('row count: ' + str(rows))
	print('col count: ' + str(cols))
	
	verify_search_count(rows - 1)
	
	# Start loop in row 2 to avoid header row
	for x in range(2, rows + 1):
		cert_id = str(sheet.cell(x, 1).value)
		cust_num = str(sheet.cell(x, 2).value)
		exposure_zone = str(sheet.cell(x, 3).value)
		source = str(sheet.cell(x, 4).value)
		priority = str(sheet.cell(x, 5).value)
		pages = str(sheet.cell(x, 6).value)
		age	= str(sheet.cell(x, 7).value)
		
		stage = ready_for_validation_date_formatter(filename, sheetname, x)
		
		verify_search_grid(x, cert_id, cust_num, stage, exposure_zone, source, priority, pages, age)

		
# HELPER FUNCTIONS

def go_to_upload():
	driver.find_element_by_id(id_locators.data_entry_upload_button).click()
	time.sleep(2)

def click_search_button():
	driver.find_element_by_id(id_locators.data_entry_search_button).click()
	time.sleep(2)
	
def select_field_xpath(locator, selection):
	driver.find_element_by_xpath(locator).click()
	time.sleep(2)
	box = Select(driver.find_element_by_xpath(locator))
	box.select_by_visible_text(selection)

# Clicks an stack action in document validation
def validate_documents_action_click(action):
	act = action.lower()
	
	driver.find_element_by_id(id_locators.stack_actions_in_search_page).click()
	
	if act == 'claim documents':
		driver.find_element_by_xpath(xpath_locators.select_claim_documents_stack_action).click()
	elif act == 'release documents':
		driver.find_element_by_xpath(xpath_locators.select_release_documents_stack_action).click()
	elif act == 'download document':
		driver.find_element_by_xpath(xpath_locators.select_download_document_stack_action).click()
	else:
		print('Invalid stack filter entered.')
		
def perform_stack_filter(filter):
	driver.find_element_by_id(id_locators.select_stack_filter).click()
	time.sleep(1)
	box = Select(driver.find_element_by_xpath(xpath_locators.select_stack_filter))
	box.select_by_visible_text(filter)
	
def select_certs_under_data_entry_search(number_of_certs):
	id_list = []
	
	if data_entry_search_count() >= number_of_certs:
		for i in range(0, number_of_certs):
			driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(i+2) + ']/td[1]/input').click()
			time.sleep(2)
			id_list.append(driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(i+2) + ']/td[4]').text)		
	
	return id_list
	
def verify_certs_under_stack_filter(list):
	for n in range(0, len(list)):
		print('Certificate ID Selected = ' + list[n])
		driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).send_keys(list[n])
		time.sleep(2)
		click_search_button()
		time.sleep(2)
		x = str(list[n])
		assert driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[4]').text.lower() == x.lower()
		print('Certificate is present.')

def verify_certs_not_listed_under_stack_filter(list):
	for n in range(0, len(list)):
		print('Certificate ID Selected = ' + list[n])
		driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).send_keys(list[n])
		time.sleep(2)
		click_search_button()
		time.sleep(2)
		x = str(list[n])
		assert driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[4]').text.lower() != x.lower()
		print('Certificate is removed.')
		
def verify_documents_claim_documents_0001(number_of_documents):
	cert_id_list = select_certs_under_data_entry_search(number_of_documents)
	
	if cert_id_list[0] is not None:
		driver.find_element_by_id(id_locators.stack_actions_in_search_page).click()
		time.sleep(2)
		validate_documents_action_click('Claim documents')
		time.sleep(2)
		perform_stack_filter('My Unfinished Documents')
		time.sleep(2)
		verify_certs_under_stack_filter(cert_id_list) 
	else:
		print('Not enough certs to claim.')

def verify_documents_release_documents_0001(number_of_documents):
	perform_stack_filter('My Unfinished Documents')
	
	cert_id_list = select_certs_under_data_entry_search(number_of_documents)
	
	if cert_id_list[0] is not None:
		driver.find_element_by_id(id_locators.stack_actions_in_search_page).click()
		time.sleep(2)
		validate_documents_action_click('Release documents')
		time.sleep(2)
		perform_stack_filter('Available Documents')
		time.sleep(2)
		verify_certs_under_stack_filter(cert_id_list) 
	else:
		print('Not enough certs to claim.')

def release_doc():
	driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[1]/input').click()
	time.sleep(2)
	validate_documents_action_click('release documents')
	
def release_doc():
	driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[1]/input').click()
	time.sleep(2)
	validate_documents_action_click('claim documents')

def documents_my_unfinished_documents_0001():
	perform_stack_filter('My Unfinished Documents')

# Possible?
def verify_documents_delete_documents_0001(number_of_documents):
	list = select_certs_under_data_entry_search(number_of_documents)
	validate_documents_action_click('delete document(s)')
	verify_certs_not_listed_under_stack_filter(list)
	
def documents_documents_claimed_by_others_0001():
	perform_stack_filter('Documents Claimed By Others')
	
def search_doc_type_0001():
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed():
		driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).click()
		time.sleep(2)
		driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(data_entry_actions_data.search_by_document_type)
		time.sleep(2)
		driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).send_keys(Keys.RETURN)
		time.sleep(2)
		click_search_button()

def search_pick_search_field(field_name, value):
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
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket).click()
			time.sleep(2)
			box = Select(driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket))
			box.select_by_visible_text(value)
			time.sleep(2)
	elif field == 'location':
		if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location).is_displayed():
			driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location).click()
			time.sleep(2)
			box = Select(driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location))
			box.select_by_visible_text(value)
			time.sleep(2)
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
	
def sort_search_results(field_name):
	field = field_name.lower()
	
	if field == 'filename' or field == 'certificate id':
		if driver.find_element_by_id(id_locators.data_entry_certificate_id_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_certificate_id_table_header_link).click()
	elif field == 'customer number':
		if driver.find_element_by_id(id_locators.data_entry_customer_number_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_customer_number_table_header_link).click()
	elif field == 'exposure zone':
		if driver.find_element_by_id(id_locators.data_entry_exposure_zone_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_exposure_zone_table_header_link).click()
	elif field == 'pages':
		if driver.find_element_by_id(id_locators.data_entry_pages_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_pages_table_header_link).click()
	elif field == 'stage':
		if driver.find_element_by_id(id_locators.data_entry_stage_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_stage_table_header_link).click()
	elif field == 'priority':
		if driver.find_element_by_id(id_locators.data_entry_priority_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_priority_table_header_link).click()
	elif field == 'source':
		if driver.find_element_by_id(id_locators.data_entry_source_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_source_table_header_link).click()
	elif field == 'account':
		if driver.find_element_by_id(id_locators.data_entry_account_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_account_table_header_link).click()
	elif field == 'age':
		if driver.find_element_by_id(id_locators.data_entry_age_table_header_link).is_displayed():
			driver.find_element_by_id(id_locators.data_entry_age_table_header_link).click()
	else:
		print('Invalid field name entered.')

'''
def verify_basic_search_fields():
	good = True

	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_customer_number).is_displayed() != True
		good = False
		return good
	if driver.find_element_by_id(id_locators.select_exposure_zone).is_displayed() != True:
		good = False
		return good
	if driver.find_element_by_id(id_locators.exempt_reason).is_displayed() != True:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status).is_displayed() != True:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_id(id_locators.data_entry_search_field_created_date).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket).is_displayed() != False:
		good = False
		return good
	if driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location).is_displayed() != False:
		good = False
		return good

	return good
'''
def verify_basic_search_fields():

	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_customer_number).is_displayed()
	assert driver.find_element_by_id(id_locators.select_exposure_zone).is_displayed()
	assert driver.find_element_by_id(id_locators.exempt_reason).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).is_displayed() == False
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority).is_displayed() == False
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source).is_displayed() == False
	assert driver.find_element_by_id(id_locators.data_entry_search_field_created_date).is_displayed() == False
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed() == False
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket).is_displayed() == False
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location).is_displayed() == False

	
def verify_advanced_search_fields():
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_customer_number).is_displayed()
	assert driver.find_element_by_id(id_locators.select_exposure_zone).is_displayed()
	assert driver.find_element_by_id(id_locators.exempt_reason).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_status).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_id).is_displayed()	
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_priority).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_source).is_displayed()
	assert driver.find_element_by_id(id_locators.data_entry_search_field_created_date).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_document_type).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_bucket).is_displayed()
	assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_certificate_location).is_displayed()	

def search_go_to_next():
	time.sleep(2)
	driver.find_element_by_id(id_locators.search_next_page).click()
	time.sleep(3)

def search_go_to_first():
	time.sleep(2)
	driver.find_element_by_id(id_locators.search_first_page).click()
	time.sleep(3)
	
def search_go_to_last():
	time.sleep(2)
	driver.find_element_by_id(id_locators.search_last_page).click()
	time.sleep(3)
	
def search_go_to_prev():
	time.sleep(2)
	driver.find_element_by_id(id_locators.search_prev_page).click()
	time.sleep(3)
	
def verify_search_next():
	assert driver.find_element_by_id(id_locators.search_next_page).is_displayed()
	
def verify_search_first():
	assert driver.find_element_by_id(id_locators.search_first_page).is_displayed()

def verify_search_last():
	assert driver.find_element_by_id(id_locators.search_last_page).is_displayed()

def verify_search_prev():
	assert driver.find_element_by_id(id_locators.search_prev_page).is_displayed()

def search_type_toggle(type_name):
	time.sleep(3)
	type = type_name.lower()
	label = driver.find_element_by_xpath(xpath_locators.data_entry_basic_advanced_search_selection_label).text.lower()
	
	if type != label:
		driver.find_element_by_xpath(xpath_locators.data_entry_basic_advanced_search_selection).click()
	
	
	
	
	
	
	
	
	
	
	
	
	