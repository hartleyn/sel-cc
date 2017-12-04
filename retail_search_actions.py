import time
import test_base
import xpath_locators
import id_locators
import os
import glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

'''
	Created by Nick Hartley
	12/01/2017
'''



driver = test_base.driver
client = test_base.client



def compare_results(filename, sheetname):
	sheet = client.open(filename).worksheet(sheetname)
	
	rows = sheet.row_count
	
	print('row count: ' + str(rows))
	
	verify_search_count(rows - 1)
	
	# Start loop in row 2 to avoid header row
	for x in range(2, rows + 1):
		cust_num = str(sheet.cell(x, 1).value)
		name = str(sheet.cell(x, 2).value)
		address = str(sheet.cell(x, 3).value)
		phone = str(sheet.cell(x, 4).value)
		certs = certs_string_formatter(x, sheet)
		
		verify_search_grid(x, cust_num, name, address, phone, certs)


# Verify that a search result row contains expected information
def verify_search_grid(row_num, cust_num, name, address, phone, certs):
	print('Checking result from row:', row_num - 1, '\n')

	actual_cust_num = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[3]').text
	print('Customer Number:')
	print('	', 'Extracted:', actual_cust_num)
	print('	', 'Expected: ', cust_num, '\n')
	assert actual_cust_num.lower() == cust_num.lower()
	time.sleep(2)
	actual_name = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[4]').text
	print('Name:')
	print('	', 'Extracted:', actual_name)
	print('	', 'Expected: ', name, '\n')
	assert actual_name.lower() == name.lower()
	time.sleep(2)
	actual_address = address_formatter(row_num)
	print('Address:')
	print('	', 'Extracted:', actual_address)
	print('	', 'Expected: ', address, '\n')
	assert actual_address.lower() == address.lower()
	time.sleep(2)
	if phone != '-':
		actual_phone = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[6]').text
		print('Phone:')
		print('	', 'Extracted:', phone_number_formatter(actual_phone))
		print('	', 'Expected: ', phone_number_formatter(phone), '\n')
		assert actual_phone == str(phone)
	time.sleep(2)
	actual_certs = get_certs_from_search_result_row(row_num)
	print('Certificates:')
	x = 0
	for cert in actual_certs:
		print('	', 'Extracted:', cert)
		print('	', 'Expected: ', certs[x], '\n')
		assert cert.lower() == certs[x].lower() # Expects extracted and expected results to be in the same order
		x += 1
	time.sleep(2)
	print('PASS\n\n')
	
def retail_search_count():
	count = ''
	
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, xpath_locators.retail_search_result_count))
		)
		count = driver.find_element_by_xpath(xpath_locators.retail_search_result_count).text
		return count
	except TimeoutException as err:
		print(err)

		
def verify_search_count(expected_count):
	actual_count = retail_search_count()
	print('	', 'Extracted:', actual_count)
	print('	', 'Expected: ', expected_count, '\n')
	assert str(expected_count) == str(actual_count)	
	
# Retrieve expected certificates from Google sheet, and format into an array	
def certs_string_formatter(row_num, sheet):
	certs_string = str(sheet.cell(row_num, 5).value)
	arr = certs_string.split(',')
	certs_arr = []

	for cert in arr:
		certs_arr.append(cert.strip())
	
	return certs_arr	

	
# Retrieve all the certs from a search result row
def get_certs_from_search_result_row(row_num):
	if driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[1]').is_displayed():
		x = 1
		certs = []
		
		try:
			while driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[' + str(x) + ']/td[1]').is_displayed() == True:
				certs.append(driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[' + str(x) + ']/td[3]').text)
				x += 1
		except NoSuchElementException:
			return certs

			
# Retrieve and format customer address from a search result row
def address_formatter(row_num):
	addr = driver.find_element_by_xpath('//tr[@id="' + str(row_num - 1) + '"]/td[5]').text
	
	stripped = addr.replace(',', '')

	parsed = stripped.split( )
	
	output = ''
	for x in range(0, len(parsed)):
		output += parsed[x]
		
		if x != len(parsed) - 1:
			output += ' '

	return output


# Phone number format helper
def phone_number_formatter(digits):
	number = str(digits)
	formatted = ''
	for x in range(0, len(number)):
		if x == 0:
			formatted += '('
		elif x == 3:
			formatted += ') '
		elif x == 6:
			formatted += ' - '
			
		formatted += number[x]
		
	return formatted

def open_new_exemption_modal():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_new_exemption_button))
		)
		time.sleep(3)
		driver.find_element_by_id(id_locators.retail_new_exemption_button).click()
	except TimeoutException as err:
		print(err)

def close_search_modal():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_close_button))
		)
		driver.find_element_by_id(id_locators.retail_search_close_button).click()
	except TimeoutException as err:
		print(err)

	
def click_search_button():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_btn))
		)
		driver.find_element_by_id(id_locators.retail_search_btn).click()
	except TimeoutException as err:
		print(err)
	

def click_new_customer_next():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_new_customer_next_button))
		)
		driver.find_element_by_id(id_locators.retail_new_customer_next_button).click()
	except TimeoutException as err:
		print(err)
		
		
def check_for_exemption_modal_close():
	check = driver.find_element_by_id(id_locators.retail_close_exemeption_wizard_modal).is_displayed()
	
	assert check == True
	

def click_search_result_row(row_num):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, str(row_num)))
		)
		driver.find_element_by_id(str(row_num)).click()
	except TimeoutException as err:
		print(err)

		
def click_search_result_certificate(row_num, cert_num):		
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, '//tr[@id="' + str(row_num) + '"]/td[7]/table/tbody/tr[' + str(cert_num) + ']'))
		)
		driver.find_element_by_xpath('//tr[@id="' + str(row_num) + '"]/td[7]/table/tbody/tr[' + str(cert_num) + ']').click()
	except TimeoutException as err:
		print(err)
		
def click_certificate_download_button():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_certificate_download_button))
		)
		driver.find_element_by_id(id_locators.retail_certificate_download_button).click()
		time.sleep(3)
	except TimeoutException as err:
		print(err)
	

def click_customer_edit_button():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_customer_edit_button))
		)
		driver.find_element_by_id(id_locators.retail_customer_edit_button).click()
	except TimeoutException as err:
		print(err)
		
		
def verify_customer_edit_modal():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, xpath_locators.retail_customer_edit_modal))
		)
	except TimeoutException as err:
		print(err)
	finally:
		assert driver.find_element_by_xpath(xpath_locators.retail_customer_edit_modal).is_displayed() == True
	
	
def check_for_newest_pdf_in_download_directory():
	list_of_files = glob.glob(test_base.download_path + test_base.slash + '*.pdf')
	latest_file = max(list_of_files, key=os.path.getctime)

	file_arr = latest_file.split(test_base.slash)
	file = file_arr[len(file_arr)-1]
	
	return file

	
# Checks that a new file is present in the downloads directory
def verify_new_file_download(file):
	new_file = check_for_newest_pdf_in_download_directory()
	
	print('Old file:   ', file)
	print('Newest file:', new_file)
	assert file != new_file
	
	
def retail_search_pick_search_field(field_name, value):
	field = field_name.lower()
	
	if field == 'customer name' or field == 'name':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_cust_name))
			)
			driver.find_element_by_id(id_locators.retail_search_cust_name).click()
			driver.find_element_by_id(id_locators.retail_search_cust_name).send_keys(value)
		except TimeoutException as err:
			print(err)
	elif field == 'phone number' or field == 'phone':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_phone))
			)
			driver.find_element_by_id(id_locators.retail_search_phone).click()
			driver.find_element_by_id(id_locators.retail_search_phone).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'email':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_email))
			)
			driver.find_element_by_id(id_locators.retail_search_email).click()
			driver.find_element_by_id(id_locators.retail_search_email).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'city':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_city))
			)
			driver.find_element_by_id(id_locators.retail_search_city).click()
			driver.find_element_by_id(id_locators.retail_search_city).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'customer state' or field == 'state':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_state))
			)
			driver.find_element_by_id(id_locators.retail_search_state).click()
			time.sleep(2)
			box = Select(driver.find_element_by_id(id_locators.retail_search_state))
			box.select_by_visible_text(value) # TODO - titlecase value
			time.sleep(2)
		except TimeoutException as err:
			print(err)	
	elif field == 'zip code' or field == 'zip':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_zip))
			)
			driver.find_element_by_id(id_locators.retail_search_zip).click()
			driver.find_element_by_id(id_locators.retail_search_zip).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'customer number':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_cust_number))
			)
			driver.find_element_by_id(id_locators.retail_search_cust_number).click()
			driver.find_element_by_id(id_locators.retail_search_cust_number).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'certificate id' or field == 'document id' or field == 'id':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_cert_id))
			)
			driver.find_element_by_id(id_locators.retail_search_cert_id).click()
			driver.find_element_by_id(id_locators.retail_search_cert_id).send_keys(value)
		except TimeoutException as err:
			print(err)	
	elif field == 'document zone' or field == 'exposure' or field == 'exposure zone':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_doc_zone))
			)
			driver.find_element_by_id(id_locators.retail_search_doc_zone).click()
			time.sleep(2)
			box = Select(driver.find_element_by_id(id_locators.retail_search_doc_zone))
			box.select_by_visible_text(value)
			time.sleep(2)
		except TimeoutException as err:
			print(err)
	else:
		print('Invalid search field argument.')
	

def retail_new_customer_and_certificate(field_name, value):
	field = field_name.lower()
	
	if field == 'name of business' or field == 'business' or field == 'business name' or field == 'name':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_new_customer_name))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_name).click()
			driver.find_element_by_id(id_locators.retail_new_customer_name).send_keys(value)
		except TimeoutException as err:
			print(err)
	elif field == 'contact email' or field == 'email':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_new_customer_email))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_email).click()
			driver.find_element_by_id(id_locators.retail_new_customer_email).send_keys(value)
		except TimeoutException as err:
			print(err)
	elif field == 'address':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_new_customer_address))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_address).click()
			driver.find_element_by_id(id_locators.retail_new_customer_address).send_keys(value)
		except TimeoutException as err:
			print(err)
	elif field == 'business city' or field == 'city':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_new_customer_city))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_city).click()
			driver.find_element_by_id(id_locators.retail_new_customer_city).send_keys(value)
		except TimeoutException as err:
			print(err)
	elif field == 'business state' or field == 'state':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_new_customer_state))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_state).click()
			time.sleep(2)
			box = Select(driver.find_element_by_id(id_locators.retail_new_customer_state))
			box.select_by_visible_text(value) # TODO - titlecase value
			time.sleep(2)
		except TimeoutException as err:
			print(err)	
	elif field == 'business zip code' or field == 'zip' or field == 'zip code' or field == 'business zip':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_new_customer_zip))
			)
			driver.find_element_by_id(id_locators.retail_new_customer_zip).click()
			driver.find_element_by_id(id_locators.retail_new_customer_zip).send_keys(value)
		except TimeoutException as err:
			print(err)
	else:
		print('Invalid field name argument')
	
	
	
	
	
	
	
	
	
	
	
	
	
	