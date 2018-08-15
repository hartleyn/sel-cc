import os
import time
import unittest
import datetime
import general.helpers
import login.actions
import general.audits
import general.actions
import dashboard.actions
import campaigns.audits
import campaigns.actions
import bulk_print.actions
import bulk_delete.audits
import bulk_delete.actions
import bulk_import.actions
import add_customer.actions
import nexus_settings.audits
import nexus_settings.actions
import account_details.audits
import account_details.actions
import company_details.actions
import customer_search.audits
import customer_search.actions
import data_entry_sets.audits
import data_entry_sets.actions
import manage_accounts.audits
import manage_accounts.actions
import protractor_tests.audits
import validate_documents.actions
import public_certexpress.actions
import certificate_search.audits
import certificate_search.actions
import certificate_details.audits
import certificate_details.actions
import send_single_request.actions
import validate_documents.audits
from test_base import slash, browser, project_directory
from utilities.report_test_result import ReportTestResult

__author__ = 'Nick Hartley'
# 2/27/2018


class SmokeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nStarting smoke test on {}.\n'.format(browser.title()))
        print('\n************* TEST STARTING *************\n')

        # Open CertCapture
        login.actions.capture_open_portal()

        # Login
        # login.actions.cc_login_from_credentials_json('Nick')
        login.actions.okta_login('CertCapture.Beta3')

        # Change account
        general.actions.change_account('6_8_9_Smoke_Test_IE11')

        # Set 'Document Type' to 'Sales and Use Tax'
        # general.actions.change_document_type('sales and use tax')

    def setUp(self):
        print('Running a test.')

    @staticmethod
    def test_create_new_company():
        # Navigate to 'SysAdmin' -> 'Company Accounts'
        general.actions.click('Manage Accounts')

        # Click the 'Add Account' button
        manage_accounts.actions.click('Add Account Button')

        # Complete new account form
        manage_accounts.actions.complete_add_account_form('6_8_9_Smoke_Test_GC', '1 1st st', 'Building #2',
                                                           'North Babylon', 'New York', 'United States',
                                                           '10038', '555-555-5555')

        # Click the 'Add Account' button
        # manage_accounts.actions.add_account_modal_click('Add Account') - TODO - uncomment

        # Navigate to 'SysAdmin' -> 'Company Accounts' - if necessary
        # general.actions.click('Manage Accounts')

        # Verify that the account was created
        manage_accounts.audits.verify_account_exists('6_8_9_Smoke_Test_GC')

    @staticmethod
    def test_create_new_hierarchy():
        # Navigate to 'Settings' -> 'Account Settings' -> 'Account Details'
        general.actions.click('Account Details')

        # Click the 'Company Hierarchy' tab
        account_details.actions.tabs_click('Company Hierarchy')

        # Click the 'Add Company' button
        account_details.actions.company_hierarchy_tab_click('Add Company button')

        # Complete the new company form
        account_details.actions.complete_add_company_form('6_8_9_Smoke_Test_Co.', 'Legal test name', False,
                                                          '123 4th st', 'Big Box Building', 'Townsville',
                                                          'United States', 'Colorado', '90210', '646-867-5309')

        # Click the 'Add' button
        account_details.actions.add_company_modal_click('Add button')

        # Navigate to 'Settings' -> 'Account Settings' -> 'Account Details' - if necessary
        general.actions.click('Account Details')

        # Verify that the new company was created
        account_details.audits.verify_company_exists('6_8_9_Smoke_Test_Co.')

    @staticmethod
    def test_assign_all_states_in_nexus_settings():  # COMPLETE
        # Navigate to 'Content Library' -> 'Nexus Settings'
        general.actions.click('Nexus Settings')

        # Click the 'Assign Nexus' button
        nexus_settings.actions.click('Assign Nexus')

        # Click the 'Toggle Select All' checkbox
        nexus_settings.actions.us_edit_client_nexus_modal_click('Toggle Select All input')

        # Click the 'Update Client Nexus' button
        nexus_settings.actions.us_edit_client_nexus_modal_click('Update Client Nexus button')

        # Click the success modal - 'OK' button
        nexus_settings.actions.success_modal_click('ok button')

        # Verify that all states are assigned (Look for green checkmark)
        nexus_settings.audits.verify_all_states_assigned()

    @staticmethod # Must be in a dev account to access settings pages - COMPLETE? (waits) Use id_selected()
    def test_enable_public_wizard_and_retail():
        # Navigate to 'Settings' -> 'Account Settings' -> 'Account Details'
        general.actions.click('Account Details')

        # Navigate to the 'Features' tab
        account_details.actions.tabs_click('Features')

        # Check the 'Public Wizard' box
        account_details.actions.features_tab_click('Public Wizard input')
        time.sleep(5)
        # Navigate to 'Settings' -> 'Company Settings' -> 'Company Details'
        general.actions.click('Company Details')

        # Navigate to the 'Company Settings' tab
        company_details.actions.click('Company Settings')

        # Click the 'Edit Company Settings' button
        company_details.actions.click('edit company settings')

        # Click the 'Use Locations' checkbox
        company_details.actions.edit_company_settings_modal_click('Use Locations checkbox input')
        time.sleep(5)
        # Click the 'Update Company Settings' button
        company_details.actions.edit_company_settings_modal_click('Update Company Settings button')

        # Click success modal - 'OK' button
        company_details.actions.success_modal_click('ok button')

        # Verify that 'Public Wizard' and 'Retail' are enabled
        general.audits.verify_enabled_public_certexpress_and_retail()

    @staticmethod
    def test_bulk_import_customers():  # COMPLETE
        # Navigate to 'Customers' -> 'Bulk Import'
        general.actions.click('Import Customers')

        # Call customer bulk import function - file must be in the test_assets directory
        # bulk_import.actions.import_customers_from_file('import_mock_data.xlsx')

        # Navigate to 'Search' -> 'Customer Search'
        general.actions.click('Customer Search')

        # Verify that customers were uploaded - Verification could be more extensive...
        customer_search.audits.verify_customers_imported('import_mock_data.xlsx')

    @staticmethod
    def test_send_single_request_protractor():  # Still has a few bugs -_-
        run = True
        if run:
            # Navigate to 'Manage Documents' -> 'Send Single Request'
            general.actions.click('Send Single Request')

            # Select a customer to send a request
            send_single_request.actions.click('customer search input', select='cc00000034')
            # general.helpers.single_request_recipient_click_or_select('cc1')

            # Select 'All Document Types' from the document type dropdown
            send_single_request.actions.click('document type select', select='All Document Types')

            # Select exposure zone(s)
            zones = ['state', 'arizona']
            send_single_request.actions.select_exposure_zones(zones)

            # Select exempt reason(s)
            reasons = ['agriculture']
            send_single_request.actions.select_exempt_reasons(reasons)
            print('clicking templates select all link')
            # Click the templates "Select All' link
            send_single_request.actions.click('templates select all link')

            # Set delivery method
            send_single_request.actions.click('delivery method select', select='Download')

            # Set 'Cover Letter' field
            send_single_request.actions.click('cover letter select', select='STANDARD_REQUEST')

            # Set return date
            send_single_request.actions.click('return date input', date='2018-08-04')  # Clear values

            # Click the 'Send Request' button
            send_single_request.actions.click('generate request button')

            # Navigate to the dashboard
            general.actions.click('Dashboard')

            # Wait and download request PDF
            dashboard.actions.wait_for_download_center_job('Single Request Bundle for Customer # cc00000034')

            # Store request code in JSON file
            send_single_request.actions.store_request_url_in_json()

            # Run protractor test - Create a certificate from request code
            os.chdir('C:{0}users{0}nick.hartley{0}desktop{0}auto{0}protractor_tests'.format(slash))
            os.system('protractor protractor.conf.js')

            # Parse protractor test report - TODO - change filename/location
            protractor_tests.audits.parse_protractor_test_report('example.json')

            # Click 'Manage Documents' -> 'Validate Documents'
            general.actions.click('Validate Documents')

            # Set up document search
            validate_documents.actions.set_up_search_for_document(source='CertExpress', stage='Ready For Validation')

            # Click 'Search'
            validate_documents.actions.click('search button')

            # Verify that certificate was created
            validate_documents.audits.verify_certexpress_certificate_creation('cc00000024')

            # Click "Ready For Validation" certificate
            validate_documents.actions.click('results row 1 link')

            # Click never expire button
            validate_documents.actions.validate_document_window_click('never expire button')

            # Validate certificate
            validate_documents.actions.validate_document_window_click('validate button')

            # Close 'Success!' modal
            validate_documents.actions.validate_document_window_click('success ok button')

        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        # import datetime
        certificate_search.actions.certificate_criteria_click('certificate created date begin input', text='2018-06-07')

        certificate_search.actions.click('customer criteria link')

        certificate_search.actions.customer_criteria_click('customer numbers input', text='cc00000024')

        certificate_search.actions.click('get search results button')

        # Verify that certificate is valid
        certificate_search.audits.verify_certexpress_certificate_validation('Arizona', 'AGRICULTURE')

    @staticmethod
    def test_create_and_complete_campaign_protractor():
        run = True
        if run:
            # Navigate to 'Search' -> 'Customer Search'
            general.actions.click('Customer Search')

            # Click the 'Customer Numbers' field and type numbers
            customer_search.actions.customer_criteria_click('customer numbers input', text='cc00000039')

            # Click the 'Get Search Results' button
            customer_search.actions.click('get search results button')

            # Click the 'Perform Actions On Results' dropdown and select 'New Campaign' from dropdown
            customer_search.actions.results_page_click('perform actions on results select', select='New Campaign')

            # Set Up Campaign
            campaigns.actions.set_up_campaign('New Test 5', 'Sales and Use Tax', ['Agriculture'])

            # Click the 'Prepare exemption certificate Campaign' button
            campaigns.actions.set_up_campaign_click('prepare campaign button')

            # Set up 'Scheduling & Delivery' tab - USE POSTAL MAIL AND THEN DOWNLOAD, DUMMY
            campaigns.actions.set_up_scheduling_and_delivery('2018-06-08', '2018-06-09', 'Postal Mail', 'STANDARD_REQUEST')

            # Click the 'Save Campaign Changes' button
            campaigns.actions.edit_campaign_click('save campaign changes button')

            # Click 'Print'
            campaigns.actions.edit_campaign_click('print link')

            # Select 'PDF - 1 Merged File'
            campaigns.actions.edit_campaign_click('pdf - 1 merged file input')

            # Click the 'Create Printable File' button
            campaigns.actions.edit_campaign_click('create printable file button')

            # Navigate to 'Dashboard'
            general.actions.click('Dashboard')

            # Wait and download PDF
            dashboard.actions.wait_for_campaign_round_download_job('New Test 5')

            # Store request codes (and maybe exposure zones?)
            campaigns.actions.store_request_links_in_json()

            # Run protractor test
            os.chdir('C:{0}users{0}nick.hartley{0}desktop{0}auto{0}protractor_tests'.format(slash))
            os.system('protractor test.conf.js')

        # Parse protractor test result
        protractor_tests.audits.parse_protractor_test_report('example.json')

        # Navigate to 'Manage Documents' -> 'Campaigns'
        general.actions.click('Campaigns')

        # Find and click in-progress campaigns
        campaigns.actions.find_and_click_in_progress_campaign('New Test 5')

        # Verify campaign completion
        campaigns.audits.verify_campaign_completion()

    @staticmethod
    def test_upload_document_in_data_entry():
        # Click 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        run = True
        if run:
            # Click 'Upload Document' button
            validate_documents.actions.click('upload document button')

            # Set up document upload
            validate_documents.actions.set_up_document_upload(
                '{0}{1}test_assets{1}1017274_auto_1883.pdf'.format(project_directory, slash),
                'Sales and Use Tax', 'Arizona', 'Agriculture')  # Fix 'Arizona' v. 'Arizona Sales Tax' issue

            # Click 'Upload Stack' button
            validate_documents.actions.upload_document_modal_click('upload stack button')
            time.sleep(10)  # Wait for processing

        # Set up search
        validate_documents.actions.set_up_search_for_document(stage='Ready For Merge', source='Upload')
        #time.sleep(5)
        # Click 'search' button
        validate_documents.actions.click('search button')
        #time.sleep(10)
        # Verify that document was uploaded
        validate_documents.audits.verify_document_upload('1017274_auto_1883.pdf', 'Arizona', 'Ready For Merge', 'Upload', '0')  # Check that certificate was uploaded

    @staticmethod
    def test_validate_certificate_in_data_entry():
        # Click 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Wait for upload processing
        # time.sleep(15)

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Merge" certificate
        validate_documents.actions.click('results row 1 link')

        # Merge certificate
        validate_documents.actions.merge_document_window_click('submit button')

        # Close 'Successful Merge' modal
        validate_documents.actions.merge_document_window_click('successful merge close button')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(source='Upload', stage='Ready For Merge')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        # Set up validation (Add Customer in Validation)
        validate_documents.actions.set_up_document_validation('cc00000011')

        # Validate certificate
        validate_documents.actions.validate_document_window_click('validate button')

        # Close 'Success!' modal
        validate_documents.actions.validate_document_window_click('success ok button')

        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        certificate_search.actions.certificate_criteria_click('certificate created date begin input', text=str(datetime.date.today()))

        certificate_search.actions.certificate_criteria_click('certificate is valid select',
                                                              select='Yes')

        certificate_search.actions.certificate_criteria_click('status input', select='COMPLETE')

        certificate_search.actions.click('customer criteria link')

        certificate_search.actions.customer_criteria_click('customer numbers input', text='cc00000011')

        certificate_search.actions.click('get search results button')

        # Verify that certificate is valid
        certificate_search.audits.verify_certificate_validation('Arizona', 'AGRICULTURE', str(datetime.date.today()), 'cc00000011')

    @staticmethod
    def test_escalate_document_in_data_entry():
        # Click 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Click 'Upload Document' button
        validate_documents.actions.click('upload document button')

        # Set up document upload
        validate_documents.actions.set_up_document_upload(
            '{0}{1}test_assets{1}1017274_auto_1883.pdf'.format(project_directory, slash),
            'Sales and Use Tax', 'Arizona', 'Agriculture')  # Fix 'Arizona' v. 'Arizona Sales Tax' issue

        # Click 'Upload Stack' button
        validate_documents.actions.upload_document_modal_click('upload stack button')
        time.sleep(10)  # Wait for processing

        # Set up search
        validate_documents.actions.set_up_search_for_document(stage='Ready For Merge', source='Upload')

        # Click 'search' button
        validate_documents.actions.click('search button')

        # Click "Ready For Merge" certificate
        validate_documents.actions.click('results row 1 link')

        # Click 'submit' button
        validate_documents.actions.merge_document_window_click('submit button')

        # Click confirmation 'close' button
        validate_documents.actions.merge_document_window_click('successful merge close button')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(stage='Ready For Validation', source='Upload')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        # Escalate certificate
        validate_documents.actions.validate_document_window_click('escalate button')

        # Escalate certificate
        validate_documents.actions.validate_document_window_click('escalate escalate button')

        # Close success modal
        validate_documents.actions.validate_document_window_click('success ok button')

        # Set up search
        validate_documents.actions.set_up_search_for_document(stage='Ready For Validation (Escalated)')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Verify that certificate was escalated
        validate_documents.audits.verify_certificate_escalation()

    @staticmethod
    def test_data_entry_sets():
        zones = ['California', 'Colorado', 'North Carolina', 'New York', 'Washington']
        run = False
        if run:
            # Click 'Settings' -> 'Company Settings' -> 'Data Entry Sets'
            general.actions.click('Data Entry Sets')

            # Click 'Add Data Entry Set'
            data_entry_sets.actions.click('add data entry set button')

            # Set up new data entry set
            # zones = ['California', 'Colorado', 'North Carolina', 'New York', 'Washington']
            data_entry_sets.actions.set_up_new_data_entry_set('data entry set test!', zones)

            # Click the 'Add' button
            data_entry_sets.actions.add_data_entry_set_modal_click('add button')

        # Navigate to 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(None, False, stage='Ready For Validation')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        # Click exposure zone clear button
        validate_documents.actions.validate_document_window_click('clear button')

        # Data entry set
        validate_documents.actions.validate_document_window_click('exposure zones input', select='test')

        # Verify that data entry set was created
        data_entry_sets.audits.verify_data_entry_set(zones)

    @staticmethod
    def test_create_a_certificate_public_certexpress():
        # Navigate to 'Settings' -> 'Company Settings' -> 'Public CertExpress'
        general.actions.click('Public CertExpress')

        # Retrieve and store 'Public CertExpress' link
        public_certexpress.actions.store_public_certexpress_link_in_json()

        # Run protractor test - Create a document
        os.system('protractor C:{0}users{0}nick.hartley{0}desktop{0}cucumber'
                  '{0}protractor-cucumber-framework-example{0}test.conf.js'.format(slash))

        # Parse protractor test report
        protractor_tests.audits.parse_protractor_test_report('example.json')

        # Navigate to 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(None, False, source='Public Wizard')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        certificate_id = validate_documents.actions.get_certificate_id()

        validate_documents.actions.set_up_document_validation('1')

        # Validate certificate
        validate_documents.actions.validate_document_window_click('validate button')
        time.sleep(2)
        # Close 'Success!' modal
        validate_documents.actions.validate_document_window_click('success ok button')
        time.sleep(2)

        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        certificate_search.actions.certificate_criteria_click('certificate created date begin input',
                                                              text=str(datetime.date.today()))

        certificate_search.actions.certificate_criteria_click('certificate ids input', text=certificate_id)

        certificate_search.actions.click('get search results button')

        certificate_search.actions.results_page_click('results row 1 link')

        certificate_details.audits.verify_status_complete()

        certificate_details.actions.click('validation link')

        # Verify that certificate was created
        certificate_details.audits.verify_certificate_validation()

    @staticmethod
    def test_create_multi_zone_certificate():  # WORKS :)
        zones = ['California', 'Colorado', 'North Carolina', 'New York', 'Washington']

        run = False
        if run:
            # Navigate to 'Customers' -> 'Add Customer'
            general.actions.click('Add Customer')

            add_customer.actions.set_up_add_new_customer('multi_zone_cert_customer', 'Multi Zone Cert Customer', '6462225678', 'test@user.com', '1 1st st', 'Raleigh', 'North Carolina', '27617')

            add_customer.actions.click('add new customer button')

            # Click 'Manage Documents' -> 'Validate Documents'
            general.actions.click('Validate Documents')

            # Set up document search
            validate_documents.actions.set_up_search_for_document(None, False, stage='Ready For Validation')

            # Click 'Search'
            validate_documents.actions.click('search button')

            # Click "Ready For Validation" certificate
            validate_documents.actions.click('results row 1 link')

            # Select a customer
            # validate_documents.actions.validate_document_window_click('customers input', select='3')
            # time.sleep(2)
            # Select 'Drop Ship - SST' exposure zone
            validate_documents.actions.validate_document_window_click('exposure zones input', select='test')
            time.sleep(2)

            # Set up SST validation
            validate_documents.actions.set_up_sst_validation('multi_zone_cert_customer')

            # Validate certificate
            validate_documents.actions.validate_document_window_click('validate button')
            time.sleep(2)
            # Close 'Success!' modal
            validate_documents.actions.validate_document_window_click('success ok button')
            time.sleep(2)

        # Navigate to 'Search' -> 'Customer Search'
        general.actions.click('Customer Search')

        # Verify that multi-zone certificate is valid
        customer_search.actions.customer_criteria_click('customer numbers input', text='multi_zone_cert_customer')

        # Click 'Get Search Results' button
        customer_search.actions.click('get search results button')

        # Verify multi-zone certificate
        customer_search.audits.verify_multi_zone_certificate(zones)

    @staticmethod
    def test_create_a_certificate_through_retail():
        # Account set up
        pass

        # Run protractor test - create through retail
        os.system('protractor C:{0}users{0}nick.hartley{0}desktop{0}cucumber'
                  '{0}protractor-cucumber-framework-example{0}retail.conf.js'.format(slash))

        # Parse protractor test report
        protractor_tests.audits.parse_protractor_test_report('retail-test.json')

        # Navigate to 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(None, False, source='Retail')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        certificate_id = validate_documents.actions.get_certificate_id()

        validate_documents.actions.set_up_document_validation('1')

        # Validate certificate
        validate_documents.actions.validate_document_window_click('validate button')
        time.sleep(2)
        # Close 'Success!' modal
        validate_documents.actions.validate_document_window_click('success ok button')
        time.sleep(2)

        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        certificate_search.actions.certificate_criteria_click('certificate ids input', text=certificate_id)

        certificate_search.actions.click('get search results button')

        certificate_search.actions.results_page_click('results row 1 link')

        certificate_details.audits.verify_status_complete()

        certificate_details.actions.click('validation link')

        # Verify that certificate was created
        certificate_details.audits.verify_certificate_validation()

    # @staticmethod
    # def test_create_a_certificate_through_guest_certexpress():  # Might not need? - Can cover this scenario in SSR
        # pass

    @staticmethod
    def test_create_a_certificate_while_logged_in_certexpress():
        # Run protractor test - create while logged in
        os.system('protractor C:{0}users{0}nick.hartley{0}desktop{0}cucumber'
                  '{0}protractor-cucumber-framework-example{0}test.conf.js'.format(slash))

        # Parse protractor test
        protractor_tests.audits.parse_protractor_test_report('example.json')

        # Navigate to 'Manage Documents' -> 'Validate Documents'
        general.actions.click('Validate Documents')

        # Set up document search
        validate_documents.actions.set_up_search_for_document(None, False, source='CertExpress')

        # Click 'Search'
        validate_documents.actions.click('search button')

        # Click "Ready For Validation" certificate
        validate_documents.actions.click('results row 1 link')

        certificate_id = validate_documents.actions.get_certificate_id()

        validate_documents.actions.set_up_document_validation('1')

        # Validate certificate
        validate_documents.actions.validate_document_window_click('validate button')
        time.sleep(2)
        # Close 'Success!' modal
        validate_documents.actions.validate_document_window_click('success ok button')
        time.sleep(2)

        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        certificate_search.actions.certificate_criteria_click('certificate ids input', text=certificate_id)

        certificate_search.actions.click('get search results button')

        certificate_search.actions.results_page_click('results row 1 link')

        certificate_details.audits.verify_status_complete()

        certificate_details.actions.click('validation link')

        # Verify that certificate was created
        certificate_details.audits.verify_certificate_validation()

    @staticmethod
    def test_bulk_print():
        # Navigate to 'Search' -> 'Certificate Search'
        general.actions.click('Certificate Search')

        # Execute a search
        certificate_search.actions.click('get search results button')

        # Select 'Bulk Print Certificates' from the 'Perform Actions...' dropdown
        certificate_search.actions.results_page_click('perform actions on results select',
                                                      select='Bulk Print Certificates')

        # Set up bulk print
        bulk_print.actions.click('title input', text='A Bulk Print Test!')

        # Click 'Create Print Job'
        bulk_print.actions.click('create print job button')

        # Navigate to 'Dashboard'
        general.actions.click('Dashboard')

        first_pdf = general.helpers.get_latest_pdf()

        # Click 'Download Center' bulk print download link
        dashboard.actions.wait_for_download_center_job('A Bulk Print Test!')

        # Verify bulk print
        general.audits.verify_bulk_print(first_pdf)

    @staticmethod
    def test_bulk_delete_customers():
        general.actions.click('Customer Search')

        customer_search.actions.click('get search results button')

        search_results_count = customer_search.actions.get_search_results_count()

        # Navigate to 'Customers' -> 'Delete Multiple Customers'
        general.actions.click('Delete Multiple Customers')

        # Choose file
        bulk_delete.actions.delete_customers_from_file('import_mock_data.xlsx')

        # Verify deletion
        bulk_delete.audits.verify_bulk_delete(search_results_count)


def suite():
    test_suite = unittest.TestSuite()

    # test_suite.addTest(SmokeTest('test_create_new_company'))
    # test_suite.addTest(SmokeTest('test_create_new_hierarchy'))
    test_suite.addTest(SmokeTest('test_assign_all_states_in_nexus_settings'))
    test_suite.addTest(SmokeTest('test_enable_public_wizard_and_retail'))
    test_suite.addTest(SmokeTest('test_bulk_import_customers'))
    test_suite.addTest(SmokeTest('test_send_single_request_protractor'))
    test_suite.addTest(SmokeTest('test_create_and_complete_campaign_protractor'))
    test_suite.addTest(SmokeTest('test_upload_document_in_data_entry'))
    test_suite.addTest(SmokeTest('test_validate_certificate_in_data_entry'))
    test_suite.addTest(SmokeTest('test_escalate_document_in_data_entry'))
    test_suite.addTest(SmokeTest('test_data_entry_sets'))
    test_suite.addTest(SmokeTest('test_create_a_certificate_public_certexpress'))
    test_suite.addTest(SmokeTest('test_create_multi_zone_certificate'))
    test_suite.addTest(SmokeTest('test_create_a_certificate_through_retail'))
    test_suite.addTest(SmokeTest('test_create_a_certificate_while_logged_in_certexpress'))
    test_suite.addTest(SmokeTest('test_bulk_print'))
    test_suite.addTest(SmokeTest('test_bulk_delete_customers'))

    return test_suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner(resultclass=ReportTestResult)
    runner = unittest.TextTestRunner()
    runner.run(suite())
