from test_base import driver
import utilities.warnings as warn
import general.helpers as helpers
import customer_search.locations as locations

__author__ = 'Nick Hartley'
# 3/27/2018


def click(target_name):
    target = target_name.lower()

    if target == 'basic button':
        helpers.click_helper(locations.Buttons.basic)
    elif target == 'advanced button':
        helpers.click_helper(locations.Buttons.advanced)
    elif target == 'get search results button':
        helpers.click_helper(locations.Buttons.get_search_results)
    elif target == 'search config button' or target == 'search configuration button':
        helpers.click_helper(locations.Buttons.search_config)
    elif target == 'customer criteria link':
        helpers.click_helper(locations.Links.customer_criteria)
    elif target == 'customer attributes link':
        helpers.click_helper(locations.Links.customer_attributes)
    elif target == 'certificate criteria link':
        helpers.click_helper(locations.Links.document_criteria)
    elif target == 'exempt reasons override link':
        helpers.click_helper(locations.Links.document_category_override)
    elif target == 'certificate attributes link':
        helpers.click_helper(locations.Links.document_attributes)
    elif target == 'customer exempt/exposure reasons link':
        helpers.click_helper(locations.Links.customer_document_categories)
    elif target == 'customer bill/ship information link':
        helpers.click_helper(locations.Links.customer_bill_ship_information)
    elif target == 'certificate exempt/exposure reasons link':
        helpers.click_helper(locations.Links.document_categories)
    elif target == 'certificate invalid reasons link':
        helpers.click_helper(locations.Links.document_invalid_reasons)
    elif target == 'campaign criteria link':
        helpers.click_helper(locations.Links.campaign_criteria)
    elif target == 'clear search criteria link':
        helpers.click_helper(locations.Links.clear_search_criteria)
    else:
        print(warn.INVALID_CLICK_TARGET)


def customer_criteria_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer numbers input':
        location = locations.CustomerCriteria.Inputs.customer_numbers
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.CustomerCriteria.Inputs.address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.CustomerCriteria.Inputs.address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone number input':
        location = locations.CustomerCriteria.Inputs.phone_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact name input':
        location = locations.CustomerCriteria.Inputs.contact_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'alternate id input' or target == 'custom id input':
        location = locations.CustomerCriteria.Inputs.alternate_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'customer name input':
        location = locations.CustomerCriteria.Inputs.customer_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'state input':
        location = locations.CustomerCriteria.Inputs.state
        helpers.state_input_field_click_or_select(location, **kwargs)
    elif target == 'fein input':
        location = locations.CustomerCriteria.Inputs.fein
        helpers.click_or_type(location, **kwargs)
    elif target == 'tax number input':
        location = locations.CustomerCriteria.Inputs.tax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.CustomerCriteria.Inputs.city
        helpers.click_or_type(location, **kwargs)
    elif target == 'zip input':
        location = locations.CustomerCriteria.Inputs.zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'fax number input':
        location = locations.CustomerCriteria.Inputs.fax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact email input':
        location = locations.CustomerCriteria.Inputs.contact_email
        helpers.click_or_type(location, **kwargs)
    elif target == 'create date start input':
        location = locations.CustomerCriteria.Inputs.customer_created_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'create date end input':
        location = locations.CustomerCriteria.Inputs.customer_created_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'create date ago input':
        location = locations.CustomerCriteria.Inputs.customer_created_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'create date to input':
        location = locations.CustomerCriteria.Inputs.customer_created_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'modified date start input':
        location = locations.CustomerCriteria.Inputs.customer_modified_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'modified date end input':
        location = locations.CustomerCriteria.Inputs.customer_modified_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'modified date ago input':
        location = locations.CustomerCriteria.Inputs.customer_modified_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'modified date to input':
        location = locations.CustomerCriteria.Inputs.customer_modified_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction start input':
        location = locations.CustomerCriteria.Inputs.last_transaction_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction end input':
        location = locations.CustomerCriteria.Inputs.last_transaction_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction ago input':
        location = locations.CustomerCriteria.Inputs.last_transaction_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction to input':
        location = locations.CustomerCriteria.Inputs.last_transaction_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'state select':
        location = locations.CustomerCriteria.Selects.state
        helpers.click_or_select(location, **kwargs)
    elif target == 'fatca reporting code select':
        location = locations.CustomerCriteria.Selects.fatca_reporting_code
        helpers.click_or_select(location, **kwargs)
    elif target == 'exempt payee code select':
        location = locations.CustomerCriteria.Selects.exempt_payee_code
        helpers.click_or_select(location, **kwargs)
    elif target == 'taxpayer identification type select':
        location = locations.CustomerCriteria.Selects.taxpayer_identification_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'tax classification select':
        location = locations.CustomerCriteria.Selects.tax_classification
        helpers.click_or_select(location, **kwargs)
    elif target == 'withhold back up taxes select':
        location = locations.CustomerCriteria.Selects.withhold_back_up_taxes
        helpers.click_or_select(location, **kwargs)
    elif target[-27:] == 'completed for a corporation select':
        location = locations.CustomerCriteria.Selects.completed_for_a_corporation
        helpers.click_or_select(location, **kwargs)
    elif target == 'llc tax classification select':
        location = locations.CustomerCriteria.Selects.llc_tax_classification
        helpers.click_or_select(location, **kwargs)
    elif target == 'create date select':
        location = locations.CustomerCriteria.Selects.create_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'modified date select':
        location = locations.CustomerCriteria.Selects.modified_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'last transaction date select':
        location = locations.CustomerCriteria.Selects.last_transaction_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'state add all button':
        location = locations.CustomerCriteria.Buttons.state_add_all
        helpers.click_helper(location)
    elif target == 'state remove all button':
        location = locations.CustomerCriteria.Buttons.state_remove_all
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def customer_attributes_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer has attributes input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_has_attributes)
    elif target == 'customer does not have attributes input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_does_not_have_attributes)
    elif target == 'attribute added date start input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_attributes_date_begin)
    elif target == 'attribute added date end input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_attributes_date_end)
    elif target == 'attribute added date ago input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_attributes_days_ago)
    elif target == 'attribute added date to input':
        helpers.click_helper(locations.CustomerAttributes.Inputs.customer_attributes_days_to)
    elif target == 'customer has any all attributes select':
        location = locations.CustomerAttributes.Selects.customer_has_any_all_attributes
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer has attributes select':
        location = locations.CustomerAttributes.Selects.customer_has_attributes
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer does not have any all attributes select':
        location = locations.CustomerAttributes.Selects.customer_does_not_have_any_all_attributes
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer does not have attributes select':
        location = locations.CustomerAttributes.Selects.customer_does_not_have_attributes
        helpers.click_or_select(location, **kwargs)
    elif target == 'between dates select':
        location = locations.CustomerAttributes.Selects.between_dates
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer has attributes add all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_has_attributes_add_all)
    elif target == 'customer has attributes remove all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_has_attributes_remove_all)
    elif target == 'customer does not have attributes add all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_does_not_have_attributes_add_all)
    elif target == 'customer does not have attributes remove all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_does_not_have_attributes_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def certificate_criteria_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate ids input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_ids)
    elif target == 'status input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.status)
    elif target == 'document type input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.document_type)
    elif target == 'exposure zone input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.exposure_zone)
    elif target == 'exempt percent input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.exempt_percent)
    elif target == 'po number input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.po_number)
    elif target == 'tax number input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.tax_number)
    elif target == 'certificate created date begin input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_created_date_begin)
    elif target == 'certificate created date end input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_created_date_end)
    elif target == 'certificate created date ago input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_created_days_ago)
    elif target == 'certificate created date to input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_created_days_to)
    elif target == 'certificate modified date begin input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_modified_date_begin)
    elif target == 'certificate modified date end input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_modified_date_end)
    elif target == 'certificate modified date ago input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_modified_days_ago)
    elif target == 'certificate modified date to input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_modified_days_to)
    elif target == 'certificate signed date begin input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_signed_date_begin)
    elif target == 'certificate signed date end input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_signed_date_end)
    elif target == 'certificate signed date ago input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_signed_days_ago)
    elif target == 'certificate signed date to input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_signed_days_to)
    elif target == 'certificate expiration date begin input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_expiration_date_begin)
    elif target == 'certificate expiration date end input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_expiration_date_end)
    elif target == 'certificate expiration date ago input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_expiration_days_ago)
    elif target == 'certificate expiration date to input':
        helpers.click_helper(locations.CertificateCriteria.Inputs.certificate_expiration_days_to)
    elif target == 'has certificates select':
        location = locations.CertificateCriteria.Selects.has_certificate
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate is valid select':
        location = locations.CertificateCriteria.Selects.certificate_is_valid
        helpers.click_or_select(location, **kwargs)
    elif target == 'status select':
        location = locations.CertificateCriteria.Selects.status
        helpers.click_or_select(location, **kwargs)
    elif target == 'document type select':
        location = locations.CertificateCriteria.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'exposure zone select':
        location = locations.CertificateCriteria.Selects.exposure_zone
        helpers.click_or_select(location, **kwargs)
    elif target == 'expired select':
        location = locations.CertificateCriteria.Selects.expired
        helpers.click_or_select(location, **kwargs)
    elif target == 'link type select':
        location = locations.CertificateCriteria.Selects.link_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'is single select':
        location = locations.CertificateCriteria.Selects.is_single
        helpers.click_or_select(location, **kwargs)
    elif target == 'has api error select':
        location = locations.CertificateCriteria.Selects.has_api_error
        helpers.click_or_select(location, **kwargs)
    elif target == 'create date select':
        location = locations.CertificateCriteria.Selects.create_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'modified date select':
        location = locations.CertificateCriteria.Selects.modified_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'effective date select':
        location = locations.CertificateCriteria.Selects.effective_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'expiration date select':
        location = locations.CertificateCriteria.Selects.expiration_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'expiration date days ago days from now select':
        location = locations.CertificateCriteria.Selects.expiration_date_days_ago_days_from_now
        helpers.click_or_select(location, **kwargs)
    elif target == 'status add all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.status_add_all)
    elif target == 'status remove all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.status_remove_all)
    elif target == 'document type add all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.document_type_add_all)
    elif target == 'document type remove all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.document_type_remove_all)
    elif target == 'exposure zone add all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.exposure_zone_add_all)
    elif target == 'exposure zone remove all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.exposure_zone_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def exempt_reason_override_click(target_name):
    target = target_name.lower()

    if target == 'override reason in exposure zones input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_reason_in_exposure_zones)
    elif target == 'override has documented reasons input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_has_documented_reasons)
    elif target == 'override created date begin input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_created_date_begin)
    elif target == 'override created date end input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_created_date_end)
    elif target == 'override created date ago input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_created_days_ago)
    elif target == 'override created date to input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_created_days_to)
    elif target == 'override effective date begin input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_effective_date_begin)
    elif target == 'override effective date end input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_effective_date_end)
    elif target == 'override effective date ago input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_effective_days_ago)
    elif target == 'override effective date to input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_effective_days_to)
    elif target == 'override expiration date begin input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_expiration_date_begin)
    elif target == 'override expiration date end input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_expiration_date_end)
    elif target == 'override expiration date ago input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_expiration_days_ago)
    elif target == 'override expiration date to input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.override_expiration_days_to)
    elif target == 'license number input':
        helpers.click_helper(locations.ExemptReasonOverride.Inputs.license_number)
    elif target == 'override reason in any all exposure zones select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.override_reason_in_any_all_exposure_zones)
    elif target == 'override reason in exposure zones select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.override_reason_in_exposure_zones)
    elif target == 'override has any all documented reasons select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.override_has_any_all_documented_reasons)
    elif target == 'override has documented reasons select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.override_has_documented_reasons)
    elif target == 'create date select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.create_date)
    elif target == 'effective date select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.effective_date)
    elif target == 'expiration date select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.expiration_date)
    elif target == 'effective date days ago days from now select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.effective_date_days_ago_days_from_now)
    elif target == 'expiration date days ago days from now select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.expiration_date_days_ago_days_from_now)
    elif target == 'create date select':
        helpers.click_helper(locations.ExemptReasonOverride.Selects.create_date)
    elif target == 'override reason in exposure zones add all button':
        helpers.click_helper(locations.ExemptReasonOverride.Buttons.override_reason_in_exposure_zones_add_all)
    elif target == 'override reason in exposure zones remove all button':
        helpers.click_helper(locations.ExemptReasonOverride.Buttons.override_reason_in_exposure_zones_remove_all)
    elif target == 'override has documented reasons add all button':
        helpers.click_helper(locations.ExemptReasonOverride.Buttons.override_has_documented_reasons_add_all)
    elif target == 'override has documented reasons remove all button':
        helpers.click_helper(locations.ExemptReasonOverride.Buttons.override_has_documented_reasons_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def certificate_attributes_click(target_name):
    target = target_name.lower()

    if target == 'customer has attributes input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.customer_has_attributes)
    elif target == 'customer does not have attributes input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.customer_does_not_have_attributes)
    elif target == 'certificate attributes date begin input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.certificate_attributes_date_begin)
    elif target == 'certificate attributes date end input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.certificate_attributes_date_end)
    elif target == 'certificate attributes date ago input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.certificate_attributes_days_ago)
    elif target == 'certificate attributes date to input':
        helpers.click_helper(locations.CertificateAttributes.Inputs.certificate_attributes_days_to)
    elif target == 'customer has any all attributes select':
        helpers.click_helper(locations.CertificateAttributes.Selects.customer_has_any_all_attributes)
    elif target == 'customer has attributes select':
        helpers.click_helper(locations.CertificateAttributes.Selects.customer_has_attributes)
    elif target == 'customer does not have any all attributes select':
        helpers.click_helper(locations.CertificateAttributes.Selects.customer_does_not_have_any_all_attributes)
    elif target == 'customer does not have attributes select':
        helpers.click_helper(locations.CertificateAttributes.Selects.customer_does_not_have_attributes)
    elif target == 'attribute added date select':
        helpers.click_helper(locations.CertificateAttributes.Selects.attribute_added_date)
    elif target == 'certificate has attributes add all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_has_attributes_add_all)
    elif target == 'certificate has attributes remove all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_has_attributes_remove_all)
    elif target == 'certificate does not have attributes add all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_does_not_have_attributes_add_all)
    elif target == 'certificate does not have attributes remove all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_does_not_have_attributes_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def customer_exempt_exposure_reasons_click(target_name):
    target = target_name.lower()

    if target == 'customer reason in exposure zones input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_reason_in_exposure_zones)
    elif target == 'customer has documented reasons input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_has_documented_reasons)
    elif target == 'customer does not have documented reasons input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_does_not_have_documented_reasons)
    elif target == 'customer has expected reasons input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_has_expected_reasons)
    elif target == 'customer does not have expected reasons input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_does_not_have_expected_reasons)
    elif target == 'reason modified date begin input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_date_begin)
    elif target == 'reason modified date end input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_date_end)
    elif target == 'reason modified date ago input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_days_ago)
    elif target == 'reason modified date to input':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_days_to)
    elif target == 'customer reason in any all exposure zones select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_reason_in_any_all_exposure_zones)
    elif target == 'customer reason in exposure zones select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_reason_in_exposure_zones)
    elif target == 'customer has any all documented reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_has_any_all_documented_reasons)
    elif target == 'customer has documented reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_has_documented_reasons)
    elif target == 'customer does not have any all documented reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_any_all_documented_reasons)
    elif target == 'customer does not have documented reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_documented_reasons)
    elif target == 'customer has any all expected reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_has_any_all_expected_reasons)
    elif target == 'customer has expected reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_has_expected_reasons)
    elif target == 'customer does not have any all expected reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_any_all_expected_reasons)
    elif target == 'customer does not have expected reasons select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_expected_reasons)
    elif target == 'reason modified date select':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Selects.reason_modified_date)
    elif target == 'customer reason in exposure zones add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_reason_in_exposure_zones_add_all)
    elif target == 'customer reason in exposure zones remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_reason_in_exposure_zones_remove_all)
    elif target == 'customer has documented reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_documented_reasons_add_all)
    elif target == 'customer has documented reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_documented_reasons_remove_all)
    elif target == 'customer does not have documented reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_documented_reasons_add_all)
    elif target == 'customer does not have documented reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_documented_reasons_remove_all)
    elif target == 'customer has expected reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_expected_reasons_add_all)
    elif target == 'customer has expected reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_expected_reasons_remove_all)
    elif target == 'customer does not have expected reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_expected_reasons_add_all)
    elif target == 'customer does not have expected reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_expected_reasons_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def customer_bill_ship_information_click(target_name):
    target = target_name.lower()

    if target == 'bill customer numbers input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.bill_customer_numbers)
    elif target == 'ship customer numbers input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.ship_customer_numbers)
    elif target == 'customer has bill ship types input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.customer_has_bill_ship_types)
    elif target == 'customer bills to states provinces input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.customer_bills_to_states_provinces)
    elif target == 'customer ships to states provinces input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.customer_ships_to_states_provinces)
    elif target == 'bill alternate id input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.bill_alternate_id)
    elif target == 'bill customer name input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.bill_customer_name)
    elif target == 'bill customer state input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.bill_customer_state)
    elif target == 'ship alternate id input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.ship_alternate_id)
    elif target == 'ship customer name input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.ship_customer_name)
    elif target == 'ship customer state input':
        helpers.click_helper(locations.CustomerBillShipInformation.Inputs.ship_customer_state)
    elif target == 'customer has any all bill ship types select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_has_any_all_bill_ship_types)
    elif target == 'customer has bill ship types select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_has_bill_ship_types)
    elif target == 'customer bills to any all states provinces select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_bills_to_any_all_states_provinces)
    elif target == 'customer bills to states provinces select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_bills_to_states_provinces)
    elif target == 'customer ships to any all states provinces select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_ships_to_any_all_states_provinces)
    elif target == 'customer ships to states provinces select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.customer_ships_to_states_provinces)
    elif target == 'bill customer state select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.bill_customer_state)
    elif target == 'ship customer state select':
        helpers.click_helper(locations.CustomerBillShipInformation.Selects.ship_customer_state)
    elif target == 'customer has bill ship types add all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_has_bill_ship_types_add_all)
    elif target == 'customer has bill ship types remove all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_has_bill_ship_types_remove_all)
    elif target == 'customer bills to states provinces add all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_bills_to_states_provinces_add_all)
    elif target == 'customer bills to states provinces remove all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_bills_to_states_provinces_remove_all)
    elif target == 'customer ships to states provinces add all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_ships_to_states_provinces_add_all)
    elif target == 'customer ships to states provinces remove all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.customer_ships_to_states_provinces_remove_all)
    elif target == 'bill customer state add all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.bill_customer_state_add_all)
    elif target == 'bill customer state remove all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.bill_customer_state_remove_all)
    elif target == 'ship customer state add all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.ship_customer_state_add_all)
    elif target == 'ship customer state remove all button':
        helpers.click_helper(locations.CustomerBillShipInformation.Buttons.ship_customer_state_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def certificate_exempt_exposure_reasons_click(target_name):
    target = target_name.lower()

    if target == 'certificate reason in exposure zones input':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Inputs.certificate_reason_in_exposure_zones)
    elif target == 'certificate has documented reasons input':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Inputs.certificate_has_documented_reasons)
    elif target == 'certificate does not have documented reasons input':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Inputs.certificate_does_not_have_documented_reasons)
    elif target == 'certificate has expected reasons input':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Inputs.certificate_has_expected_reasons)
    elif target == 'certificate does not have expected reasons input':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Inputs.certificate_does_not_have_expected_reasons)
    elif target == 'certificate reason in any all exposure zones select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_reason_in_any_all_exposure_zones)
    elif target == 'certificate reason in exposure zones select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_reason_in_exposure_zones)
    elif target == 'certificate reason has any all documented reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_has_any_all_documented_reasons)
    elif target == 'certificate reason has documented reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_has_documented_reasons)
    elif target == 'certificate reason does not have any all documented reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_any_all_documented_reasons)
    elif target == 'certificate reason does not have documented reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_documented_reasons)
    elif target == 'certificate reason has any all expected reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_has_any_all_expected_reasons)
    elif target == 'certificate reason has expected reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_has_expected_reasons)
    elif target == 'certificate reason does not have any all expected reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_any_all_documented_reasons)
    elif target == 'certificate reason does not have expected reasons select':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_expected_reasons)
    elif target == 'certificate reason in exposure zones add all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_reason_in_exposure_zones_add_all)
    elif target == 'certificate reason in exposure zones remove all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_reason_in_exposure_zones_remove_all)
    elif target == 'certificate has documented reasons add all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_has_documented_reasons_add_all)
    elif target == 'certificate has documented reasons remove all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_has_documented_reasons_remove_all)
    elif target == 'certificate does not have documented reasons add all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_documented_reasons_add_all)
    elif target == 'certificate does not have documented reasons remove all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_documented_reasons_remove_all)
    elif target == 'certificate has expected reasons add all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_has_expected_reasons_add_all)
    elif target == 'certificate has expected reasons remove all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_has_expected_reasons_remove_all)
    elif target == 'certificate does not have expected reasons add all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_expected_reasons_add_all)
    elif target == 'certificate does not have expected reasons remove all button':
        helpers.click_helper(locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_expected_reasons_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def certificate_invalid_reasons_click(target_name):
    target = target_name.lower()

    if target == 'certificate has invalid reasons input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_has_invalid_reasons)
    elif target == 'certificate does not have invalid reasons input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_does_not_have_invalid_reasons)
    elif target == 'certificate invalid reasons date begin input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_date_begin)
    elif target == 'certificate invalid reasons date end input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_date_end)
    elif target == 'certificate invalid reasons date ago input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_days_ago)
    elif target == 'certificate invalid reasons date to input':
        helpers.click_helper(locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_days_to)
    elif target == 'certificate has any all invalid reasons select':
        helpers.click_helper(locations.CertificateInvalidReasons.Selects.certificate_has_any_all_invalid_reasons)
    elif target == 'certificate has invalid reasons select':
        helpers.click_helper(locations.CertificateInvalidReasons.Selects.certificate_has_invalid_reasons)
    elif target == 'certificate does not have any all invalid reasons select':
        helpers.click_helper(locations.CertificateInvalidReasons.Selects.certificate_does_not_have_any_all_invalid_reasons)
    elif target == 'certificate does not have invalid reasons select':
        helpers.click_helper(locations.CertificateInvalidReasons.Selects.certificate_does_not_have_invalid_reasons)
    elif target == 'reason added date select':
        helpers.click_helper(locations.CertificateInvalidReasons.Selects.reason_added_date)
    elif target == 'certificate has invalid reasons add all button':
        helpers.click_helper(locations.CertificateInvalidReasons.Buttons.certificate_has_invalid_reasons_add_all)
    elif target == 'certificate has invalid reasons remove all button':
        helpers.click_helper(locations.CertificateInvalidReasons.Buttons.certificate_has_invalid_reasons_remove_all)
    elif target == 'certificate does not have invalid reasons add all button':
        helpers.click_helper(locations.CertificateInvalidReasons.Buttons.certificate_does_not_have_invalid_reasons_add_all)
    elif target == 'certificate does not have invalid reasons remove all button':
        helpers.click_helper(locations.CertificateInvalidReasons.Buttons.certificate_does_not_have_invalid_reasons_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def campaign_criteria_click(target_name):
    target = target_name.lower()

    if target == 'campaign name input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_name)
    elif target == 'campaign status input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_status)
    elif target == 'campaign request date begin input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_request_date_begin)
    elif target == 'campaign request date end input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_request_date_end)
    elif target == 'campaign request date ago input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_request_days_ago)
    elif target == 'campaign request date to input':
        helpers.click_helper(locations.CampaignCriteria.Inputs.campaign_request_days_to)
    elif target == 'customer status select':
        helpers.click_helper(locations.CampaignCriteria.Selects.customer_status)
    elif target == 'campaign name select':
        helpers.click_helper(locations.CampaignCriteria.Selects.campaign_name)
    elif target == 'campaign status select':
        helpers.click_helper(locations.CampaignCriteria.Selects.campaign_status)
    elif target == 'missing certificates select':
        helpers.click_helper(locations.CampaignCriteria.Selects.missing_certificates)
    elif target == 'invalid certificates select':
        helpers.click_helper(locations.CampaignCriteria.Selects.invalid_certificates)
    elif target == 'valid certificates select':
        helpers.click_helper(locations.CampaignCriteria.Selects.valid_certificates)
    elif target == 'has requests select':
        helpers.click_helper(locations.CampaignCriteria.Selects.has_requests)
    elif target == 'campaign name add all button':
        helpers.click_helper(locations.CampaignCriteria.Buttons.campaign_name_add_all)
    elif target == 'campaign name remove all button':
        helpers.click_helper(locations.CampaignCriteria.Buttons.campaign_name_remove_all)
    elif target == 'campaign status add all button':
        helpers.click_helper(locations.CampaignCriteria.Buttons.campaign_status_add_all)
    elif target == 'campaign status remove all button':
        helpers.click_helper(locations.CampaignCriteria.Buttons.campaign_status_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET)


def results_page_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer number header link':
        helpers.click_helper(locations.ResultsPage.Links.customer_number_header)
    elif target == 'name header link':
        helpers.click_helper(locations.ResultsPage.Links.name_header)
    elif target == 'first top link':
        helpers.click_helper(locations.ResultsPage.Links.first_top)
    elif target == 'prev top link':
        helpers.click_helper(locations.ResultsPage.Links.prev_top)
    elif target == 'page selector top link':
        helpers.click_helper(locations.ResultsPage.Links.page_selector_top)
    elif target == 'next top link':
        helpers.click_helper(locations.ResultsPage.Links.next_top)
    elif target == 'last top link':
        helpers.click_helper(locations.ResultsPage.Links.last_top)
    elif target == 'first bottom link':
        helpers.click_helper(locations.ResultsPage.Links.first_bottom)
    elif target == 'prev bottom link':
        helpers.click_helper(locations.ResultsPage.Links.prev_bottom)
    elif target == 'page selector bottom link':
        helpers.click_helper(locations.ResultsPage.Links.page_selector_bottom)
    elif target == 'next bottom link':
        helpers.click_helper(locations.ResultsPage.Links.next_bottom)
    elif target == 'last bottom link':
        helpers.click_helper(locations.ResultsPage.Links.last_bottom)
    elif target == 'perform actions on results select':
        location = locations.ResultsPage.Selects.perform_actions_on_results
        helpers.click_or_select(location, **kwargs)
    elif target == 'search again button':
        location = locations.ResultsPage.Buttons.search_again
        helpers.click_or_select(location, **kwargs)
    elif target == 'save search button':
        location = locations.ResultsPage.Buttons.save_search
        helpers.click_or_select(location, **kwargs)
    elif target == 'email report button':
        location = locations.ResultsPage.Buttons.email_report
        helpers.click_or_select(location, **kwargs)
    elif target == 'export report button':
        location = locations.ResultsPage.Buttons.export_report
        helpers.click_or_select(location, **kwargs)
    else:
        print(warn.INVALID_CLICK_TARGET)


def get_search_results_count():
    count = driver.find_element_by_xpath('//*[@id="search_results_grid_toppager_right"]/div').text
    count = count.split()
    count = count[-1]

    print(count)
    return count
