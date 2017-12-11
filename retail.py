import time
import capture_login_actions
import unittest
import test_base
import general_actions
import retail_search_actions


'''
	Created by Nick Hartley
	12/02/2017
'''

class Retail(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\n\n************* TEST STARTING *************\n')
		
	
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
	INCOMPLETE - Out of date?
	
	# Verifies other exemption on file button functions	
	def test_cc_customer_information_other_exemption_on_file(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('customer number', 'cust_9')
	
	'''
	
	# Verifies that 'Print Certificate' button functions - Only works with Chrome for now
	def test_cc_retail_customer_information_print(self):
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
		
		# Storing current window handles [Should only be 1]
		window = self.driver.window_handles
		
		# Click the certificate download button
		retail_search_actions.click_certificate_print_button()
		
		# Verify that pressing the download button opened a new window
		retail_search_actions.verify_certificate_print_window(window)
	
	
	# Verify that when choose the View Details button it will then show the details of that certificate - PERFECT
	def test_cc_retail_customer_information_view_detail(self):
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
		
		# Click the certificate view button		
		retail_search_actions.click_certificate_view_button()
		
		# Verify that a certificate preview modal appears
		retail_search_actions.verify_certificate_view_modal()
	
	
	# Verify clicking on X works - PERFECT
	def test_cc_retail_customer_information_x_button(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('customer number', 'cust_1')

		# Execute retail search
		retail_search_actions.click_search_button()

		# Click on the first row of search results
		retail_search_actions.click_search_result_row(1)
		
		# Click the 'X' on the customer details modal
		retail_search_actions.click_customer_details_modal_close()
		
		# Verify that modal was closed
		retail_search_actions.verify_customer_details_modal_close()
	
	
	# Verify that search results can be sorted by address - PERFECT
	def test_cc_retail_exemption_information_sort_address(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		

		# Execute a blank retail search
		retail_search_actions.click_search_button()
		
		# Sort search results by address
		retail_search_actions.retail_search_sort_results('CUSTOMER ADDRESS')
		
		# Compare results
		retail_search_actions.compare_results('retail_expected', 'retail_search_sort_address')
	
	
	# Verify that a new division can be selected - PERFECT
	def test_cc_retail_change_division(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe Retail')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Storing current division name
		division = retail_search_actions.retrieve_division_name()
		
		# Open 'Change Division' drop down menu
		retail_search_actions.change_division('Retail 2')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Verify that a new retail division context has been entered
		retail_search_actions.verify_change_division(division)
		
		
	# Verify that a new location can be selected - PERFECT
	def test_cc_retail_change_location(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe Retail')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Storing current division name
		location = retail_search_actions.retrieve_location_name()
		
		# Open 'Change Division' drop down menu
		retail_search_actions.change_location('Location 2')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Verify that a new retail division context has been entered
		retail_search_actions.verify_change_location(location)
			
		
	# Verify that clicking on a search result row opens a customer information modal for the selected customer
	def test_cc_retail_click_customer(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Search certificates by customer number
		customer = 'cust_1'
		retail_search_actions.retail_search_pick_search_field('customer number', customer)

		# Execute a blank retail search
		retail_search_actions.click_search_button()		

		# Click on the first row of search results
		retail_search_actions.click_search_result_row(1)			
			
		# Verify that the customer information modal for searched customer was opened
		retail_search_actions.verify_click_customer(customer)
			
		
	# Verify that search results can be sorted by customer number - PERFECT
	def test_cc_retail_search_sort_customer_number(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe Retail')		
		
		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('state', 'Alaska')

		# Execute a blank retail search
		retail_search_actions.click_search_button()

		# Sort search results by customer number
		retail_search_actions.retail_search_sort_results('number')
		
		# Compare results
		retail_search_actions.compare_results('retail_expected', 'retail_search_sort_customer_number')
	
	
	# Verify that search results can be sorted by certificate(s) - PERFECT
	def test_cc_retail_search_sort_certificates(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Search certificates by customer number
		retail_search_actions.retail_search_pick_search_field('email', 'bob.caldwell@avalara.com')

		# Execute a blank retail search
		retail_search_actions.click_search_button()

		# Sort search results by customer number
		retail_search_actions.retail_search_sort_results('certs')
		
		# Compare results
		retail_search_actions.compare_results('retail_expected', 'retail_search_sort_certificates')
	
	
	# Verify that search results can be sorted by name - PERFECT
	def test_cc_retail_search_sort_name(self):
		# Open CertCapture
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe Retail')		
		
		# Search certificates by state
		retail_search_actions.retail_search_pick_search_field('state', 'Alaska')

		# Execute a blank retail search
		retail_search_actions.click_search_button()

		# Sort search results by customer name
		retail_search_actions.retail_search_sort_results('name')
		
		# Compare results
		retail_search_actions.compare_results('retail_expected', 'retail_search_sort_name')	
	
	
	# Verify that search results can be sorted by phone
	def test_cc_retail_search_sort_phone(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Search certificates by email
		retail_search_actions.retail_search_pick_search_field('email', 'bob.caldwell@avalara.com')

		# Execute a blank retail search
		retail_search_actions.click_search_button()

		# Sort search results by certificates
		retail_search_actions.retail_search_sort_results('certificates')		
		time.sleep(3)
		# Sort search results by phone number
		retail_search_actions.retail_search_sort_results('phone')
		
		# Compare results
		retail_search_actions.compare_results('retail_expected', 'retail_search_sort_phone')	
	
	
	# Verify that the 'Search' button opens the search modal
	def test_cc_retail_search_button(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		time.sleep(3)
		# Click the 'Search' button
		retail_search_actions.open_search_modal()
		
		# Verify that the search modal is open
		retail_search_actions.verify_search_modal_open()
		
	
	# Verify that hitting the 'Clear Screen' button clears the search fields - PERFECT
	def test_cc_retail_clear_screen_button(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob Retail')		
		
		# Execute a blank retail search
		retail_search_actions.click_search_button()
		
		# Storing search result count for a blank search
		count = retail_search_actions.retail_search_count()
		
		# Open search modal again
		retail_search_actions.open_search_modal()
		
		# Search certificates by email
		retail_search_actions.retail_search_pick_search_field('customer name', 'Johnny Test')
		retail_search_actions.retail_search_pick_search_field('phone', '1234567890')
		retail_search_actions.retail_search_pick_search_field('email', 'test@email.com')
		retail_search_actions.retail_search_pick_search_field('city', 'Townsville')
		retail_search_actions.retail_search_pick_search_field('state', 'California')
		retail_search_actions.retail_search_pick_search_field('zip', '90210')
		retail_search_actions.retail_search_pick_search_field('customer number', '1886')
		retail_search_actions.retail_search_pick_search_field('id', 'doc_id')
		retail_search_actions.retail_search_pick_search_field('exposure zone', 'New York')
		
		# Click 'Clear Screen' button
		retail_search_actions.click_clear_screen_button()
		time.sleep(2)
		# Execute a blank retail search
		retail_search_actions.click_search_button()
		
		assert count == retail_search_actions.retail_search_count()
	
	
	
	# Verify that a user can logout successfully - PERFECT
	def test_cc_retail_logout(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe Retail')
		
		# Close search modal
		retail_search_actions.close_search_modal()
		
		# Click 'Logout' button
		retail_search_actions.retail_logout()
		
		# Verify that the user has logged out
		retail_search_actions.verify_retail_logout()
	
	
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
		

		

		
def suite():
	suite = unittest.TestSuite()
	#suite.addTest(Retail('test_cc_retail_exemption_information_sort_address'))
	suite.addTest(Retail('test_cc_retail_clear_screen_button'))
	return suite
	
	
if __name__ == '__main__':	
	runner = unittest.TextTestRunner()
	runner.run(suite())
	

	
	
	
	
	