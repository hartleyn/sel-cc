import test_base
import company_accounts.locations as locations
import general_actions.helpers as helpers

'''
	Created by Nick Hartley
	3/6/18
'''


driver = test_base.driver

def click(target_name):
	target = target_name.lower()
	
	if target == 'add account':
		helpers.click_helper(locations.Buttons.add_account)
	elif target == 'provision avatax account':
		helpers.click_helper(locations.Buttons.provision_avatax_account)
	elif target == 'filter button':
		helpers.click_helper(locations.Buttons.filter)
	elif target == 'account list':
		helpers.click_helper(locations.Links.account_list)
	elif target == 'account statistics':
		helpers.click_helper(locations.Links.account_statistics)
	elif target == 'account / database name input':
		helpers.click_helper(locations.Inputs.account_database_name)
	elif target == 'zuora / avatax account id input':
		helpers.click_helper(locations.Inputs.zuora_avatax_id)
	elif target == 'filter tier input':
		helpers.click_helper(locations.Inputs.filter_tier)
	elif target == 'filter server input':
		helpers.click_helper(locations.Inputs.filter_server)
	elif target == 'filter status input':
		helpers.click_helper(locations.Inputs.filter_status)
	elif target == 'first top button':
		helpers.click_helper(locations.Buttons.first_top)
	elif target == 'prev top button':
		helpers.click_helper(locations.Buttons.prev_top)
	elif target == 'next top button':
		helpers.click_helper(locations.Buttons.next_top)
	elif target == 'last top button':
		helpers.click_helper(locations.Buttons.last_top)
	elif target == 'first bottom button':
		helpers.click_helper(locations.Buttons.first_bottom)
	elif target == 'prev bottom button':
		helpers.click_helper(locations.Buttons.prev_bottom)
	elif target == 'next bottom button':
		helpers.click_helper(locations.Buttons.next_bottom)
	elif target == 'last bottom button':
		helpers.click_helper(locations.Buttons.last_bottom)
	elif target == 'page select top button':
		helpers.click_helper(locations.Buttons.page_select_top)
	elif target == 'page select bottom button':
		helpers.click_helper(locations.Buttons.page_select_bottom)
	elif target == 'id header button':
		helpers.click_helper(locations.Buttons.id_header)
	elif target == 'name header button':
		helpers.click_helper(locations.Buttons.name_header)
	elif target == 'tier header button':
		helpers.click_helper(locations.Buttons.tier_header)
	elif target == 'zuora id header button':
		helpers.click_helper(locations.Buttons.zuora_id_header)
	elif target == 'database server header button':
		helpers.click_helper(locations.Buttons.database_server_header)
	elif target == 'database name header button':
		helpers.click_helper(locations.Buttons.database_name_header)
	else:
		print('Invalid click target requested')
		
def add_account_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'account name':
		helpers.click_helper(locations.Inputs.add_account_modal_account_name)
	elif target == 'address line 1':
		helpers.click_helper(locations.Inputs.add_account_modal_address_line_1)
	elif target == 'address line 2':
		helpers.click_helper(locations.Inputs.add_account_modal_address_line_2)
	elif target == 'city':
		helpers.click_helper(locations.Inputs.add_account_modal_city)
	elif target == 'state/province':
		helpers.click_helper(locations.Inputs.add_account_modal_state_province)		
	elif target == 'country':
		helpers.click_helper(locations.Inputs.add_account_modal_country)
	elif target == 'zip':
		helpers.click_helper(locations.Inputs.add_account_modal_zip)	
	elif target == 'phone':
		helpers.click_helper(locations.Inputs.add_account_modal_phone)
	elif target == 'zuora id':
		helpers.click_helper(locations.Inputs.add_account_modal_zuora_id)
	elif target == 'salesforce id':
		helpers.click_helper(locations.Inputs.add_account_modal_salesforce_id)
	elif target == 'database name':
		helpers.click_helper(locations.Inputs.add_account_modal_database_name)
	elif target == 'database server':
		helpers.click_helper(locations.Inputs.add_account_modal_database_server)
	elif target == 'tier':
		helpers.click_helper(locations.Inputs.add_account_modal_tier)	
	elif target == 'upload logo':
		helpers.click_helper(locations.Buttons.add_account_modal_upload_logo)
	elif target == 'demo account checkbox':
		helpers.click_helper(locations.Inputs.add_account_modal_demo_account_checkbox)		
	elif target == 'sandbox checkbox':
		helpers.click_helper(locations.Inputs.add_account_modal_sandbox_checkbox)
	elif target == 'x' or target == 'close':
		helpers.click_helper(locations.Buttons.add_account_modal_close)
	elif target == 'add account':
		helpers.click_helper(locations.Buttons.add_account_modal_add_account)
	elif target == 'cancel':
		helpers.click_helper(locations.Buttons.add_account_modal_cancel)
	elif target == 'reset':
		helpers.click_helper(locations.Buttons.add_account_modal_reset)
	else:
		print('Invalid click target requested')
		
def provision_avatax_account_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'avatax account id':
		helpers.click_helper(locations.Buttons.provision_avatax_account_modal_avatax_account_id)
	elif target == 'import ecms data checkbox':
		helpers.click_helper(locations.Inputs.provision_avatax_account_modal_import_ecms_data_checkbox)
	elif target == 'provision avatax account':
		helpers.click_helper(locations.Buttons.provision_avatax_account_modal_provision_avatax_account)
	elif target == 'cancel':
		helpers.click_helper(locations.Buttons.provision_avatax_account_modal_cancel)
	elif target == 'x' or target == 'close':
		helpers.click_helper(locations.Buttons.provision_avatax_account_modal_close)
	else:
		print('Invalid click target requested')
		
def complete_add_account_form(account_name, address_line_1, address_line_2, city, state_province, country, zip, phone):
	# Click the 'Account Name' field and fill field
	add_account_modal_click('Account Name')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_account_name).send_keys(account_name)
	
	# Click the 'Address Line 1' field and fill field
	add_account_modal_click('Address Line 1')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_address_line_1).send_keys(address_line_1)
	
	# Click the 'Address Line 2' field and fill field
	add_account_modal_click('Address Line 2')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_address_line_2).send_keys(address_line_2)

	# Click the 'City' field and fill field
	add_account_modal_click('City')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_city).send_keys(city)

	# Click the 'State/Province' field and fill field
	helpers.select_helper(locations.Inputs.add_account_modal_state_province, state_province)

	# Click the 'Country' field and fill field
	helpers.select_helper(locations.Inputs.add_account_modal_country, country)

	# Click the 'Zip' field and fill field
	add_account_modal_click('Zip')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_zip).send_keys(zip)

	# Click the 'Phone' field and fill field
	add_account_modal_click('Phone')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_phone).send_keys(phone)
	
	# Append account name to the 'Database Name' field
	add_account_modal_click('Database Name')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_database_name).send_keys(account_name)
	
	# Set 'Zuora ID' to 'Internal'
	add_account_modal_click('Zuora ID')
	driver.find_element_by_xpath(locations.Inputs.add_account_modal_zuora_id).send_keys('internal')
	
	# Set the 'Database Server' and 'Tier' fields
	add_account_modal_click('Database Server')
	driver.find_element_by_xpath('//select[@id="database_server"]/option').click()
	
	add_account_modal_click('Tier')
	driver.find_element_by_xpath('//select[@id="tier"]/option').click()
	
	time.sleep(2)
		
		
		