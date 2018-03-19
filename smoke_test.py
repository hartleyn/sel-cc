import time
import capture_login_actions
import unittest
import test_base
import general_actions.actions
from report_test_result import ReportTestResult

'''
	Created by Nick Hartley
	2/27/2018
'''

class SmokeTest(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\nStarting smoke test on' + test_base.browser.title() + '.\n')
		print('\n************* TEST STARTING *************\n')
	
	def create_new_company(self):
		# Login
		
	
		# Navigate to 'SysAdmin' -> 'Company Accounts'
		general_actions.actions.click('Company Accounts')
		
		# Click the 'Add Account' button
		company_accounts.actions.click('Add Account')
		
		# Complete new account form
		company_accounts.actions.complete_add_account_form('6_8_9_Smoke_Test_GC', '1 1st st', 'Building #2', 'North Babylon', 'New York', 'United States', '10038', '555-555-5555')

		# Click the 'Add Account' button
		company_accounts.actions.add_account_modal_click('Add Account')
		
		# Verify that the account was created
		
		
	def create_new_hierarchy(self):
		# Login
		
		
		# Navigate to 'Settings' -> 'Account Settings' -> 'Account Details'
		general_actions.actions.click('Account Details')
		
		# Click the 'Company Hierarchy' tab
		account_details.actions.click('Company Hierarchy')
		
		# Click the 'Add Company' button
		account_details.actions.company_hierarchy_tab_click('Add Company button')
		
		# Complete the new company form
		account_details.actions.complete_add_company_form('6_9_0_Smoke_Test_Co.', 'Legal test name', False, '123 4th st', 'Big Box Building', 'Townsville', 'United States', 'Colorado', '90210', '646-867-5309')
		
		# Click the 'Add' button
		account_details.actions.add_company_modal_click('Add button')
		
		# Verify that the new company was created
		
		
	def assign_all_states_in_nexus_settings(self):
		# Login
		
	
		# Navigate to 'Content Library' -> 'Nexus Settings'
		general_actions.actions.click('Nexus Settings')
	
		# Click the 'Assign Nexus' button
		nexus_settings.click('Assign Nexus')
		
		# Click the 'Toggle Select All' checkbox
		nexus_settings.us_edit_client_nexus_modal_click('Toggle Select All input')
		
		# Click the 'Update Client Nexus' button
		nexus_settings.us_edit_client_nexus_modal_click('Update Client Nexus button')
		
		# Verify that all states are assigned (Look for green checkmark)
		
		
	def enable_public_wizard_and_retail(self):
		# Login
		
		
		# Navigate to 'Settings' -> 'Account Settings' -> 'Account Details'
		general_actions.actions.click('Account Details')
		
		# Navigate to the 'Features' tab
		account_details.actions.tabs_click('Features')
		
		# Check the 'Public Wizard' box
		account_details.actions.features_tab_click('Public Wizard input')
		
		# Navigate to 'Settings' -> 'Company Settings' -> 'Company Details'
		general_actions.actions.click('Company Details')
		
		# Navigate to the 'Company Settings' tab
		company_details.actions.click('Company Settings')
		
		# Click the 'Edit Company Settings' button
		company_details.actions.click('edit company settings')
		
		# Click the 'Use Locations' checkbox
		company_details.actions.edit_company_settings_modal_click('Use Locations input')
		
		# Click the 'Update Company Settings' button
		company_details.actions.edit_company_settings_modal_click('Update Company Settings button')
		
		# Verify that 'Public Wizard' and 'Retail' are enabled
	
	
	def bulk_import_customers(self):
		# Login
		
		
		# Navigate to 'Customers' -> 'Bulk Import'
		general_actions.actions.click('bulk import')
		
		# Call customer bulk import function - file must be in the test_assets directory
		bulk_import.actions.bulk_import_customers_from_file('import_mock_data.xlsx')

		# Verify that customers were uploaded
	
	
	def send_single_request(self):
		# Login
		
		
		# Navigate to 'Manage Documents' -> 'Send Single Request'
		general_actions.actions.click('send single request')
		
		# Select a customer to send a request
		send_single_request.actions.select_recipient_customer('cc1')
		
		# Select 'All Document Types' from the document type dropdown
		send_single_request.actions.select_document_type('all document types')
		
		# Select exposure zone(s)
		zones = ['state', 'California', 'arizona', 'Guam']
		send_single_request.actions.select_exposure_zones(zones)
		
		# Select exempt reason(s)
		reasons = ['agriculture', 'religious org', 'reSale']
		send_single_request.actions.select_exempt_reasons(reasons)
		
		# Click the templates "Select All' link
		send_single_request.actions.click('templates select all link')
		
		# Set delivery method
		send_single_request.actions.select_delivery_method('email')
		
		# Enter email address
		send_single_request.actions.click('email address input').clear().send_keys('cc.automated.user@gmail.com') # Clear values
		
		# Set 'Cover Letter' field
		send_single_request.actions.select_cover_letter('standard_request')
		
		# Set return date
		send_single_request.actions.click('return date input').clear().send_keys('2018-08-04')  # Clear values
		
		# Click the 'Send Request' button
		
	
	
		
		
	