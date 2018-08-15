import time
from general import helpers
from company_details import locations
from utilities import warnings as warn

__author__ = 'Nick Hartley'
# 3/13/18


def click(target_name):
    target = target_name.lower()

    if target == 'company information':
        helpers.click_helper(locations.Links.company_information_tab)
    elif target == 'company settings':
        helpers.click_helper(locations.Links.company_settings_tab)
    elif target == 'retail settings':
        helpers.click_helper(locations.Links.retail_settings_tab)
    elif target == 'certexpress settings':
        helpers.click_helper(locations.Links.certexpress_settings_tab)
    elif target == 'retail purchaser settings':
        helpers.click_helper(locations.Links.retail_purchaser_settings_tab)
    elif target == 'company fax emails':
        helpers.click_helper(locations.Links.company_fax_emails_tab)
    elif target == 'edit company information':
        helpers.click_helper(locations.CompanyInformationTab.Buttons.edit_company_information)
    elif target == 'edit company settings':
        helpers.click_helper(locations.CompanySettingsTab.Buttons.edit_company_settings)
    elif target == 'edit retail settings':
        helpers.click_helper(locations.RetailSettingsTab.Buttons.edit_retail_settings)
    elif target == 'edit certexpress settings':
        helpers.click_helper(locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings)
    elif target == 'edit retail purchaser settings':
        helpers.click_helper(locations.RetailPurchaserSettingsTab.Buttons.edit_retail_purchaser_settings)
    elif target == 'manage company fax emails':
        helpers.click_helper(locations.CompanyFaxEmailsTab.Buttons.manage_company_fax_emails)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_company_information_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'name input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'legal name input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_legal_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_city
        helpers.click_or_type(location, **kwargs)
    elif target == 'country select':
        location = locations.CompanyInformationTab.Selects.edit_company_information_modal_country
        helpers.click_or_select(location, **kwargs)
    elif target == 'state select':
        location = locations.CompanyInformationTab.Selects.edit_company_information_modal_state
        helpers.click_or_select(location, **kwargs)
    elif target == 'zip input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'fein input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_fein
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_phone
        helpers.click_or_type(location, **kwargs)
    elif target == 'fax input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_fax
        helpers.click_or_type(location, **kwargs)
    elif target == 'corporate email input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_corporate_email
        helpers.click_or_type(location, **kwargs)
    elif target == 'notification emails input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_notification_emails
        helpers.click_or_type(location, **kwargs)
    elif target == 'account lead select':
        location = locations.CompanyInformationTab.Selects.edit_company_information_modal_account_lead
        helpers.click_or_select(location, **kwargs)
    elif target == 'equipment description input':
        location = locations.CompanyInformationTab.Inputs.edit_company_information_modal_equipment_description
        helpers.click_or_type(location, **kwargs)
    elif target == 'default bucket select':
        location = locations.CompanyInformationTab.Selects.edit_company_information_modal_default_bucket
        helpers.click_or_select(location, **kwargs)
    elif target == 'generated customer number prefix input':
        location = locations\
            .CompanyInformationTab.Inputs.edit_company_information_modal_generated_customer_number_prefix
        helpers.click_or_type(location, **kwargs)
    elif target == 'typeahead minimum search length select':
        location = locations\
            .CompanyInformationTab.Selects.edit_company_information_modal_typeahead_minimum_search_length
        helpers.click_or_select(location, **kwargs)
    elif target == 'affidavit expiration select':
        location = locations.CompanyInformationTab.Selects.edit_company_information_modal_affidavit_expiration
        helpers.click_or_select(location, **kwargs)
    elif target == 'update company information button':
        location = locations.CompanyInformationTab.Buttons.edit_company_information_modal_update_company_information
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CompanyInformationTab.Buttons.edit_company_information_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CompanyInformationTab.Buttons.edit_company_information_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_company_settings_modal_click(target_name):
    target = target_name.lower()

    if target == 'require tax checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_require_tax
        helpers.click_helper(location)
    elif target == 'allow jobs checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_allow_jobs
        helpers.click_helper(location)
    elif target == 'use document checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_documents
        helpers.click_helper(location)
    elif target == 'use barcodes checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_barcodes
        helpers.click_helper(location)
    elif target == 'use managed checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_managed
        helpers.click_helper(location)
    elif target == 'collect sst checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_collect_sst
        helpers.click_helper(location)
    elif target == 'require sst checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_require_sst
        helpers.click_helper(location)
    elif target == 'hide title checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_hide_title
        helpers.click_helper(location)
    elif target == 'use locations checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_locations
        helpers.click_helper(location)
    elif target == 'use location checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_location
        helpers.click_helper(location)
    elif target == 'allow requesters checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_allow_requesters
        helpers.click_helper(location)
    elif target == 'apply to checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_apply_to
        helpers.click_helper(location)
    elif target == 'remove non-nexus checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_remove_nonnexus
        helpers.click_helper(location)
    elif target == 'api access checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_api_access
        helpers.click_helper(location)
    elif target == 'force certexpress checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_force_certexpress
        helpers.click_helper(location)
    elif target == 'sso and checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_sso_and
        helpers.click_helper(location)
    elif target == 'use exposure checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_use_exposure
        helpers.click_helper(location)
    elif target == 'auto update checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_auto_update
        helpers.click_helper(location)
    elif target == 'set default checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_set_default
        helpers.click_helper(location)
    elif target == 'set default days field checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_set_default_days_field
        helpers.click_helper(location)
    elif target == 'public wizard checkbox input':
        location = locations.CompanySettingsTab.Inputs.edit_company_settings_modal_public_wizard
        helpers.click_helper(location)
    elif target == 'update company settings button':
        location = locations.CompanySettingsTab.Buttons.edit_company_settings_modal_update_company_settings
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CompanySettingsTab.Buttons.edit_company_settings_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CompanySettingsTab.Buttons.edit_company_settings_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_retail_options_modal_click(target_name):
    target = target_name.lower()

    if target == 'show pending checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_pending
        helpers.click_helper(location)
    elif target == 'show customers checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_customers
        helpers.click_helper(location)
    elif target == 'submit to checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_submit_to
        helpers.click_helper(location)
    elif target == 'append barcode checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_append_barcode
        helpers.click_helper(location)
    elif target == 'append certificate checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_append_certificate
        helpers.click_helper(location)
    elif target == 'disable upload checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_disable_upload
        helpers.click_helper(location)
    elif target == 'print/preview checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_print_preview
        helpers.click_helper(location)
    elif target == 'show certificate checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_certificate
        helpers.click_helper(location)
    elif target == 'upload only checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_upload_only
        helpers.click_helper(location)
    elif target == 'show historical checkbox input':
        location = locations.RetailSettingsTab.Inputs.edit_retail_settings_modal_show_historical
        helpers.click_helper(location)
    elif target == 'update retail settings button':
        location = locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_update_retail_settings
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.RetailSettingsTab.Buttons.edit_retail_settings_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_certexpress_options_click(target_name):
    target = target_name.lower()

    if target == 'account expiration input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_account_expiration
        helpers.click_helper(location)
    elif target == 'edit purchaser checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_edit_purchaser
        helpers.click_helper(location)
    elif target == 'submit to checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_submit_to
        helpers.click_helper(location)
    elif target == 'upload document checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_upload_document
        helpers.click_helper(location)
    elif target == 'print/preview checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_print_preview
        helpers.click_helper(location)
    elif target == 'customer list checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_customer_list
        helpers.click_helper(location)
    elif target == 'email dialog checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_email_dialog
        helpers.click_helper(location)
    elif target == 'fax dialog checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_fax_dialog
        helpers.click_helper(location)
    elif target == 'hide signature checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_hide_signature
        helpers.click_helper(location)
    elif target == 'send certificate checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_send_certificate
        helpers.click_helper(location)
    elif target == 'disable customer checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_disable_customer
        helpers.click_helper(location)
    elif target == 'append barcode checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_append_barcode
        helpers.click_helper(location)
    elif target == 'show certificate checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_show_certificate
        helpers.click_helper(location)
    elif target == 'append certificate checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_append_certificate
        helpers.click_helper(location)
    elif target == 'upload only checkbox input':
        location = locations.CertExpressSettingsTab.Inputs.edit_certexpress_settings_modal_upload_only
        helpers.click_helper(location)
    elif target == 'update certexpress settings button':
        location = locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_update_certexpress_settings
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CertExpressSettingsTab.Buttons.edit_certexpress_settings_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_retail_purchaser_options_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'address line 1 checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_address_line_2
        helpers.click_helper(location)
    elif target == 'city checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_city
        helpers.click_helper(location)
    elif target == 'contact name checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_contact_name
        helpers.click_helper(location)
    elif target == 'country checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_country
        helpers.click_helper(location)
    elif target == 'customer number checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_customer_number
        helpers.click_helper(location)
    elif target == 'email checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_email
        helpers.click_helper(location)
    elif target == 'name checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_name
        helpers.click_helper(location)
    elif target == 'phone checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_phone
        helpers.click_helper(location)
    elif target == 'state checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_state
        helpers.click_helper(location)
    elif target == 'zip checkbox input':
        location = locations.RetailPurchaserSettingsTab.Inputs.edit_retail_purchaser_settings_modal_zip
        helpers.click_helper(location)
    if target == 'address line 1 select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_address_line_1
        helpers.click_or_select(location)
    elif target == 'address line 2 select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_address_line_2
        helpers.click_or_select(location)
    elif target == 'city select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_city
        helpers.click_or_select(location)
    elif target == 'contact name select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_contact_name
        helpers.click_or_select(location)
    elif target == 'country select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_country
        helpers.click_or_select(location)
    elif target == 'customer number select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_customer_number
        helpers.click_or_select(location)
    elif target == 'email select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_email
        helpers.click_or_select(location)
    elif target == 'name select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_name
        helpers.click_or_select(location)
    elif target == 'phone select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_phone
        helpers.click_or_select(location)
    elif target == 'state select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_state
        helpers.click_or_select(location)
    elif target == 'zip select':
        location = locations.RetailPurchaserSettingsTab.Selects.edit_retail_purchaser_settings_modal_zip
        helpers.click_or_select(location)
    elif target == 'update purchaser settings button':
        location = locations\
            .RetailPurchaserSettingsTab.Buttons.edit_retail_purchaser_settings_modal_update_purchaser_settings
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.RetailPurchaserSettingsTab.Buttons.edit_retail_purchaser_settings_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.RetailPurchaserSettingsTab.Buttons.edit_retail_purchaser_settings_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def manage_company_fax_emails(target_name, **kwargs):
    target = target_name.lower()

    if target == 'fax email input':
        location = locations.CompanyFaxEmailsTab.Inputs.manage_company_fax_emails_modal_fax_email
        helpers.click_or_type(location, **kwargs)
    elif target == 'priority select':
        location = locations.CompanyFaxEmailsTab.Selects.manage_company_fax_emails_modal_priority
        helpers.click_or_select(location, **kwargs)
    elif target == 'bucket select':
        location = locations.CompanyFaxEmailsTab.Selects.manage_company_fax_emails_modal_bucket
        helpers.click_or_select(location, **kwargs)
    elif target == 'save button':
        location = locations.CompanyFaxEmailsTab.Buttons.manage_company_fax_emails_modal_save
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CompanyFaxEmailsTab.Buttons.manage_company_fax_emails_modal_close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def success_modal_click(target_name):
    target = target_name.lower()

    if target == 'ok button':
        helpers.click_helper(locations.SuccessModal.Buttons.ok)
    elif target == 'x button' or target == 'close button':
        helpers.click_helper(locations.SuccessModal.Buttons.close)
    else:
        print(warn.INVALID_CLICK_TARGET)


def toggle_retail_setting():
    click('company settings')
    time.sleep(2)
    click('edit company settings')
    time.sleep(2)
    edit_company_settings_modal_click('use locations input')
