import capture_login_actions
import unittest
import test_base
import data_entry.actions
import data_entry.audits
import data_entry.store_results
import general.actions
#import time
#from selenium import webdriver                   - Don't 
#from selenium.webdriver.common.keys import Keys  - need?


'''
	Created by Nick Hartley
	11/28/2017
'''

class Sort(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\n\n************* TEST STARTING *************\n')

		
	# Verify that you can sort data entry by stage - PERFECT
	def test_cc_data_entry_sort_stage(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Change company
		general.actions.change_company('QA_Automation_Hartley')
		
		# Change client
		#general.change_client('Data_Entry_SortStage')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by stage - descending (Z -> A)
		data_entry.actions.sort_search_results('stage')
		
		# Verify results
		#data_entry.store_results.store_results_in_google_sheet('sort_expected', 'data_entry_sort_stage_descending', True)
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_stage_descending')
		
		# Reverse the sort - ascending (A -> Z)
		#data_entry.actions.sort_search_results('stage')
		
		# Verify results
		#data_entry.store_results.store_results_in_google_sheet('sort_expected', 'data_entry_sort_stage_ascending', True)
		#data_entry.audits.compare_results('sort_expected', 'data_entry_sort_stage_ascending')

		
	# Verify that you can sort data entry by source - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_source(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by source - descending (Z -> A)
		data_entry.actions.sort_search_results('source')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_source_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('source')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_source_descending')

		
	# Verify that you can sort data entry by priority - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_priority(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by priority - descending (Z -> A)
		data_entry.actions.sort_search_results('priority')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_priority_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('priority')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_priority_descending')

		
	# Verify that you can sort data entry by exposure zone - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_exposure_zone(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by exposure zone - descending (Z -> A)
		data_entry.actions.sort_search_results('exposure zone')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_exposure_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('exposure zone')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_exposure_descending')
		
		
	# Verify that you can sort data entry by certificate id - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_certificate_id(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by certificate id - descending (Z -> A)
		data_entry.actions.sort_search_results('certificate id')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_id_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('certificate id')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_id_descending')		
		
		
	# Verify that you can sort data entry by customer number - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_customer_number(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by customer number - descending (Z -> A)
		data_entry.actions.sort_search_results('customer number')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_cust_number_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('customer number')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_cust_number_descending')
		
		
	# Verify that you can sort data entry by age - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_age(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by age - descending (Z -> A)
		data_entry.actions.sort_search_results('age')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_age_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('age')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_age_descending')
		
		
	# Verify that you can sort data entry by account - NEEDS EXPECTED RESULTS
	def test_cc_data_entry_sort_account(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general.actions.click('validate documents')
		
		# Sort by account - descending (Z -> A)
		data_entry.actions.sort_search_results('account')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_account_ascending')
		
		# Reverse the sort - ascending (A -> Z)
		data_entry.actions.sort_search_results('account')
		
		# Verify results
		data_entry.audits.compare_results('sort_expected', 'data_entry_sort_account_descending')

		
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Sort('test_cc_data_entry_sort_stage'))
	#suite.addTest(Search('test_cc_data_entry_search_stage_reviewed'))
	return suite
	

if __name__ == '__main__':	
	runner = unittest.TextTestRunner()
	runner.run(suite())
	
'''
if __name__ == '__main__':
	run_tests = unittest.TestSuite()
	run_tests.addTest(suite())
	result = unittest.TestResult()
	run_tests.run(result)
	print(result)
	print('Tests Run:', result.testsRun)
	print('Success?', result.wasSuccessful())
'''			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	