import time
from general import helpers
from utilities import warnings as warn
from certificate_search import locations

__author__ = 'Nick Hartley'
# 5/15/2018


def click(target_name):
    target = target_name.lower()

    if target == 'basic button':
        helpers.click_helper(locations.Buttons.basic)
    elif target == 'advanced button':
        helpers.click_helper(locations.Buttons.advanced)
    elif target == 'get search results button':
        helpers.click_helper(locations.Buttons.get_search_results)
        time.sleep(2)
    elif target == 'search config button' or target == 'search configuration button':
        helpers.click_helper(locations.Buttons.search_config)
    elif target == 'certificate criteria link':
        helpers.click_helper(locations.Links.certificate_criteria)
    elif target == 'certificate attributes link':
        helpers.click_helper(locations.Links.certificate_attributes)
    elif target == 'customer criteria link':
        helpers.click_helper(locations.Links.customer_criteria)
    elif target == 'customer attributes link':
        helpers.click_helper(locations.Links.customer_attributes)
    elif target == 'customer exempt exposure reasons link':
        helpers.click_helper(locations.Links.customer_exempt_exposure_reasons)
    elif target == 'certificate exempt/exposure reasons link':
        helpers.click_helper(locations.Links.certificate_exempt_exposure_reasons)
    elif target == 'certificate invalid reasons link':
        helpers.click_helper(locations.Links.certificate_invalid_reasons)
    elif target == 'validator criteria link':
        helpers.click_helper(locations.Links.validator_criteria)
    elif target == 'retail location link':
        helpers.click_helper(locations.Links.retail_location)
    elif target == 'clear search criteria link':
        helpers.click_helper(locations.Links.clear_search_results)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def certificate_criteria_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate ids input':
        location = locations.CertificateCriteria.Inputs.certificate_ids
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'status input':
        location = locations.CertificateCriteria.Inputs.status
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'exposure zone input':
        location = locations.CertificateCriteria.Inputs.exposure_zone
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'exempt percent input':
        location = locations.CertificateCriteria.Inputs.exempt_percent
        helpers.click_or_type(location, **kwargs)
    elif target == 'po number input':
        location = locations.CertificateCriteria.Inputs.po_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'tax number input':
        location = locations.CertificateCriteria.Inputs.tax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate created date begin input':
        location = locations.CertificateCriteria.Inputs.certificate_created_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate created date end input':
        location = locations.CertificateCriteria.Inputs.certificate_created_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate created date ago input':
        location = locations.CertificateCriteria.Inputs.certificate_created_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate created date to input':
        location = locations.CertificateCriteria.Inputs.certificate_created_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate modified date begin input':
        location = locations.CertificateCriteria.Inputs.certificate_modified_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate modified date end input':
        location = locations.CertificateCriteria.Inputs.certificate_modified_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate modified date ago input':
        location = locations.CertificateCriteria.Inputs.certificate_modified_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate modified date to input':
        location = locations.CertificateCriteria.Inputs.certificate_modified_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate signed date begin input':
        location = locations.CertificateCriteria.Inputs.certificate_signed_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate signed date end input':
        location = locations.CertificateCriteria.Inputs.certificate_signed_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate signed date ago input':
        location = locations.CertificateCriteria.Inputs.certificate_signed_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate signed date to input':
        location = locations.CertificateCriteria.Inputs.certificate_signed_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate expiration date begin input':
        location = locations.CertificateCriteria.Inputs.certificate_expiration_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate expiration date end input':
        location = locations.CertificateCriteria.Inputs.certificate_expiration_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate expiration date ago input':
        location = locations.CertificateCriteria.Inputs.certificate_expiration_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate expiration date to input':
        location = locations.CertificateCriteria.Inputs.certificate_expiration_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'has customer select':
        location = locations.CertificateCriteria.Selects.has_customer
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate is valid select':
        location = locations.CertificateCriteria.Selects.valid
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
    elif target == 'create date select':
        location = locations.CertificateCriteria.Selects.certificate_create_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'modified date select':
        location = locations.CertificateCriteria.Selects.certificate_modified_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'effective date select':
        location = locations.CertificateCriteria.Selects.certificate_signed_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'expiration date select':
        location = locations.CertificateCriteria.Selects.certificate_expiration_date_day_range
        helpers.click_or_select(location, **kwargs)
    elif target == 'effective date days ago days from now select':
        location = locations.CertificateCriteria.Selects.certificate_signed_date_day_range
        helpers.click_or_select(location, **kwargs)
    elif target == 'expiration date days ago days from now select':
        location = locations.CertificateCriteria.Selects.certificate_expiration_date_day_range
        helpers.click_or_select(location, **kwargs)
    elif target == 'status add all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.status_add_all)
    elif target == 'status remove all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.status_remove_all)
    elif target == 'exposure zone add all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.exposure_zone_add_all)
    elif target == 'exposure zone remove all button':
        helpers.click_helper(locations.CertificateCriteria.Buttons.exposure_zone_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def certificate_attributes_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate has input':
        location = locations.CertificateAttributes.Inputs.certificate_has
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'certificate does not have input':
        location = locations.CertificateAttributes.Inputs.certificate_does_not_have
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate attribute added date begin input':
        location = locations.CertificateAttributes.Inputs.certificate_attribute_added_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate attribute added date end input':
        location = locations.CertificateAttributes.Inputs.certificate_attribute_added_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate attribute added date ago input':
        location = locations.CertificateAttributes.Inputs.certificate_attribute_added_date_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate attribute added date to input':
        location = locations.CertificateAttributes.Inputs.certificate_attribute_added_date_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'certificate has select':
        location = locations.CertificateAttributes.Selects.certificate_has
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate does not have select':
        location = locations.CertificateAttributes.Selects.certificate_does_not_have
        helpers.click_or_select(location, **kwargs)
    elif target == 'attribute added date select':
        location = locations.CertificateAttributes.Selects.attribute_added_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate has add all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_has_add_all)
    elif target == 'certificate has remove all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_has_remove_all)
    elif target == 'certificate does not have add all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_does_not_have_add_all)
    elif target == 'certificate does not have remove all button':
        helpers.click_helper(locations.CertificateAttributes.Buttons.certificate_does_not_have_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def customer_criteria_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer numbers input':
        location = locations.CustomerCriteria.Inputs.customer_numbers
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'alternate id input':
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
    elif target == 'address line 1 input':
        location = locations.CustomerCriteria.Inputs.address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.CustomerCriteria.Inputs.address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'zip input' or target == 'zip code input':
        location = locations.CustomerCriteria.Inputs.zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone number input':
        location = locations.CustomerCriteria.Inputs.phone_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'fax number input':
        location = locations.CustomerCriteria.Inputs.fax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact name input':
        location = locations.CustomerCriteria.Inputs.contact_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact email input':
        location = locations.CustomerCriteria.Inputs.contact_email
        helpers.click_or_type(location, **kwargs)
    elif target == 'created date begin input':
        location = locations.CustomerCriteria.Inputs.customer_created_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'created date end input':
        location = locations.CustomerCriteria.Inputs.customer_created_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'created date ago input':
        location = locations.CustomerCriteria.Inputs.customer_created_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'created date to input':
        location = locations.CustomerCriteria.Inputs.customer_created_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'modified date begin input':
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
    elif target == 'last transaction date begin input':
        location = locations.CustomerCriteria.Inputs.last_transaction_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction date end input':
        location = locations.CustomerCriteria.Inputs.last_transaction_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction date ago input':
        location = locations.CustomerCriteria.Inputs.last_transaction_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'last transaction date to input':
        location = locations.CustomerCriteria.Inputs.last_transaction_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'create date select':
        location = locations.CustomerCriteria.Selects.customer_create_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'modified date select':
        location = locations.CustomerCriteria.Selects.customer_modified_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'last transaction date select':
        location = locations.CustomerCriteria.Selects.last_transaction_date_format
        helpers.click_or_select(location, **kwargs)
    elif target == 'state add all button':
        helpers.click_helper(locations.CustomerCriteria.Buttons.state_add_all)
    elif target == 'state remove all button':
        helpers.click_helper(locations.CustomerCriteria.Buttons.state_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def customer_attributes_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer has attributes input':
        location = locations.CustomerAttributes.Inputs.customer_has
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer does not have attributes input':
        location = locations.CustomerAttributes.Inputs.customer_does_not_have
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'attribute added date start input':
        location = locations.CustomerAttributes.Inputs.customer_attributes_date_begin
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'attribute added date end input':
        location = locations.CustomerAttributes.Inputs.customer_attributes_date_end
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'attribute added date ago input':
        location = locations.CustomerAttributes.Inputs.customer_attributes_days_ago
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'attribute added date to input':
        location = locations.CustomerAttributes.Inputs.customer_attributes_days_to
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer has attributes select':
        location = locations.CustomerAttributes.Selects.customer_has
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer does not have attributes select':
        location = locations.CustomerAttributes.Selects.customer_does_not_have
        helpers.click_or_select(location, **kwargs)
    elif target == 'attribute added date select':
        location = locations.CustomerAttributes.Selects.attribute_added_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer has add all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_has_add_all)
    elif target == 'customer has remove all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_has_remove_all)
    elif target == 'customer does not have add all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_does_not_have_add_all)
    elif target == 'customer does not have remove all button':
        helpers.click_helper(locations.CustomerAttributes.Buttons.customer_does_not_have_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def customer_exempt_exposure_reasons(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer reason in exposure zones input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_reason_in_exposure_zones
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer has documented reasons input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_has_documented_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer does not have documented reasons input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_does_not_have_documented_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer has expected reasons input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_has_expected_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'customer does not have expected reasons input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_does_not_have_expected_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'reason modified date begin input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'reason modified date end input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'reason modified date ago input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'reason modified date to input':
        location = locations.CustomerExemptExposureReasons.Inputs.customer_tax_code_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'customer reason in exposure zones select':
        location = locations.CustomerExemptExposureReasons.Selects.customer_reason_in_exposure_zones
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer has documented reasons select':
        location = locations.CustomerExemptExposureReasons.Selects.customer_has_documented_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer does not have documented reasons select':
        location = locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_documented_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer has expected reasons select':
        location = locations.CustomerExemptExposureReasons.Selects.customer_has_expected_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer does not have expected reasons select':
        location = locations.CustomerExemptExposureReasons.Selects.customer_does_not_have_expected_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'reason modified date select':
        location = locations.CustomerExemptExposureReasons.Selects.reason_modified_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'customer reason in exposure zones add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_reason_in_exposure_zones_add_all)
    elif target == 'customer reason in exposure zones remove all button':
        helpers.click_helper(
            locations.CustomerExemptExposureReasons.Buttons.customer_reason_in_exposure_zones_remove_all)
    elif target == 'customer has documented reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_documented_reasons_add_all)
    elif target == 'customer has documented reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_documented_reasons_remove_all)
    elif target == 'customer does not have documented reasons add all button':
        helpers.click_helper(
            locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_documented_reasons_add_all)
    elif target == 'customer does not have documented reasons remove all button':
        helpers.click_helper(
            locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_documented_reasons_remove_all)
    elif target == 'customer has expected reasons add all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_expected_reasons_add_all)
    elif target == 'customer has expected reasons remove all button':
        helpers.click_helper(locations.CustomerExemptExposureReasons.Buttons.customer_has_expected_reasons_remove_all)
    elif target == 'customer does not have expected reasons add all button':
        helpers.click_helper(
            locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_expected_reasons_add_all)
    elif target == 'customer does not have expected reasons remove all button':
        helpers.click_helper(
            locations.CustomerExemptExposureReasons.Buttons.customer_does_not_have_expected_reasons_remove_all)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def certificate_exempt_exposure_reason_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate reason in exposure zones input':
        location = locations.CertificateExemptExposureReasons.Inputs.certificate_reason_in_exposure_zones
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate has documented reasons input':
        location = locations.CertificateExemptExposureReasons.Inputs.certificate_has_documented_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate does not have documented reasons input':
        location = locations.CertificateExemptExposureReasons.Inputs.certificate_does_not_have_documented_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate has expected reasons input':
        location = locations.CertificateExemptExposureReasons.Inputs.certificate_has_expected_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate does not have expected reasons input':
        location = locations.CertificateExemptExposureReasons.Inputs.certificate_does_not_have_expected_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate reason in exposure zones select':
        location = locations.CertificateExemptExposureReasons.Selects.certificate_reason_in_exposure_zones
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate reason has documented reasons select':
        location = locations.CertificateExemptExposureReasons.Selects.certificate_has_documented_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate reason does not have documented reasons select':
        location = locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_documented_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate reason has expected reasons select':
        location = locations.CertificateExemptExposureReasons.Selects.certificate_has_expected_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate reason does not have expected reasons select':
        location = locations.CertificateExemptExposureReasons.Selects.certificate_does_not_have_expected_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate reason in exposure zones add all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_reason_in_exposure_zones_add_all
        helpers.click_helper(location)
    elif target == 'certificate reason in exposure zones remove all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_reason_in_exposure_zones_remove_all
        helpers.click_helper(location)
    elif target == 'certificate has documented reasons add all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_has_documented_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate has documented reasons remove all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_has_documented_reasons_remove_all
        helpers.click_helper(location)
    elif target == 'certificate does not have documented reasons add all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_documented_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate does not have documented reasons remove all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_documented_reasons_remove_all
        helpers.click_helper(location)
    elif target == 'certificate has expected reasons add all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_has_expected_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate has expected reasons remove all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_has_expected_reasons_remove_all
        helpers.click_helper(location)
    elif target == 'certificate does not have expected reasons add all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_expected_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate does not have expected reasons remove all button':
        location = locations.CertificateExemptExposureReasons.Buttons.certificate_does_not_have_expected_reasons_remove_all
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def certificate_invalid_reasons_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate has invalid reasons input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_has_invalid_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate does not have invalid reasons input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_does_not_have_invalid_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate invalid reasons date begin input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_date_begin
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate invalid reasons date end input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_date_end
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate invalid reasons date ago input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_days_ago
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate invalid reasons date to input':
        location = locations.CertificateInvalidReasons.Inputs.certificate_invalid_reasons_days_to
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'certificate has invalid reasons select':
        location = locations.CertificateInvalidReasons.Selects.certificate_has_invalid_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate does not have invalid reasons select':
        location = locations.CertificateInvalidReasons.Selects.certificate_does_not_have_invalid_reasons
        helpers.click_or_select(location, **kwargs)
    elif target == 'reason added date select':
        location = locations.CertificateInvalidReasons.Selects.reason_added_date
        helpers.click_or_select(location, **kwargs)
    elif target == 'certificate has invalid reasons add all button':
        location = locations.CertificateInvalidReasons.Buttons.certificate_has_invalid_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate has invalid reasons remove all button':
        location = locations.CertificateInvalidReasons.Buttons.certificate_has_invalid_reasons_remove_all
        helpers.click_helper(location)
    elif target == 'certificate does not have invalid reasons add all button':
        location = locations.CertificateInvalidReasons.Buttons.certificate_does_not_have_invalid_reasons_add_all
        helpers.click_helper(location)
    elif target == 'certificate does not have invalid reasons remove all button':
        location = locations.CertificateInvalidReasons.Buttons.certificate_does_not_have_invalid_reasons_remove_all
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def validator_criteria_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'validator names input':
        location = locations.ValidatorCriteria.Inputs.validator_names
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'validation date date begin input':
        location = locations.ValidatorCriteria.Inputs.certificate_validation_date_begin
        helpers.click_or_type(location, **kwargs)
    elif target == 'validation date date end input':
        location = locations.ValidatorCriteria.Inputs.certificate_validation_date_end
        helpers.click_or_type(location, **kwargs)
    elif target == 'validation date date ago input':
        location = locations.ValidatorCriteria.Inputs.certificate_validation_days_ago
        helpers.click_or_type(location, **kwargs)
    elif target == 'validation date date to input':
        location = locations.ValidatorCriteria.Inputs.certificate_validation_days_to
        helpers.click_or_type(location, **kwargs)
    elif target == 'validation date select':
        location = locations.ValidatorCriteria.Selects.validation_date
        helpers.click_or_select(location, **kwargs)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def retail_location_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'location name input':
        location = locations.RetailLocation.Inputs.name
        helpers.click_or_type(location, **kwargs)
    elif target == 'location codes input':
        location = locations.RetailLocation.Inputs.location_codes
        helpers.textarea_field_click_or_type(location, **kwargs)
    elif target == 'state input':
        location = locations.RetailLocation.Inputs.state
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'limit search select':
        location = locations.RetailLocation.Selects.limit_search
        helpers.click_or_select(location, **kwargs)
    elif target == 'state add all button':
        location = locations.RetailLocation.Buttons.state_add_all
        helpers.click_helper(location)
    elif target == 'state remove all button':
        location = locations.RetailLocation.Buttons.state_remove_all
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target)


def results_page_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'certificate id header link':
        helpers.click_helper(locations.ResultsPage.Links.certificate_id_header)
    elif target == 'zone header link':
        helpers.click_helper(locations.ResultsPage.Links.zone_header)
    elif target == 'exempt reason header link':
        helpers.click_helper(locations.ResultsPage.Links.exempt_reason_header)
    elif target == 'effective header link':
        helpers.click_helper(locations.ResultsPage.Links.effective_header)
    elif target == 'expiration header link':
        helpers.click_helper(locations.ResultsPage.Links.expiration_header)
    elif target[0:11] == 'results row' and target[-4:] == 'link':
        if target[13] == ' ':
            number = target[12]  # Supports single digits
            helpers.click_helper(locations.Links.results_row(number))
            time.sleep(2)
            helpers.switch_to_new_window()
            time.sleep(2)
        elif target[14] == ' ':
            number = target[12:13]  # Supports double digits
            helpers.click_helper(locations.Links.results_row(number))
            time.sleep(2)
            helpers.switch_to_new_window()
            time.sleep(2)
        else:
            print(warn.SOME_PROBLEM)
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
        print(warn.INVALID_CLICK_TARGET, target)
