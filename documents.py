import time
import capture_login_actions
import unittest
import test_base
import data_entry.actions
import data_entry.audits
import data_entry.store_results
import general_actions.actions
from report_test_result import ReportTestResult


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
		general_actions.actions.click('validate documents')
		
		# Verify search count?
		#data_entry_actions.verify_count(?)
		
		# Sort by certificate id
		data_entry.actions.sort_search_results('certificate id')
		
		# Claim first document
		#data_entry_actions.single_doc_stack_action('claim documents', 1)
		data_entry.actions.select_single_document_in_row(1)
		data_entry.actions.click('Action')
		data_entry.actions.click('Claim documents')
		
		# Navigate to 'My Unfinished Documents'
		data_entry.actions.filter_documents('My Unfinished Documents')
		
		# Verify search count - should be two
		#data_entry.audits.verify_count(2)
		
		# Verify results in 'My Unfinished Documents'
		data_entry.audits.compare_results('documents_expected', 'data_entry_documents_claim_document')
		
		# Release document
		data_entry.actions.select_single_document_in_row(1)
		data_entry.actions.click('Action')
		data_entry.actions.click('Release documents')

	
	# Verify documents claimed by others - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_claimed_by_others(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.actions.click('validate documents')
		
		# Navigate to 'Documents Claimed By Others'
		data_entry.actions.filer_documents('Documents Claimed By Others')
	
		# Sort by certificate id
		data_entry.actions.sort_search_results('certificate id')
	
		# Verify results in 'Documents Claimed By Others'
		#data_entry.audits.compare_results('documents_expected', 'data_entry_documents_claimed_by_others')
	
	
	# Verify my unfinished documents - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_my_unfinished_documents(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.actions.click('validate documents')
		
		# Navigate to 'My Unfinished Documents'
		data_entry.actions.filer_documents('My Unfinished Documents')
	
		# Sort by certificate id
		data_entry.actions.sort_search_results('certificate id')
	
		# Verify results in 'Documents Claimed By Others'
		#data_entry.audits.compare_results('documents_expected', 'data_entry_documents_claimed_by_others')
		time.sleep(10)


	# Verify user can release a document - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_documents_release_document(self):		
		# Open CertCapture
		capture_login_actions.capture_open_portal()
	
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.actions.click('validate documents')
		
		# Sort by certificate id
		data_entry.actions.sort_search_results('certificate id')
		
		# Verify results - Only check first row
		#rows = [1]
		#data_entry.audits.compare_results_with_row_numbers('documents_expected', 'data_entry_release_document_1', rows)
		
		# Claim first document
		data_entry_actions.single_doc_stack_action('claim documents', 1)
		
		

		# Return to Data Entry -> Validate Documents
		#general_actions.actions.click('validate documents')
		
		# Navigate to 'My Unfinished Documents'
		data_entry.actions.filer_documents('My Unfinished Documents')
		
		# Verify count in 'My Unfinished Documents' - should be one
		#data_entry_actions.verify_count(1)
		
		# Release document
		data_entry_actions.single_doc_stack_action('release documents', 1)
		
		'''	
		try:
			WebDriverWait(self.driver, 10).until(
				expected_conditions.element_to_be_clickable((By.XPATH, xpath_locators.data_entry_release_doc_alert_btn))
			)
		finally:
			self.driver.find_element_by_xpath(xpath_locators.data_entry_release_doc_alert_btn).click()
		
		
		
		time.sleep(4)
		
		self.driver.find_element_by_xpath(xpath_locators.data_entry_release_doc_alert_btn).click()
			
		time.sleep(2)
		'''
		
		# Navigate to 'Available Documents'
		data_entry.actions.filer_documents('Available Documents')
		
		# Sort by certificate id
		data_entry.actions.sort_search_results('certificate id')
		
		# Verify that claimed document has been released back to 'Available Documents' - Only check first row
		#rows = [1]
		#data_entry.audits.compare_results_with_row_numbers('documents_expected', 'data_entry_release_document_1', rows)
		
		time.sleep(10)
		
		
		#def tearDown(self):
			#if self.unreturned == True:
				

		
	
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Documents('test_cc_data_entry_documents_claim_document'))
	#suite.addTest(Documents(''))
	return suite
	
	
if __name__ == '__main__':	
	#runner = unittest.TextTestRunner(resultclass=ReportTestResult)
	runner = unittest.TextTestRunner()
	runner.run(suite())	
	
	
'''	
if __name__ == '__main__':
	unittest.main()
'''		
		
		
		
		
		
		
		
		
		
		
		
		
		
		