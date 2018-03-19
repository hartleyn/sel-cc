
'''
	Created by Nick Hartley
	3/13/18
'''

class Links:
	company_information_tab = '//*[@id="customer_tab"]/li[1]/a'
	company_settings_tab = '//*[@id="customer_tab"]/li[2]/a'
	retail_settings_tab = '//*[@id="customer_tab"]/li[3]/a'
	certexpress_settings_tab = '//*[@id="customer_tab"]/li[4]/a'
	retail_purchaser_settings_tab = '//*[@id="customer_tab"]/li[5]/a'
	company_fax_emails_tab = '//*[@id="customer_tab"]/li[6]/a'

	
class CompanyInformationTab:
	class Buttons:
		edit_company_information = '//*[@id="client_information"]/div/div[1]/div/a' # Actually a link
		edit_company_information_modal_close = '//div[@id="edit_client_entity_modal"]/div/div/div/button'
		edit_company_information_modal_update_company_information = '//div[@id="edit_client_entity_modal"]/div/div/div[3]/button'
		edit_company_information_modal_cancel = '//div[@id="edit_client_entity_modal"]/div/div/div[3]/button[2]'
		
	class Inputs:
		edit_company_information_modal_name = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input'
		edit_company_information_modal_legal_name = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[2]'
		edit_company_information_modal_address_line_1 = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[3]'
		edit_company_information_modal_address_line_2 = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[4]'
		edit_company_information_modal_city = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[5]'
		edit_company_information_modal_zip = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[6]'
		edit_company_information_modal_fein = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[7]'
		edit_company_information_modal_phone = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[8]'
		edit_company_information_modal_fax = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[9]'
		edit_company_information_modal_corporate_email = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[10]'
		edit_company_information_modal_notification_emails = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[11]'
		edit_company_information_modal_equipment_description = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[12]'
		edit_company_information_modal_generated_customer_number_prefix = '//[@id="edit_client_entity_modal"]/div/div/div[2]/div/div/input[13]'
	
	class Selects:
		edit_company_information_modal_country = '//*[@id="edit_client_country"]'
		edit_company_information_modal_state = '//*[@id="edit_client_state"]'
		edit_company_information_modal_account_lead = '//*[@id="edit_client_project_manager"]'
		edit_company_information_modal_default_bucket = '//*[@id="edit_client_bucket_id"]'
		edit_company_information_modal_typeahead_minimum_search_length = '//*[@id="edit_client_typeahead_minlength"]'
		edit_company_information_modal_affidavit_expiration = '//*[@id="edit_client_affidavit"]'
	
	
class CompanySettingsTab:
	class Buttons:
		edit_company_settings = '//*[@id="edit_client_options"]' # Actually a link
		edit_company_settings_modal_close = '//div[@id="edit_client_entity_options_modal"]/div/div/div/button'
		edit_company_settings_modal_update_company_settings = '//div[@id="edit_client_entity_options_modal"]/div/div/div[3]/button'
		edit_company_settings_modal_cancel = '//div[@id="edit_client_entity_options_modal"]/div/div/div[3]/button[2]'
		
	class Inputs:
		edit_company_settings_modal_require_tax = '//form[@id="client_options_form"]/div/div/input'
		edit_company_settings_modal_allow_jobs = '//form[@id="client_options_form"]/div[2]/div/input'
		edit_company_settings_modal_use_documents = '//form[@id="client_options_form"]/div[3]/div/input'
		edit_company_settings_modal_use_barcodes = '//form[@id="client_options_form"]/div[4]/div/input'
		edit_company_settings_modal_use_managed = '//form[@id="client_options_form"]/div[5]/div/input'
		edit_company_settings_modal_collect_sst = '//form[@id="client_options_form"]/div[6]/div/input'
		edit_company_settings_modal_require_sst = '//form[@id="client_options_form"]/div[7]/div/input'
		edit_company_settings_modal_hide_title = '//form[@id="client_options_form"]/div[8]/div/input'
		edit_company_settings_modal_use_locations = '//form[@id="client_options_form"]/div[9]/div/input'
		edit_company_settings_modal_use_location = '//form[@id="client_options_form"]/div[10]/div/input'
		edit_company_settings_modal_allow_requesters = '//form[@id="client_options_form"]/div[11]/div/input'
		edit_company_settings_modal_apply_to = '//form[@id="client_options_form"]/div[12]/div/input'
		edit_company_settings_modal_remove_nonnexus = '//form[@id="client_options_form"]/div[13]/div/input'
		edit_company_settings_modal_api_access = '//form[@id="client_options_form"]/div[14]/div/input'
		edit_company_settings_modal_force_certexpress = '//form[@id="client_options_form"]/div[15]/div/input'
		edit_company_settings_modal_sso_and = '//form[@id="client_options_form"]/div[16]/div/input'
		edit_company_settings_modal_use_exposure = '//form[@id="client_options_form"]/div[17]/div/input'
		edit_company_settings_modal_auto_update = '//form[@id="client_options_form"]/div[18]/div/input'
		edit_company_settings_modal_set_default = '//form[@id="client_options_form"]/div[19]/div/input'
		edit_company_settings_modal_set_default_days_field = '//form[@id="client_options_form"]/div[19]/div[2]/input'
		edit_company_settings_modal_public_wizard = '//form[@id="client_options_form"]/div[20]/div/input'
	
	
class RetailSettingsTab:
	class Buttons:
		edit_retail_settings = '//*[@id="retail_additional_options"]/div/div[1]/div/a' # Actually a link
		edit_retail_settings_modal_close = '//*[@id="edit_retail_options_modal"]/div/div/div[1]/button'
		edit_retail_settings_modal_update_retail_settings = '//*[@id="edit_retail_option"]'
		edit_retail_settings_modal_cancel = '//*[@id="edit_retail_options_modal"]/div/div/div[3]/button[2]'
		
	class Inputs:
		edit_retail_settings_modal_show_pending = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[2]/div/input'
		edit_retail_settings_modal_show_customers = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[3]/div/input'
		edit_retail_settings_modal_submit_to = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[4]/div/input'
		edit_retail_settings_modal_append_barcode = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[5]/div/input'
		edit_retail_settings_modal_append_certificate = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[6]/div/input'
		edit_retail_settings_modal_disable_upload = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[7]/div/input'
		edit_retail_settings_modal_print_preview = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[8]/div/input'
		edit_retail_settings_modal_show_certificate = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[9]/div/input'
		edit_retail_settings_modal_upload_only = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[10]/div/input'
		edit_retail_settings_modal_show_historical = '//div[@id="edit_retail_options_modal"]/div/div/div[2]/div/div/form/div[11]/div/input'
	
	
class CertExpressSettingsTab:
	class Buttons:
		edit_certexpress_settings = '//*[@id="webportal_options"]/div/div[1]/div/a' # Actually a link
		edit_certexpress_settings_modal_close = '//div[@id="edit_portal_options_modal"]/div/div/div/button'
		edit_certexpress_settings_modal_update_certexpress_settings = '//div[@id="edit_portal_options_modal"]/div/div/div[3]/button'
		edit_certexpress_settings_modal_cancel = '//div[@id="edit_portal_options_modal"]/div/div/div[3]/button[2]'
		
	class Inputs:
		edit_certexpress_settings_modal_account_expiration = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div/div/input'
		edit_certexpress_settings_modal_edit_purchaser = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[2]/div/input'
		edit_certexpress_settings_modal_submit_to = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[3]/div/input'
		edit_certexpress_settings_modal_upload_document = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[4]/div/input'
		edit_certexpress_settings_modal_print_preview = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[5]/div/input'
		edit_certexpress_settings_modal_customer_list = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[6]/div/input'
		edit_certexpress_settings_modal_email_dialog = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[7]/div/input'
		edit_certexpress_settings_modal_fax_dialog = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[8]/div/input'
		edit_certexpress_settings_modal_hide_signature = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[9]/div/input'
		edit_certexpress_settings_modal_send_certificate = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[10]/div/input'
		edit_certexpress_settings_modal_disable_customer = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[11]/div/input'
		edit_certexpress_settings_modal_append_barcode = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[12]/div/input'
		edit_certexpress_settings_modal_show_certificate = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[13]/div/input'
		edit_certexpress_settings_modal_append_certificate = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[14]/div/input'
		edit_certexpress_settings_modal_upload_only = '//div[@id="edit_portal_options_modal"]/div/div/div[2]/div/div/form/div[15]/div/input'
	
	
class RetailPurchaserTab:
	class Buttons:
		edit_retail_purchaser_settings = '//*[@id="edit_purchaser_options"]/div/div[2]/div/a' # Actually a link
		edit_retail_purchaser_settings_modal_close = '//div[@id="edit_purchaser_options_modal"]/div/div/div/button'
		edit_retail_purchaser_settings_modal_update_purchaser_settings = '//div[@id="edit_purchaser_options_modal"]/div/div/div[3]/button'
		edit_retail_purchaser_settings_modal_cancel = '//div[@id="edit_purchaser_options_modal"]/div/div/div[3]/button[2]'
		
	class Inputs:
		edit_retail_purchaser_settings_modal_address_line_1 = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_address_line_2 = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[2]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_city = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[3]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_contact_name = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[4]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_country = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[5]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_customer_number = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[6]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_email = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[7]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_name = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[8]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_phone = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[9]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_state = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[10]/tbody/tr[2]/td/input'
		edit_retail_purchaser_settings_modal_zip = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[11]/tbody/tr[2]/td/input'
		
	class Selects:
		edit_retail_purchaser_settings_modal_address_line_1 = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_address_line_2 = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[2]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_city = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[3]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_contact_name = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[4]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_country = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[5]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_customer_number = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[6]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_email = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[7]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_name = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[8]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_phone = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[9]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_state = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[10]/tbody/tr[2]/td[2]/select'
		edit_retail_purchaser_settings_modal_zip = '//div[@id="edit_purchaser_options_modal"]/div/div/div[2]/div/div/form/table[11]/tbody/tr[2]/td[2]/select'
		
		
class CompanyFaxEmailsTab:
	class Buttons:
		manage_company_fax_emails = '//button[@id="manage_fax_emails"]'
		manage_company_fax_emails_modal_close = '//*[@id="manage_client_fax_modal"]/div/div/div[1]/button'
		manage_company_fax_emails_modal_save = '//*[@id="btn_add_fax_email"]'
		
	class Inputs:
		manage_company_fax_emails_modal_fax_email = '//*[@id="fax_email_address"]'
		
	class Selects:
		manage_company_fax_emails_modal_priority = '//*[@id="priority"]'
		manage_company_fax_emails_modal_bucket = '//*[@id="bucket"]'
		
