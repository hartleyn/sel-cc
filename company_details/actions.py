import general_actions.helpers as helpers
import company_details.locations as locations


'''
	Created by Nick Hartley
	3/13/18
'''


def click(target_name):
	target = target_name.lower()
	
	if target == 'company information':
		return helpers.click_helper(locations.Links.company_information_tab)
	elif target == 'company settings':
		return helpers.click_helper(locations.Links.company_settings_tab)
	elif target == 'retail settings':
		return helpers.click_helper(locations.Links.retail_settings_tab)
	elif target == 'certexpress settings':
		return helpers.click_helper(locations.Links.certexpress_settings_tab)
	elif target == 'retail purchaser settings':
		return helpers.click_helper(locations.Links.retail_purchaser_settings_tab)
	elif target == 'company fax emails':
		return helpers.click_helper(locations.Links.company_fax_emails_tab)
	elif target == 'edit company information':
		return helpers.click_helper(locations.CompanyInformationTab.Buttons.edit_client_information)
	elif target == 'edit company settings':
		return helpers.click_helper(locations.CompanySettingsTab.Buttons.edit_company_settings)
	elif target == 'edit retail settings':
		return helpers.click_helper(locations.RetailSettingsTab.Buttons.edit_retail_settings)
	elif target == 'edit certexpress settings':
		return helpers.click_helper(locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings)
	elif target == 'edit retail purchaser settings':
		return helpers.click_helper(locations.RetailPurchaserSettingsTabs.Buttons.edit_retail_purchaser_settings)
	elif target == 'manage company fax emails':
		return helpers.click_helper(locations.CompanyFaxEmails.Buttons.manage_company_fax_emails)
	else:
		print('Invalid target requested.')
		
def edit_company_information_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'name input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_name)
	elif target == 'legal name input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_legal_name)
	elif target == 'address line 1 input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_address_line_1)
	elif target == 'address line 2 input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_address_line_2)
	elif target == 'city input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_city)
	elif target == 'country select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_country)
	elif target == 'state select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_state)
	elif target == 'zip input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_zip)
	elif target == 'fein input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_fein)
	elif target == 'phone input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_phone)
	elif target == 'fax input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_fax)
	elif target == 'corporate email input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_corporate_email)
	elif target == 'notification emails input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_notification_emails)
	elif target == 'account lead select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_account_lead)
	elif target == 'equipment description input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_equipment_description)
	elif target == 'default bucket select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_default_bucket)		
	elif target == 'generated customer number prefix input':
		return helpers.click_helper(locations.CompanyInformationTab.Inputs.edit_company_information_modal_generated_customer_number_prefix)
	elif target == 'typeahead minimum search length select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_typeahead_minimum_search_length)	
	elif target == 'affidavit expiration select':
		return helpers.select_helper(locations.CompanyInformationTab.Selects.edit_company_information_modal_affidavit_expiration)
	elif target == 'update company information button':
		return helpers.click_helper(locations.CompanyInformationTab.Buttons.edit_company_information_modal_update_company_information)	
	elif target == 'cancel button':
		return helpers.click_helper(locations.CompanyInformationTab.Buttons.edit_company_information_modal_cancel)	
	elif target == 'close button':
		return helpers.click_helper(locations.CompanyInformationTab.Buttons.edit_company_information_modal_close)	
	else:
		print('Invalid target requested.')
		
def edit_company_settings_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'require tax input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_require_tax)
	elif target == 'allow jobs input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_allow_jobs)
	elif target == 'use document input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_documents)	
	elif target == 'use barcodes input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_barcodes)
	elif target == 'use managed input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_managed)
	elif target == 'collect sst input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_collect_sst)
	elif target == 'require sst input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_require_sst)
	elif target == 'hide title input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_hide_title)		
	elif target == 'use locations input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_locations)
	elif target == 'use location input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_location)
	elif target == 'allow requesters input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_allow_requesters)
	elif target == 'apply to input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_apply_to)
	elif target == 'remove non-nexus input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_remove_nonnexus)
	elif target == 'api access input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_api_access)
	elif target == 'force certexpress input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_force_certexpress)
	elif target == 'sso and input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_sso_and)
	elif target == 'use exposure input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_exposure)
	elif target == 'auto update input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_auto_update)
	elif target == 'set default input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_set_default)
	elif target == 'set default days field input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_set_default_days_field)
	elif target == 'public wizard input':
		return helpers.click_helper(locations.CompanySettingsTab.Inputs.edit_company_settings_modal_public_wizard)
	elif target == 'update company settings button':
		return helpers.click_helper(locations.CompanySettingsTab.Buttons.edit_company_settings_modal_update_company_settings)
	elif target == 'cancel button':
		return helpers.click_helper(locations.CompanySettingsTab.Buttons.edit_company_settings_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.CompanySettingsTab.Buttons.edit_company_settings_modal_close)
	else:
		print('Invalid target requested.')
		
def edit_retail_options_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'show pending input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_pending)
	elif target == 'show customers input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_customers)
	elif target == 'submit to input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_submit_to)
	elif target == 'append barcode input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_append_barcode)
	elif target == 'append certificate input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_append_certificate)
	elif target == 'disable upload input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_disable_upload)
	elif target == 'print/preview input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_print_preview)
	elif target == 'show certificate input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_certificate)
	elif target == 'upload only input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_upload_only)
	elif target == 'show historical input':
		return helpers.click_helper(locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_historical)
	elif target == 'update retail settings button':
		return helpers.click_helper(locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_update_retail_settings)
	elif target == 'cancel button':
		return helpers.click_helper(locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_close)
	else:
		print('Invalid target requested.')
		
def edit_certexpress_options_click(target_name):
	target = target_name.lower()
	
	if target == 'account expiration input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_account_expiration)
	elif target == 'edit purchaser input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_edit_purchaser)	
	elif target == 'submit to input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_submit_to)		
	elif target == 'upload document input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_upload_document)		
	elif target == 'print/preview input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_print_preview)		
	elif target == 'customer list input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_customer_list)		
	elif target == 'email dialog input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_email_dialog)		
	elif target == 'fax dialog input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_fax_dialog)		
	elif target == 'hide signature input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_hide_signature)		
	elif target == 'send certificate input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_send_certificate)		
	elif target == 'disable customer input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_disable_customer)		
	elif target == 'append barcode input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_append_barcode)		
	elif target == 'show certificate input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_show_certificate)		
	elif target == 'append certificate input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_append_certificate)		
	elif target == 'upload only input':
		return helpers.click_helper(locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_upload_only)
	elif target == 'update certexpress settings button':
		return helpers.click_helper(locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_update_certexpress_settings)
	elif target == 'cancel button':
		return helpers.click_helper(locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_close)
	else:
		print('Invalid target requested.')

def edit_retail_purchaser_options_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'address line 1 input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_address_line_1)
	elif target == 'address line 2 input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_address_line_2)
	elif target == 'city input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_city)
	elif target == 'contact name input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_contact_name)
	elif target == 'country input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_country)
	elif target == 'customer number input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_customer_number)
	elif target == 'email input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_email)
	elif target == 'name input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_name)
	elif target == 'phone input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_phone)
	elif target == 'state input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_state)
	elif target == 'zip input':
		return helpers.click_helper(locations.RetailPurchaserTab.Inputs.edit_retail_purchaser_settings_modal_zip)
	if target == 'address line 1 select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_address_line_1)
	elif target == 'address line 2 select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_address_line_2)
	elif target == 'city select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_city)
	elif target == 'contact name select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_contact_name)
	elif target == 'country select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_country)
	elif target == 'customer number select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_customer_number)
	elif target == 'email select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_email)
	elif target == 'name select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_name)
	elif target == 'phone select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_phone)
	elif target == 'state select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_state)
	elif target == 'zip select':
		return helpers.select_helper(locations.RetailPurchaserTab.Selects.edit_retail_purchaser_settings_modal_zip)
	elif target == 'update purchaser settings button':
		return helpers.click_helper(locations.RetailPurchaserTab.Buttons.edit_retail_purchaser_settings_modal_update_purchaser_settings)
	elif target == 'cancel button':
		return helpers.click_helper(locations.RetailPurchaserTab.Buttons.edit_retail_purchaser_settings_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.RetailPurchaserTab.Buttons.edit_retail_purchaser_settings_modal_close)
	else:
		print('Invalid target requested.')
		
def manage_company_fax_emails(target_name):
	target = target_name.lower()
	
	if target == 'fax email input':
		helpers.click_helper(locations.CompanyFaxEmailsTab.Inputs.manage_company_fax_emails_modal_fax_email)
	elif target == 'priority select':
		helpers.select_helper(locations.CompanyFaxEmailsTab.Selects.manage_company_fax_emails_modal_priority)
	elif target == 'bucket select':
		helpers.select_helper(locations.CompanyFaxEmailsTab.Selects.manage_company_fax_emails_modal_bucket)
	elif target == 'save button':
		helpers.click_helper(locations.CompanyFaxEmailsTab.Buttons.manage_company_fax_emails_modal_save)
	elif target == 'close button':
		helpers.click_helper(locations.CompanyFaxEmailsTab.Buttons.manage_company_fax_emails_modal_close)
	else:
		print('Invalid target requested.')
		
def toggle_retail_setting():
	click('company settings')
	time.sleep(2)
	click('edit company settings')
	time.sleep(2)
	edit_company_settings_modal_click('use locations input')
	
		
		
		
		
		
		
		