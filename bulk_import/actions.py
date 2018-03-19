import general_actions.helpers as helpers
import bulk_import.locations as locations
import test_base
import time
import os


'''
	Created by Nick Hartley
	3/14/2018
'''

driver = test_base.driver

def click(target_name):
	target = target_name.lower()
	
	if target == 'choose file input':
		return helpers.click_helper(locations.Inputs.choose_file)
	elif target == 'upload button':
		return helpers.click_helper(locations.Buttons.upload)
	elif target == 'import customer data button':
		return helpers.click_helper(locations.Buttons.import_customer_data)
	elif target == 'success modal ok button': # Not working for some reason? Other seem to work fine.
		return helpers.click_helper(locations.Buttons.success_modal_ok)
	elif target == 'success modal close button':
		return helpers.click_helper(locations.Buttons.success_modal_close)
	elif target == 'error modal ok button':
		return helpers.click_helper(locations.Buttons.error_modal_ok)
	elif target == 'error modal close button':
		return helpers.click_helper(locations.Buttons.error_modal_close)
	else:
		print('Invalid target requested.')

def import_customers_from_file(filename):
	filepath = os.getcwd() + test_base.slash + 'test_assets' + test_base.slash + filename
	print('file:', filepath)
	driver.find_element_by_xpath(locations.Inputs.choose_file).send_keys(filepath)
	
	click('upload button')
	#time.sleep(2)
	click('import customer data button')
	time.sleep(2)
	driver.find_element_by_xpath(locations.Buttons.success_modal_ok).click()