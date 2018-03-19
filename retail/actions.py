import test_base
import retail.locations as locations
import time
import general_actions.actions
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


def click(location_name):
	location = location_name.lower()
	
	if driver.find_element_by_id(locations.Modals.exemption_search_modal).is_displayed():
		if location == 'close':
			xpath_click_helper(locations.Buttons.exemption_search_modal_close)
		elif location == 'search':
			xpath_click_helper(locations.Buttons.exemption_search_modal_search)
		elif location[0:5] == 'clear':
			xpath_click_helper(locations.Buttons.exemption_search_modal_clear_screen)
		else:
			print('Invalid action requested.')
	elif driver.find_element_by_id(locations.Modals.new_customer_and_document_modal).is_displayed():
		if location == 'next':
			xpath_click_helper(locations.Buttons.new_customer_and_document_modal_next)
		elif location == 'cancel':
			xpath_click_helper(locations.Buttons.new_customer_and_document_modal_cancel)
		else:
			print('Invalid action requested.')
	else:
		if location == 'search':
			xpath_click_helper(locations.Buttons.retail_search)
		elif location == 'new exemption':
			xpath_click_helper(locations.Buttons.retail_new_exemption)
		else:
			print('Invalid action requested.')
		
		
def search(field_name, value):
	field = field_name.lower()
	
	if driver.find_element_by_id(exemption_search_modal).is_displayed():
		if field == 'customer name' or field == 'name':
			search_helper(locations.Fields.customer_name, value)
		elif field[0:5] == 'phone':
			search_helper(locations.Fields.phone_number, value)
		elif field == 'email':
			search_helper(locations.Fields.email, value)
		elif field == 'city':
			search_helper(locations.Fields.city, value)
		elif field == 'customer state' or field == 'state':
			id_select_helper(locations.Fields.customer_state, value)
		elif field[0:3] == 'zip':
			search_helper(locations.Fields.zip_code, value)
		elif field == 'customer number' or field == 'number':
			search_helper(locations.Fields.customer_number, value)
		elif field == 'document id' or field == 'id':
			search_helper(locations.Fields.document_id, value)
		elif field == 'document zone' or field == 'zone':
			id_select_helper(locations.Fields.document_zone, value)
		else:
			print('Invalid exemption search field requested.)
	elif driver.find_element_by_id(locations.Modals.new_customer_and_document_modal).is_displayed():
		if field == 'name of business' or field == 'business name':
			search_helper(locations.Fields.name_of_business, value)
		elif field == 'contact email' or field == 'email':
			search_helper(locations.Fields.contact_email, value)
		elif field == 'main business phone number' or field[0:5] == 'phone':
			search_helper(locations.Fields.main_business_phone_number), value)
		elif field == 'address line 1' or field == 'address 1' or field == 'address' :
			search_helper(locations.Fields.address_line_1, value)
		elif field == 'address line 2' or field == 'address 2':
			search_helper(locations.Fields.address_line_2, value)
		elif field == 'business city' or field == 'city':
			search_helper(locations.Fields.business_city, value)
		elif field == 'business country' or field 'country':
			id_select_helper(locations.Fields.business_country, value)
		elif field == 'business state' or field == 'state':
			id_select_helper(locations.Fields.business_state, value)
		elif field == 'business zip code' or field[0:3] == 'zip':
			search_helper(locations.Fields.business_zip_code, value)
		elif field == 'contact name':
			search_helper(locations.Fields.contact_name, value)
		elif field == 'is this form being completed for a corporation' or field == 'completed for a corporation' or field == 'corporation question':
			id_select_helper(locations.Fields.completed_for_a_corporation, value)
		elif field[0:9] == 'tax class':
			id_select_helper(locations.Fields.tax_classification, value)
	else:
		print('No search modals displayed.')
		

def sort_search_results(field_name):
	time.sleep(5)
	field = field_name.lower()

	if field == 'customer number':
		id_click_helper(locations.Headers.customer_number)
	elif field == 'name':
		id_click_helper(locations.Headers.name)
	elif field == 'address':
		id_click_helper(locations.Headers.address)
	elif field[0:5] == 'phone':
		id_click_helper(locations.Headers.phone)
	elif field == 'certificates' or field == 'certs':
		id_click_helper(locations.Headers.certificates)
	else:
		print('Invalid field name entered.')		

		
def xpath_click_helper(location):
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.XPATH, location))
		)
		driver.find_element_by_xpath(location).click()
		time.sleep(3)
	except TimeoutException as err:
		print(err)	
	
		
			
def search_helper(location, value):
	field = driver.find_element_by_id(location)
	field.click()
	time.sleep(2)
	field.send_keys(value)
	time.sleep(2)
	field.send_keys(Keys.RETURN)
	time.sleep(2)
	
def id_select_helper(location, value):
	if driver.find_element_by_id(location).is_displayed():
		driver.find_element_by_id(location).click()
		time.sleep(2)
		box = Select(driver.find_element_by_id(location))
		box.select_by_visible_text(value)
		time.sleep(2)