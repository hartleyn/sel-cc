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


def change_division(division):
	click_change_division_dropdown()
	
	time.sleep(3)
	driver.find_element_by_xpath(xpath_locators.retail_change_division_input).send_keys(division)
	time.sleep(3)
	driver.find_element_by_xpath(xpath_locators.retail_change_division_input).send_keys(Keys.RETURN)


def retrieve_division_name():
	division = driver.find_element_by_xpath(xpath_locators.retail_division_name_label).text

	return division
	
def verify_change_division(old_division):
	new = retrieve_division_name()
	
	print('Previous Company:', old_division)
	print('Current Company: ', new)
	assert old_division.lower() != new.lower()
	
	
def change_location(location):
	click_change_location_dropdown()
	time.sleep(3)
	driver.find_element_by_xpath(xpath_locators.retail_change_location_input).send_keys(location)
	time.sleep(3)
	driver.find_element_by_xpath(xpath_locators.retail_change_location_input).send_keys(Keys.RETURN)


def retrieve_location_name():
	location = driver.find_element_by_xpath(xpath_locators.retail_location_name_label).text
	
	return location
	

def verify_change_location(old_location):
	new = retrieve_location_name()
	
	print('Previous Location:', old_location)
	print('Current Location: ', new)
	assert old_location.lower() != new.lower()
	

def retail_logout():
	click_change_location_dropdown()
	time.sleep(3)
	
	x = 1
	while driver.find_element_by_xpath('//div[@id="location_chosen_chosen"]/div/ul/li[' + str(x) + ']').text != 'Logout':
		x += 1
	
	driver.find_element_by_xpath('//div[@id="location_chosen_chosen"]/div/ul/li[' + str(x) + ']').click()
	
def verify_retail_logout():
	time.sleep(3)
	url = driver.current_url
	short = url[len(url)-5:len(url)]
	
	assert short == 'login'


def compare_results(filename, sheetname):
	sheet = client.open(filename).worksheet(sheetname)
	
	rows = sheet.row_count
	
	print('row count: ' + str(rows - 1))
	
	verify_search_count(rows - 1)
	
	# Start loop in row 2 to avoid header row
	for x in range(2, rows + 1):
		cust_num = str(sheet.cell(x, 1).value)
		name = str(sheet.cell(x, 2).value)
		address = str(sheet.cell(x, 3).value)
		phone = str(sheet.cell(x, 4).value)
		certs = certs_string_formatter(x, sheet)
		
		# Taking out dashes
		phone_num = phone.replace('-', '')
		
		verify_search_grid(x, cust_num, name, address, phone_num, certs)


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
		assert phone_number_formatter(actual_phone) == phone_number_formatter(phone)
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
		
		'''
			The certificates field of retail search results is displayed as a table within a <td> element. 
			Each certificate is displayed within a <tr> child element of the inner table. 
			This block will loop through the <tr> elements until no more <tr> elements are present, and thus a NoSuchElementException is thrown.
			An array of certificate names is returned upon the exception being thrown.
		'''
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
	
	# Check for dashes, and remove if present
	dashes = False
	for x in range(0, len(number)):
		if number[x] == '-':
			dashes = True
	
	if dashes == True:
		number = number.replace('-', '')

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

	
def open_search_modal():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_open_modal))
		)
		driver.find_element_by_id(id_locators.retail_search_open_modal).click()
	except TimeoutException as err:
		print(err)
	
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
		
		# Pause for 3 seconds after executing search
		time.sleep(3)
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

		
def click_certificate_print_button():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.retail_certificate_print_button))
		)
		driver.find_element_by_xpath(xpath_locators.retail_certificate_print_button).click()
		time.sleep(3)
	except TimeoutException as err:
		print(err)
		

def click_certificate_view_button():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_certificate_view_button))
		)
		driver.find_element_by_id(id_locators.retail_certificate_view_button).click()
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

		
def	click_customer_details_modal_close():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_customer_details_close_modal))
		)
		driver.find_element_by_id(id_locators.retail_customer_details_close_modal).click()
	except TimeoutException as err:
		print(err)
		

def click_change_division_dropdown():
	time.sleep(3)
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.retail_change_division_dropdown))
		)
		driver.find_element_by_xpath(xpath_locators.retail_change_division_dropdown).click()
	except TimeoutException as err:
		print(err)
		
		
def click_change_location_dropdown():
	time.sleep(3)
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.retail_change_location_dropdown))
		)
		driver.find_element_by_xpath(xpath_locators.retail_change_location_dropdown).click()
	except TimeoutException as err:
		print(err)
		

def verify_search_modal_open():
	check = False

	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_search_modal))
		)
		if driver.find_element_by_id(id_locators.retail_search_modal).is_displayed():
			check = True
	except Timeout as err:
		print(err)
	finally:
		assert check == True
		
		
def verify_customer_details_modal_close():
	check = True
	
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.invisibility_of_element_located((By.ID, id_locators.retail_certificate_preview))
		)
		if driver.find_element_by_id(id_locators.retail_certificate_preview).is_displayed():
			check = False
	except TimeoutException as err:
		print(err)
	finally:
		assert check == True	
	
		
def verify_certificate_view_modal():
	check = False
	
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_certificate_preview))
		)
		if driver.find_element_by_id(id_locators.retail_certificate_preview).is_displayed():
			check = True
	except TimeoutException as err:
		print(err)
	finally:
		assert check == True
		
def verify_customer_edit_modal():
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, xpath_locators.retail_customer_edit_modal))
		)
	except TimeoutException as err:
		print(err)
	finally:
		assert driver.find_element_by_xpath(xpath_locators.retail_customer_edit_modal).is_displayed() == True
	

def verify_certificate_print_window(windows):
	time.sleep(3)
	new_windows = driver.window_handles
	print('Previous Windows:', windows)
	print('Current Windows: ', new_windows)
	assert len(windows) == 1
	assert len(windows) != len(new_windows)

	
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
	
	
def verify_click_customer(customer_name):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.retail_customer_modal_header))
		)
		name = driver.find_element_by_id(id_locators.retail_customer_modal_header).text
		
		# Stripping the 'Customer Information: ' portion of the modal header
		name = name[22:len(name)]
	except TimeoutException as err:
		print(err)
	finally:
		print('Displaying modal for customer:', name)
		assert customer_name.lower() == name.lower()
	
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


# Retail search result sort function
def retail_search_sort_results(field_name):
	field = field_name.lower()
	if field[0:9] == 'customer ':
		field = field[9:len(field)]
		
	if field == 'number':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_results_sort_customer_number))
			)
			driver.find_element_by_id(id_locators.retail_search_results_sort_customer_number).click()
		except TimeoutException as err:
			print(err)
	elif field == 'name':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_results_sort_name))
			)
			driver.find_element_by_id(id_locators.retail_search_results_sort_name).click()
		except TimeoutException as err:
			print(err)
	elif field == 'address':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_results_sort_address))
			)
			driver.find_element_by_id(id_locators.retail_search_results_sort_address).click()
		except TimeoutException as err:
			print(err)
	elif field == 'phone' or field == 'phone number':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_results_sort_phone))
			)
			driver.find_element_by_id(id_locators.retail_search_results_sort_phone).click()
		except TimeoutException as err:
			print(err)
	elif field == 'certificates' or field == 'certs':
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.element_to_be_clickable((By.ID, id_locators.retail_search_results_sort_certificates))
			)
			driver.find_element_by_id(id_locators.retail_search_results_sort_certificates).click()
		except TimeoutException as err:
			print(err)
	else:
		print('Invalid sort field argument:', field)
	
		
		
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	