import json
import test_base
import time
import requests
import pdf_reader
import general_actions.helpers as helpers
import send_single_request.locations as locations
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

'''
	Created by Nick Hartley
	3/14/2018
'''


driver = test_base.driver

def click(target_name):
	target = target_name.lower()
	
	if target == 'generate request button' or target == 'generate request top button':
		return helpers.click_helper(locations.Buttons.generate_request_top)
	elif target == 'generate request bottom button':
		return helpers.click_helper(locations.Buttons.generate_request_bottom)
	elif target == 'add exposure zone button' or target == 'add shipto state/zone button' or target == 'add shipto zone button':
		return helpers.click_helper(locations.Buttons.add_exposure_zone)
	elif target == 'customer search input':
		return helpers.click_helper(locations.Inputs.search_customer_name_number)
	elif target == 'customer number / name input':
		return helpers.click_helper(locations.Inputs.customer)
	elif target == 'return date input':
		return helpers.click_helper(locations.Inputs.return_date)
	elif target == 'email address input' or target == 'email input':
		return helpers.click_helper(locations.Inputs.email_address)
	elif target == 'fax number input':
		return helpers.click_helper(locations.Inputs.fax_number)
	elif target == 'exposure zone select all link':
		return helpers.click_helper(locations.Links.exposure_zones_select_all)
	elif target == 'exposure zone select none link':
		return helpers.click_helper(locations.Links.exposure_zones_select_none)
	elif target == 'exposure zone select default link':
		return helpers.click_helper(locations.Links.exposure_zones_select_default)
	elif target == 'exempt reason select all link':
		return helpers.click_helper(locations.Links.exempt_reasons_select_all)
	elif target == 'exempt reason deselect all link' or target == 'exempt reason de-select all link':
		return helpers.click_helper(locations.Links.exempt_reasons_deselect_all)
	elif target == 'exemption certificate templates select all link' or target == 'templates select all link':
		return helpers.click_helper(locations.Links.templates_select_all)
	elif target == 'exemption certificate templates deselect all link' or target == 'exemption certificate templates de-select all link' or target == 'templates deselect all link' or target == 'templates de-select all link':
		return helpers.click_helper(locations.Links.templates_deselect_all)
	elif target == 'company select':
		return helpers.click_helper(locations.Selects.company)
	elif target == 'delivery method select':
		return helpers.click_helper(locations.Selects.delivery_method)
	elif target == 'cover letter select':
		return helpers.click_helper(locations.Selects.cover_letter)
	elif target == 'exempt reason input':
		return helpers.click_helper(locations.Inputs.exempt_reason)
	elif target == 'document type select':
		return helpers.click_helper(locations.Selects.document_type)
	else:
		print('Invalid target requested.')
		
def add_shipto_zone_state_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'state link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_state_tab)
	elif target == 'excise certificates link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_excise_certificates_tab)
	elif target == 'excise licenses link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_excise_licenses_tab)
	elif target == 'federal withholding link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_federal_withholding_tab)
	elif target == 'custom zone link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_custom_zone_tab)
	elif target == 'vat link':
		helpers.click_helper(locations.Links.add_shipto_zone_state_modal_vat_tab)
	elif target == 'state select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_state)
	elif target == 'excise certificates select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_excise_certificates)
	elif target == 'excise licenses select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_excise_licenses)
	elif target == 'federal withholding select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_federal_withholding)
	elif target == 'custom zone select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_custom_zone)
	elif target == 'vat select':
		helpers.click_helper(locations.Selects.add_shipto_zone_state_modal_vat)
	elif target == 'add shipto state button':
		helpers.click_helper(locations.Buttons.add_shipto_zone_state_modal_add_shipto_state)
	elif target == 'add shipto zone button':
		helpers.click_helper(locations.Buttons.add_shipto_zone_state_modal_add_shipto_zone)
	elif target == 'cancel button':
		helpers.click_helper(locations.Buttons.add_shipto_zone_state_modal_cancel)
	elif target == 'close button' or target == 'x button':
		helpers.click_helper(locations.Buttons.add_shipto_zone_state_modal_close)
	else:
		print('Invalid target requested.')
		
def select_recipient_customer(customer):
	ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="customer_number_search"]')).click().send_keys(customer).perform()
	time.sleep(2)
	ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span/div/span/div[1]/div/div[1]')).click().perform()
	
	
def select_document_type(type):
	type = type.title()
	
	if type == 'Sales And Use Tax':
		type = 'Sales and Use Tax'
	elif type == 'Vat':
		type = 'VAT'
	
	helpers.select_helper(locations.Selects.document_type, type)
	
def select_company(company):
	helpers.select_helper(locations.Selects.company, company)
	
def select_cover_letter(letter):
	letter = letter.title()
	
	if letter == 'Standard_Request':
		letter = letter.upper()
	elif letter[-17:] == 'Sales And Use Tax':
		letter = letter[:-17] + 'Sales and Use Tax'
	elif letter == 'Standard Request - Vat Identification Information':
		letter = 'Standard Request - VAT Identification Information'
	
	helpers.select_helper(locations.Selects.cover_letter, letter)

def select_delivery_method(method):
	helpers.select_helper(locations.Selects.delivery_method, method.capitalize())
	
def set_email_address(email):
	field = click('email address input')
	field.clear()
	field.send_keys(email)
	
def select_exempt_reasons(reasons):
	# Cast argument to a list if one wasn't passed in
	if type(reasons) is not list:
		reasons = [ reasons ]
	
	for reason in reasons:
		click('exempt reason input')
		
		x = 1
		check = True
		
		while check:
			try:
				if reason.upper() == driver.find_element_by_xpath('//*[@id="tax_code_id_chosen"]/div/ul/li[' + str(x) + ']').text:
					driver.find_element_by_xpath('//*[@id="tax_code_id_chosen"]/div/ul/li[' + str(x) + ']').click()
					check = False
				else:
					x += 1
			except NoSuchElementException:
				print('Unable to locate exempt reason.')
				check = False
			
def select_exposure_zones(zones):
	# Cast argument to a list if one wasn't passed in
	if type(zones) is not list:
		zones = [ zones ]
		
	# Click the 'Select None' link to ensure that all zones are unchecked
	click('exposure zone select none link')
	
	current_zone_type = ''
	
	for zone in zones:
	
		z = zone.lower()
		if z == 'state' or z == 'excise certificates' or z == 'excise licenses' or z == 'federal withholding' or z == 'custom zone' or z == 'vat':
			current_zone_type = z
		else:
	
			x = 1
			check = True
			found = False
			
			while check:
				try:
					label = driver.find_element_by_xpath('//*[@id="send_request_exposures_table"]/tbody/tr[' + str(x) + ']/td[1]/div/label/span[2]').text
					print(label)

					if zone.title() == label or label == zone.title() + ' Sales Tax':
						check = False
						found = True
						print('found')
					else:
						x += 1
				except NoSuchElementException:
					check = False
					
			if found:
				driver.find_element_by_xpath('//*[@id="send_request_exposures_table"]/tbody/tr[' + str(x) + ']/td[1]/div/label/input').click()
			else:
				if current_zone_type == '':
					print('No zone type set. Pass "state", "excise certificates", "excise licenses", "federal withholding", "custom zone", or "vat" in the zones array to set zone type.')
				else:
					zone = zone.title()
					
					click('add shipto zone button')
					
					if current_zone_type == 'state':
						try:
							add_shipto_zone_state_modal_click('state link')
							helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_state, zone)
							add_shipto_zone_state_modal_click('add shipto state button')
						except NoSuchElementException:
							if zone.endswith(' Sales Tax'):
								zone_list = zone.split( )
								new_zone = ''
								
								for x in range(0, len(zone_list)):
									if zone_list[x] != 'Sales' or zone_list[x] != 'Tax':
										new_zone += zone_list[x]
								
								zone = new_zone
							else:
								zone += ' Sales Tax'
									
							try:
								add_shipto_zone_state_modal_click('state link')
								helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_state, zone)
								add_shipto_zone_state_modal_click('add shipto state button')
							except NoSuchElementException:
								print('Sales and Use Tax exposure zone not found.')
							
					elif current_zone_type == 'excise certificates':
						add_shipto_zone_state_modal_click('excise certificates link')
						helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_excise_certificates, zone)
						add_shipto_zone_state_modal_click('add shipto zone button')
					elif current_zone_type == 'excise licenses':
						add_shipto_zone_state_modal_click('excise licenses link')
						helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_excise_licenses, zone)
						add_shipto_zone_state_modal_click('add shipto zone button')
					elif current_zone_type == 'federal withholding':
						add_shipto_zone_state_modal_click('federal withholding link')
						helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_federal_withholding, zone)
						add_shipto_zone_state_modal_click('add shipto zone button')
					elif current_zone_type == 'custom zone':
						add_shipto_zone_state_modal_click('custom zone link')
						helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_custom_zone, zone)
						add_shipto_zone_state_modal_click('add shipto zone button')
					elif current_zone_type == 'vat':
						add_shipto_zone_state_modal_click('vat link')
						helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_vat, zone)
						add_shipto_zone_state_modal_click('add shipto zone button')
					else:
						print('Some zone type error occured.')

def set_return_date(date):
	field = click('return date input')
	field.clear()
	field.send_keys(date)
						
def set_up_request(customer):
	click('document type select')
	
def store_request_url_in_json():
	link = pdf_reader.get_request_link_from_request_pdf()
	print('Opening request link:', link)
	
	my_data = {}
	my_data['url'] = link

	with open('send_single_request\\request.json', 'w') as f:
		json.dump(my_data, f)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	