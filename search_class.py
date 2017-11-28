import time
import capture_login_actions
import unittest
import test_base
import data_entry_actions
import general_actions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


'''
	Created by Nick Hartley
	11/22/2017
'''

class Search(unittest.TestCase):
	def setUp(self):
		self.driver = test_base.driver
		
		print('\n\n************* TEST STARTING *************\n')
	
	# TODO - Verify that the advanced Search Slider is Functioning
	def test_cc_data_entry_search_basic_search_0001(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Toggle to basic search - Can't click toggle switch....
		data_entry_actions.search_type_toggle('basic search')
		
		# Verify basic search field
		data_entry_actions.verify_basic_search_fields()
	
	
	# TODO - Verify fields are visible for Basic Search
	def test_cc_data_entry_search_advanced_search_0001(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nick')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Toggle to basic search - Can't click toggle switch....
		data_entry_actions.search_type_toggle('basic search')
		
		# Verify basic search field
		data_entry_actions.verify_basic_search_fields()
		
		# Toggle to advanced search - Can't click toggle switch....
		data_entry_actions.search_type_toggle('advanced search')
		
		# Verify basic search field
		data_entry_actions.verify_advanced_search_fields()
	
	
	# Verify that you can search Data Entry by Bucket - 'External' - ACCOUNT CHANGED
	def test_cc_data_entry_search_bucket_external(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nikki')
		
		# Change company
		general_actions.change_company('NA Automation Company -- DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('QA_Test_Automation')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by bucket - 'External'
		data_entry_actions.search_pick_search_field('bucket', 'External')
	
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_bucket_external')

		
	# Verify that you can search Data Entry by Bucket - 'Internal' - ACCOUNT CHANGED
	def test_cc_data_entry_search_bucket_external(self):		
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Pat')
		
		# Change company
		general_actions.change_company('QA_Automation_Clark')
		
		# Change client
		general_actions.change_client('Bucket_Internal')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Verify count - Two documents, one internal
		data_entry_actions.verify_search_count(2)
		
		# Search by bucket - 'Internal'
		data_entry_actions.search_pick_search_field('bucket', 'Internal')
	
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_internal')

	
	# Verify that you can search Data Entry by Certificate ID - PERFECT
	def test_cc_data_entry_search_certificate_id(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by certificate id
		data_entry_actions.search_pick_search_field('certificate id', 7)
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_certid')
	
	
	# Verify that you can search Data Entry by Created Date - ACCOUNT CHANGED
	def test_cc_data_entry_search_created_date(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
	
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
	
		# Search by created date
		data_entry_actions.search_pick_search_field('created date', '2017-03-30')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		#Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_createdate')

		
	# Verify that you can search Data Entry by Customer Number - PERFECT
	def test_cc_data_entry_search_created_date(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by certificate id
		data_entry_actions.search_pick_search_field('customer number', 'cc00000001')
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_customer')
	
	
	# Verify that you can search Data Entry by Document Type 'Exicse' - ACCOUNT CHANGED
	def test_cc_data_entry_search_doc_type_excise(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nikki')
	
		# Change company
		general_actions.change_company('NA Automation Company -- DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('QA_Test_Automation')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document type - Which type of 'excise'?
		data_entry_actions.search_pick_search_field('document type', 'excise')
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_excise')
	
	# Verify that you can search Data Entry by Document Type 'Federal Withholding' - ACCOUNT CHANGED
	def test_cc_data_entry_search_doc_type_fed_with(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Nikki')
	
		# Change company
		general_actions.change_company('NA Automation Company -- DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('QA_Test_Automation')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document typ
		data_entry_actions.search_pick_search_field('document type', 'Federal Withholding')
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_fedwith')
	
	
	# Verify that you can search Data Entry by Document Type 'Federal Withholding' - ACCOUNT CHANGED
	def test_cc_data_entry_search_doc_type_fed_with_2(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Pat')
		
		# Change company
		general_actions.change_company('QA_Automation_Clark')
		
		# Change client
		general_actions.change_client('Data_Entry_DocType_FedWith')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document type
		data_entry_actions.search_pick_search_field('document type', 'Federal Withholding')
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_fedwith_2')
	
	
	# Verify that you can search Data Entry by Multiple Document Types - ACCOUNT CHANGED
	def test_cc_data_entry_search_doc_type_multi(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Pat')
		
		# Change company
		general_actions.change_company('QA_Automation_Clark')
		
		# Change client
		general_actions.change_client('Data_Entry_DocType_FedWith')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by multiple document types
		data_entry_actions.search_pick_search_field('document type list', ['Use Tax', 'Federal Withholding'])
	
		# Click search button
		data_entry_actions.click_search_button()
	
		# Sort by priority
		data_entry_actions.sort_search_results('priority')
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_multi_2b')
	
	
	# Verify that you can search Data Entry by Document Type 'Sales and Use' - ACCOUNT CHANGED
	def test_cc_data_entry_search_doc_type_sales_and_use_tax(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Pat')
		
		# Change company
		general_actions.change_company('QA_Automation_Clark')
		
		# Change client
		general_actions.change_client('Data_Entry_DocType_FedWith')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document type
		data_entry_actions.search_pick_search_field('document type', 'Use Tax')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_sales_2')
		
	
	# Verify that you can search Data Entry by Exempt Reason 'Resale' - PERFECT
	def test_cc_data_entry_search_exempt_reason(self):	
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document category
		data_entry_actions.search_pick_search_field('document category', 'RESALE')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_exempt')
	

	# Verify that you can search Data Entry by Exposure Zone - PERFECT
	def test_cc_data_entry_search_exposure_zone(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document category
		data_entry_actions.search_pick_search_field('exposure zone', 'Indiana')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_exposure')
		
		
	# Verify that you can search Data Entry by Filename - PERFECT
	def test_cc_data_entry_search_filename(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by document category
		data_entry_actions.search_pick_search_field('filename', 'blank_CA_BOE_230-D_Post.pdf')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_filename')	
		
	
	# Verify first button works correctly - PERFECT
	def test_cc_data_entry_search_first(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Verify 'next page' link
		data_entry_actions.verify_search_next()
		
		# Go to next page
		data_entry_actions.search_go_to_next()
		
		# Verify 'first page' link
		data_entry_actions.verify_search_first()
		
		# Go to first page
		data_entry_actions.search_go_to_first()
	
	
	# Verify that the 'last' link takes you to the last page - PERFECT
	def test_cc_data_entry_search_last(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Verify 'last page' link
		data_entry_actions.verify_search_last()
		
		# Go to last page
		data_entry_actions.search_go_to_last()
		
		# Verify results from rows 1 and 2
		rows = [1, 2]
		data_entry_actions.compare_results_with_row_numbers('hartley_auto', 'data_entry_search_last_2', rows)
	

	# Verify that you can search Data Entry by Location - ACCOUNT CHANGED
	def test_cc_data_entry_search_location(self):	
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by location
		data_entry_actions.search_pick_search_field('location', 'Joe NC')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_location')
	
	# Verify user can perform search using multiple fields - ACCOUNT CHANGED
	def test_cc_data_entry_search_multi_fields(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()

		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Pat')

		# Change company
		general_actions.change_company('QA_Automation_Clark')

		# Change client
		general_actions.change_client('Data_Entry')

		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()

		# Add multiple search parameters
		data_entry_actions.search_pick_search_field('exposure zone', 'Wyoming')	
		data_entry_actions.search_pick_search_field('priority', '2 - Normal')
		data_entry_actions.search_pick_search_field('document type', 'Sales and Use Tax')
		data_entry_actions.search_pick_search_field('stage', 'Ready For Validation')
		data_entry_actions.search_pick_search_field('source', 'CertExpress')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_multi_fields')
		
	
	# Verify that the 'next' link takes you to the next page - PERFECT
	def test_cc_data_entry_search_next(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Verify 'last page' link
		data_entry_actions.verify_search_next()
		
		# Go to last page
		data_entry_actions.search_go_to_next()
		
		# Verify results from rows 1 and 2
		rows = [1, 2]
		data_entry_actions.compare_results_with_row_numbers('hartley_auto', 'data_entry_search_next_2', rows)
		
	
	# Verify that the 'next' link takes you to the previous page - PERFECT
	def test_cc_data_entry_search_prev(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Go to next page
		data_entry_actions.search_go_to_next()
		
		# Go to prev page
		data_entry_actions.search_go_to_prev()
		
		# Verify results from rows 1 and 2
		rows = [1]
		data_entry_actions.compare_results_with_row_numbers('hartley_auto', 'data_entry_search_prev_2', rows)	
		
		
	
	# Verify that you can search Data Entry by Priority '1 - Low' - ACCOUNT CHANGED
	def test_cc_data_entry_search_priority_1(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by priority
		data_entry_actions.search_pick_search_field('priority', '1 - Low')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_priority')
	

	# Verify that you can search Data Entry by Priority '2 - Normal' - ACCOUNT CHANGED
	def test_cc_data_entry_search_priority_2(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by priority
		data_entry_actions.search_pick_search_field('priority', '2 - Normal')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_priority_2')
		
		
	# Verify that you can search Data Entry by Priority '3 - High' - ACCOUNT CHANGED
	def test_cc_data_entry_search_priority_3(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by priority
		data_entry_actions.search_pick_search_field('priority', '3 - High')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_priority_3')


	# Verify that you can search Data Entry by Priority '4 - Crtical' - ACCOUNT CHANGED
	def test_cc_data_entry_search_priority_4(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by priority
		data_entry_actions.search_pick_search_field('priority', '4 - Critical')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_priority_4')


	# Verify that you can search Data Entry by Source 'Public Wizard' - ACCOUNT CHANGED
	def test_cc_data_entry_search_source_pubwizard(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by source
		data_entry_actions.search_pick_search_field('source', 'Public Wizard')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Sort by certificate id
		data_entry_actions.sort_search_results('certificate id')
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_pubwiz')
		
		
	# Verify that you can search Data Entry by Source 'CertExpress' - ACCOUNT CHANGED
	def test_cc_data_entry_search_source_certexpress(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by source
		data_entry_actions.search_pick_search_field('source', 'CertExpress')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results - Existing bug causes test to fail
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_certexpress')
		
	
	# Verify that you can search Data Entry by Source 'Ecommerce Plugin' - ACCOUNT CHANGED
	def test_cc_data_entry_search_source_ecomm(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by source
		data_entry_actions.search_pick_search_field('source', 'Ecommerce Plugin')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_ecomm')	
		
		
	# Verify that you can search Data Entry by Source 'Retail' - ACCOUNT CHANGED
	def test_cc_data_entry_search_source_retail(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by source
		data_entry_actions.search_pick_search_field('source', 'Retail')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_retail')			
		

	# Verify that you can search Data Entry by Source 'Upload' - ACCOUNT CHANGED
	def test_cc_data_entry_search_source_upload(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Joe DataEntry')
		
		# Change company
		general_actions.change_company('JCAutomationCompany-DO NOT TOUCH')
		
		# Change client
		general_actions.change_client('Data Entry 1')
		
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by source
		data_entry_actions.search_pick_search_field('source', 'Upload')
		
		# Click search button
		data_entry_actions.click_search_button()
		
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_upload')			
	
	
	# Verify that you can search Data Entry by Stage 'Error: Re-Process Document' - PERFECT
	def test_cc_data_entry_search_stage_error_reprocess_document(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Error: Re-Process Document')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_re_process')
		
		
	# Verify that you can search Data Entry by Stage 'Failed To Process' - PERFECT
	def test_cc_data_entry_search_stage_failed_to_process_document(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Failed To Process')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_failed_process')

	
	# Verify that you can search Data Entry by Stage 'Ready For Merge' - PERFECT | Long test (~20 minutes, checks 57 search results)
	def test_cc_data_entry_search_stage_ready_for_merge(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Ready For Merge')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_merge')
	
	
	# Verify that you can search Data Entry by Stage 'Ready For Validation' - PERFECT
	def test_cc_data_entry_search_stage_ready_for_validation(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Ready For Validation')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_validation')
	
	
	# Verify that you can search Data Entry by Stage 'Ready For Validation (Escalated)' - PERFECT
	def test_cc_data_entry_search_stage_ready_for_validation_escalated(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Ready For Validation (Escalated)')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results - Use special function to account for adaptation of expected results
		data_entry_actions.ready_for_validation_compare_results('hartley_auto', 'data_entry_search_escalated')	


	# Verify that you can search Data Entry by Stage 'Reviewed' - PERFECT
	def test_cc_data_entry_search_stage_reviewed(self):
		# Open CertCapture
		capture_login_actions.capture_open_portal()
		
		# Login to CertCapture
		capture_login_actions.cc_login_from_google_sheet('Bob')
	
		# Navigate to Data Entry -> Validate Documents
		general_actions.go_to_validate_documents_page()
		
		# Search by stage
		data_entry_actions.search_pick_search_field('stage', 'Reviewed')
		
		# Click search button
		data_entry_actions.click_search_button()
	
		# Verify results
		data_entry_actions.compare_results('hartley_auto', 'data_entry_search_reviewed')	



		

		
		
		
def suite():
	suite = unittest.TestSuite()
	suite.addTest(Search('test_cc_data_entry_search_basic_search_0001'))
	#suite.addTest(Search('test_cc_data_entry_search_stage_reviewed'))
	return suite

if __name__ == '__main__':
	run_tests = unittest.TestSuite()
	run_tests.addTest(suite())
	result = unittest.TestResult()
	run_tests.run(result)
	print(result)
	print('Tests Run:', result.testsRun)
	print('Success?', result.wasSuccessful())








# ???













		