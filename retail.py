import time
import capture_login_actions
import unittest
import test_base
import data_entry_actions
import general_actions
import retail_search_actions


'''
	Created by Nick Hartley
	12/02/2017
'''

class Search(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\n\n************* TEST STARTING *************\n')
		
	'''
	# Click add customer, enter info and click on Next - PERFECT
	def test_cc_retail_create_new_customer_and_certificate_next(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Change company
		general_actions.change_company('QA_Automation_Hartley')
		
		# Change client
		general_actions.change_client('Retail')
		
		# Navigate to Retail
		general_actions.go_to_retail_page()
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Open 'New Exemption' modal
		retail_search_actions.open_new_exemption_modal()
		
		# Filling our 'New Customer and Document' fields
		retail_search_actions.retail_new_customer_and_certificate('Name', 'Testing Time Inc.')
		retail_search_actions.retail_new_customer_and_certificate('EMAil', 'CreateNewCustAndCert@avalara.com')
		retail_search_actions.retail_new_customer_and_certificate('ADDRESS', '123 test avenue')
		retail_search_actions.retail_new_customer_and_certificate('city', 'Raleigh')
		retail_search_actions.retail_new_customer_and_certificate('sTate', 'North Carolina')
		retail_search_actions.retail_new_customer_and_certificate('zip', 27617)
		
		time.sleep(5)
		
		# Click 'Next' on 'New Customer and Document' modal
		retail_search_actions.click_new_customer_next()
		
		time.sleep(5)
		
		retail_search_actions.check_for_exemption_modal_close()
	
	
	# Verifies that a customer certificate can be downloaded - PERFECT	
	def test_cc_retail_customer_information_download(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')

		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('customer number', 'cust_9')
		
		# Execute retail search
		retail_search_actions.click_search_button()		
	
		# Click the second certificate in the first row of search results
		retail_search_actions.click_search_result_certificate(1, 2)
		
		# Storing the current newest PDF file in the downloads directory
		file = retail_search_actions.check_for_newest_pdf_in_download_directory()
		
		# Clicks the 'Download' button on the 'Customer Information' modal
		retail_search_actions.click_certificate_download_button()
		
		# Check for the newest PDF file in the downloads directory
		retail_search_actions.check_for_newest_pdf_in_download_directory()
		
		# Checking that a new file has been added to the downloads directory
		retail_search_actions.verify_new_file_download(file)
	'''	
	
	# Verifies edit customer functionality - PERFECT
	def test_cc_retail_customer_information_edit(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')

		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('customer number', 'cust_9')

		# Execute retail search
		retail_search_actions.click_search_button()

		# Click on the first row of search results
		retail_search_actions.click_search_result_row(1)
		
		# Click the customer edit button
		retail_search_actions.click_customer_edit_button()
		
		# Verify that the 'Edit Customer' modal appears
		retail_search_actions.verify_customer_edit_modal()
		
		
	'''
	# Verify that users can search by Certificate ID in retail - PERFECT
	def test_cc_retail_exemption_search_by_certificate_id(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		#general_actions.change_company('034Motorsport')
		#general_actions.change_client('034Motorsport, Inc.')
		
		# Navigate to Retail
		general_actions.go_to_retail_page()
		
		# Search certificates by certificate id
		retail_search_actions.retail_search_pick_search_field('customer number', 28)
		
		# Execute retail search
		retail_search_actions.click_search_button()
		
		# Verify search results
		retail_search_actions.compare_results('retail_expected', 'retail_search_cert_id')
	'''
		
		
if __name__ == '__main__':
	unittest.main()
