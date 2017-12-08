import time
import capture_login_actions
import unittest
import test_base
import data_entry_actions
import general_actions
import xpath_locators # REMOVE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


'''
	Created by Nick Hartley
	11/28/2017
'''

class Documents(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\n\n************* TEST STARTING *************\n')
		
		
	# Verify user can claim a document - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_claim_document(self):		
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Verify search count?
		#data_entry_actions.verify_count(?)
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify results - Only check first row
		#rows = [1]
		#data_entry_actions.compare_results_with_row_numbers('documents_expected', 'data_entry_claim_document_1', rows)
		
		# Claim first document
		data_entry_actions.single_doc_stack_action('claim documents', 1)
		
		# Navigate to 'My Unfinished Documents'
		data_entry_actions.perform_stack_filter('My Unfinished Documents')
		
		# Verify search count - should be one
		#data_entry_actions.verify_count(1)
		
		# Verify results in 'My Unfinished Documents'
		#data_entry_actions.compare_results('documents_expected', 'data_entry_documents_claim_document_2')
		
		# Release document
		data_entry_actions.single_doc_stack_action('release documents', 1)

	
	# Verify documents claimed by others - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_claimed_by_others(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Navigate to 'Documents Claimed By Others'
		data_entry_actions.perform_stack_filter('Documents Claimed By Others')
	
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
	
		# Verify results in 'Documents Claimed By Others'
		#data_entry_actions.compare_results('documents_expected', 'data_entry_documents_claimed_by_others')
	
	
	# Verify my unfinished documents - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_my_unfinished_documents(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Navigate to 'My Unfinished Documents'
		data_entry_actions.perform_stack_filter('My Unfinished Documents')
	
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
	
		# Verify results in 'Documents Claimed By Others'
		#data_entry_actions.compare_results('documents_expected', 'data_entry_documents_claimed_by_others')
		time.sleep(10)


	# Verify user can release a document - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_release_document(self):		
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify results - Only check first row
		#rows = [1]
		#data_entry_actions.compare_results_with_row_numbers('documents_expected', 'data_entry_release_document_1', rows)
		
		# Claim first document
		data_entry_actions.single_doc_stack_action('claim documents', 1)
		
		

		# Return to Data Entry -> Validate Documents
		#general_actions.go_to_validate_documents_page()
		
		# Navigate to 'My Unfinished Documents'
		data_entry_actions.perform_stack_filter('My Unfinished Documents')
		
		# Verify count in 'My Unfinished Documents' - should be one
		#data_entry_actions.verify_count(1)
		
		# Release document
		data_entry_actions.single_doc_stack_action('release documents', 1)
		
		
		try:
			WebDriverWait(self.driver, 10).until(
				expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.data_entry_release_doc_alert_btn))
			)
		finally:
			self.driver.find_element_by_xpath(xpath_locators.data_entry_release_doc_alert_btn).click()
		
		
		'''	
		time.sleep(4)
		
		self.driver.find_element_by_xpath(xpath_locators.data_entry_release_doc_alert_btn).click()
			
		time.sleep(2)
		'''
		
		# Navigate to 'Available Documents'
		data_entry_actions.perform_stack_filter('Available Documents')
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify that claimed document has been released back to 'Available Documents' - Only check first row
		#rows = [1]
		#data_entry_actions.compare_results_with_row_numbers('documents_expected', 'data_entry_release_document_1', rows)
		
		time.sleep(10)


		
	
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Documents('test_cc_data_entry_documents_claim_document'))
	#suite.addTest(Documents(''))
	return suite
	
	
if __name__ == '__main__':	
	runner = unittest.TextTestRunner()
	runner.run(suite())	
	
	
'''	
if __name__ == '__main__':
	unittest.main()
'''		
		
		
		
		
		
		
		
		
		
		
		
		
		
		