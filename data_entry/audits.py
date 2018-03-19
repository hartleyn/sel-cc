import test_base
import time
import datetime
import data_entry.locations as locations

'''
	Created by Nick Hartley
	12/12/2017
'''

driver = test_base.driver
client = test_base.client


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
	print('Checking result from row:', row_num - 1, '\n')

	actual_cert_id = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[4]').text
	print('Certificate ID:')
	print('	', 'Extracted:', actual_cert_id)
	print('	', 'Expected: ', cert_id, '\n')
	assert actual_cert_id == cert_id
	time.sleep(2)
	actual_cust_num = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[5]').text
	#print('Extracted Customer Number:', actual_cust_num, '     |     Expected:', cust_num)
	print('Customer Number:')
	print('	', 'Extracted:', actual_cust_num)
	print('	', 'Expected: ', cust_num, '\n')
	assert actual_cust_num == cust_num
	time.sleep(2)
	actual_stage = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[6]').text
	#print('Extracted Stage:', actual_stage, '     |     Expected:', stage)
	print('Stage:')
	print('	', 'Extracted:', actual_stage)
	print('	', 'Expected: ', stage, '\n')
	assert actual_stage == stage
	time.sleep(2)
	actual_exposure_zone = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[9]').text
	#print('Extracted Exposure Zone:', actual_exposure_zone, '     |     Expected:', exposure_zone)
	print('Exposure Zone:')
	print('	', 'Extracted:', actual_exposure_zone)
	print('	', 'Expected: ', exposure_zone, '\n')
	assert actual_exposure_zone == exposure_zone
	time.sleep(2)
	actual_source = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[10]').text
	#print('Extracted Source:', actual_source, '     |     Expected:', source)
	print('Source:')
	print('	', 'Extracted:', actual_source)
	print('	', 'Expected: ', source, '\n')
	assert actual_source == source
	time.sleep(2)
	actual_priority = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[11]').text
	#print('Extracted Priority:', actual_priority, '     |     Expected:', priority)
	print('Priority:')
	print('	', 'Extracted:', actual_priority)
	print('	', 'Expected: ', priority, '\n')
	assert actual_priority == priority
	time.sleep(2)
	actual_pages = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[12]').text
	#print('Extracted Pages:', actual_pages, '     |     Expected:', pages)
	print('Pages:')
	print('	', 'Extracted:', actual_pages)
	print('	', 'Expected: ', pages, '\n')
	assert actual_pages == pages
	time.sleep(2)
	actual_age = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[' + str(row_num) + ']/td[13]').text
	#print('Extracted Age:', actual_age, '     |     Expected:', calculate_age(age))
	print('Age (days):')
	print('	', 'Extracted:', actual_age)
	print('	', 'Expected: ', calculate_age(age), '\n')
	assert actual_age == calculate_age(age) or actual_age - calculate_age(age) <= 1 or calculate_age(age) - actual_age >= 1 # Timezones throwing off day count by a day?
	time.sleep(2)
	print('PASS\n\n')
	
	
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
	'''
		Params: 
		filename - the name of the google sheets file.
		sheetname - the name of the particular worksheet with the expected results for the test.
		row_arr - an array of integers representing the search result rows to be checked.
	'''
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
		
		
def verify_basic_search_fields():
	
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_customer_number).is_displayed() #== False # CHANGE
	assert driver.find_element_by_id(locations.IDs.select_exposure_zone).is_displayed()
	assert driver.find_element_by_id(locations.IDs.exempt_reason).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_status).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_id).is_displayed() == False
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_priority).is_displayed() == False
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_source).is_displayed() == False
	assert driver.find_element_by_id(locations.IDs.data_entry_search_field_created_date).is_displayed() == False
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_document_type).is_displayed() == False
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_bucket).is_displayed() == False
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_location).is_displayed() == False

	
def verify_advanced_search_fields():
	if test_base.quick_fails == True:
		assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_customer_number).is_displayed() == False
	else:
		assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_customer_number).is_displayed()
	assert driver.find_element_by_id(locatios.IDs.select_exposure_zone).is_displayed()
	assert driver.find_element_by_id(locations.IDs.exempt_reason).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_status).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_id).is_displayed()	
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_priority).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_source).is_displayed()
	assert driver.find_element_by_id(locations.IDs.data_entry_search_field_created_date).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_document_type).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_bucket).is_displayed()
	assert driver.find_element_by_xpath(locations.Fields.data_entry_search_field_certificate_location).is_displayed()	
	
	
def verify_search_next():
	assert driver.find_element_by_id(id_locators.search_next_page).is_displayed()
	
def verify_search_first():
	assert driver.find_element_by_id(id_locators.search_first_page).is_displayed()

def verify_search_last():
	assert driver.find_element_by_id(id_locators.search_last_page).is_displayed()

def verify_search_prev():
	assert driver.find_element_by_id(id_locators.search_prev_page).is_displayed()