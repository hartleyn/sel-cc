__author__ = 'Nick Hartley'
# 3/27/2018


class Buttons:
    basic = '//div[@id="search_options"]/button'
    advanced = '//div[@id="search_options"]/button[2]'
    get_search_results = '//div[@id="content"]/div[10]/button'
    search_config = '//div[@id="mainsearch_config_div"]/button'


class Links:
    customer_criteria = '//div[@id="CustomerCriteria"]/div/h4/a'
    customer_attributes = '//div[@id="CustomerAttributes"]/div/h4/a'
    document_criteria = '//div[@id="CertificateCriteria"]/div/h4/a'
    document_category_override = '//div[@id="OverrideCriteria"]/div/h4/a'
    document_attributes = '//div[@id="CertificateAttributes"]/div/h4/a'
    customer_document_categories = '//div[@id="CustomerTaxCodes"]/div/h4/a'
    customer_bill_ship_information = '//div[@id="CustomerBillShip"]/div/h4/a'
    document_categories = '//div[@id="CertificateTaxCodes"]/div/h4/a'
    document_invalid_reasons = '//div[@id="CertificateInvalidReason"]/div/h4/a'
    campaign_criteria = '//div[@id="CampaignCustomerStatus"]/div/h4/a'
    clear_search_criteria = '//*[@id="CustomerCriteria"]/div[1]/h4/span'


class CustomerCriteria:
    class Buttons:
        state_add_all = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button'
        state_remove_all = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button[2]'

    class Selects:
        state = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[3]/td[2]/select'
        fatca_reporting_code = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[14]/td[4]/div/select'
        exempt_payee_code = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[15]/td[2]/div/select'
        taxpayer_identification_type = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[15]/td[4]/div/select'
        tax_classification = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[16]/td[2]/div/select'
        withhold_back_up_taxes = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[16]/td[4]/div/select'
        completed_for_a_corporation = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[17]/td[2]/div/select'
        llc_tax_classification = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[17]/td[4]/div/select'
        create_date = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[19]/td[2]/div/select'
        modified_date = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[20]/td[2]/div/select'
        last_transaction_date = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[21]/td[2]/div/select'

    class Inputs:
        customer_numbers = '//textarea[@id="Customer.customer_numbers"]'
        alternate_id = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr/td[4]/div/input'
        customer_name = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[2]/td[2]/div/input'
        state = '//div[@id="Customer_state_id_chosen"]/ul/li/input'
        fein = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[4]/td[2]/div/input'
        tax_number = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[5]/td[2]/div/input'
        address_line_1 = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[6]/td[2]/div/input'
        city = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[6]/td[4]/div/input'
        address_line_2 = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[7]/td[2]/div/input'
        zip = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[7]/td[4]/div/input'
        phone_number = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[8]/td[2]/div/input'
        fax_number = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[8]/td[4]/div/input'
        contact_name = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[9]/td[2]/div/input'
        contact_email = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[9]/td[4]/div/input'
        customer_created_date_begin = '//div[@id="customer_create_date_exact_div"]/div/input'
        customer_created_date_end = '//div[@id="customer_create_date_exact_div"]/div[2]/input'
        customer_created_days_ago = '//div[@id="customer_create_date_relative_div"]/div/input'
        customer_created_days_to = '//div[@id="customer_create_date_relative_div"]/div[2]/input'
        customer_modified_date_begin = '//div[@id="customer_modified_date_exact_div"]/div/input'
        customer_modified_date_end = '//div[@id="customer_modified_date_exact_div"]/div[2]/input'
        customer_modified_days_ago = '//div[@id="customer_modified_date_relative_div"]/div/input'
        customer_modified_days_to = '//div[@id="customer_modified_date_relative_div"]/div[2]/input'
        last_transaction_date_begin = '//div[@id="last_transaction_date_exact_div"]/div/input'
        last_transaction_date_end = '//div[@id="last_transaction_date_exact_div"]/div[2]/input'
        last_transaction_days_ago = '//div[@id="last_transaction_date_relative_div"]/div/input'
        last_transaction_days_to = '//div[@id="last_transaction_date_relative_div"]/div[2]/input'


class CustomerAttributes:
    class Buttons:
        customer_has_attributes_add_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div[3]/button'
        customer_has_attributes_remove_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div[3]/button[2]'
        customer_does_not_have_attributes_add_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div[3]/button'
        customer_does_not_have_attributes_remove_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        customer_has_any_all_attributes = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div/select'
        customer_has_attributes = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/select'
        customer_does_not_have_any_all_attributes = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div/select'
        customer_does_not_have_attributes = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/select'
        between_dates = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        customer_has_attributes = '//div[@id="CustomerCode_has_chosen"]/ul/li/input'
        customer_does_not_have_attributes = '//div[@id="CustomerCode_not_has_chosen"]/ul/li/input'
        customer_attributes_date_begin = '//div[@id="customer_attributes_date_exact_div"]/div/input'
        customer_attributes_date_end = '//div[@id="customer_attributes_date_exact_div"]/div[2]/input'
        customer_attributes_days_ago = '//div[@id="customer_attributes_date_relative_div"]/div/input'
        customer_attributes_days_to = '//div[@id="customer_attributes_date_relative_div"]/div[2]/input'


class CertificateCriteria:
    class Buttons:
        status_add_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button'
        status_remove_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button[2]'
        document_type_add_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[4]/td[2]/div[2]/button'
        document_type_remove_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[4]/td[2]/div[2]/button[2]'
        exposure_zone_add_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[5]/td[2]/div[2]/button'
        exposure_zone_remove_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[5]/td[2]/div[2]/button[2]'

    class Selects:
        has_certificate = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr/td[4]/div/select'
        certificate_is_valid = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[2]/td[2]/div/select'
        status = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[3]/td[2]/select'
        document_type = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[4]/td[2]/select'
        exposure_zone = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[5]/td[2]/select'
        expired = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[6]/td[2]/div/select'
        link_type = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[6]/td[4]/div/select'
        is_single = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[7]/td[2]/div/select'
        has_api_error = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[9]/td[2]/div/select'
        create_date = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[11]/td[2]/div/select'
        modified_date = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[12]/td[2]/div/select'
        effective_date = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[13]/td[2]/div/select'
        expiration_date = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[14]/td[2]/div/select'
        expiration_date_days_ago_days_from_now = '//div[@id="certificate_expiration_date_relative_div"]/div[3]/select'

    class Inputs:
        certificate_ids = '//textarea[@id="Certificate.certificate_ids"]'
        status = '//div[@id="Certificate_certificate_status_id_chosen"]/ul/li/input'
        document_type = '//div[@id="Certificate_document_type_id_chosen"]/ul/li/input'
        exposure_zone = '//div[@id="Certificate_exposure_zone_id_chosen"]/ul/li/input'
        exempt_percent = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[7]/td[4]/div/input'
        po_number = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[8]/td[2]/div/input'
        tax_number = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[8]/td[4]/div/input'
        custom_field1 = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[9]/td[4]/div/input'
        custom_field2 = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[10]/td[2]/div/input'
        certificate_created_date_begin = '//div[@id="certificate_create_date_exact_div"]/div/input'
        certificate_created_date_end = '//div[@id="certificate_create_date_exact_div"]/div[2]/input'
        certificate_created_days_ago = '//div[@id="certificate_create_date_relative_div"]/div/input'
        certificate_created_days_to = '//div[@id="certificate_create_date_relative_div"]/div[2]/input'
        certificate_modified_date_begin = '//div[@id="certificate_modified_date_exact_div"]/div/input'
        certificate_modified_date_end = '//div[@id="certificate_modified_date_exact_div"]/div[2]/input'
        certificate_modified_days_ago = '//div[@id="certificate_modified_date_relative_div"]/div/input'
        certificate_modified_days_to = '//div[@id="certificate_modified_date_relative_div"]/div[2]/input'
        certificate_signed_date_begin = '//div[@id="certificate_signed_date_exact_div"]/div/input'
        certificate_signed_date_end = '//div[@id="certificate_signed_date_exact_div"]/div[2]/input'
        certificate_signed_days_ago = '//div[@id="certificate_signed_date_relative_div"]/div/input'
        certificate_signed_days_to = '//div[@id="certificate_signed_date_relative_div"]/div[2]/input'
        certificate_expiration_date_begin = '//div[@id="certificate_expiration_date_exact_div"]/div/input'
        certificate_expiration_date_end = '//div[@id="certificate_expiration_date_exact_div"]/div[2]/input'
        certificate_expiration_days_ago = '//div[@id="certificate_expiration_date_relative_div"]/div/input'
        certificate_expiration_days_to = '//div[@id="certificate_expiration_date_relative_div"]/div[2]/input'


class ExemptReasonOverride:
    class Buttons:
        override_reason_in_exposure_zones_add_all = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr/td/div[3]/button'
        override_reason_in_exposure_zones_remove_all = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr/td/div[3]/button[2]'
        override_has_documented_reasons_add_all = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[2]/td/div[3]/button'
        override_has_documented_reasons_remove_all = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        override_reason_in_any_all_exposure_zones = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr/td/div/select'
        override_reason_in_exposure_zones = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr/td/select'
        override_has_any_all_documented_reasons = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[2]/td/div/select'
        override_has_documented_reasons = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[2]/td/select'
        create_date = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[3]/td[2]/div/select'
        effective_date = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[4]/td[2]/div/select'
        expiration_date = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[5]/td[2]/div/select'
        effective_date_days_ago_days_from_now = '//div[@id="override_effective_date_relative_div"]/div[3]/select'
        expiration_date_days_ago_days_from_now = '//div[@id="override_expiration_date_relative_div"]/div[3]/select'

    class Inputs:
        override_reason_in_exposure_zones = '//div[@id="Override_zone_has_chosen"]/ul/li/input'
        override_has_documented_reasons = '//div[@id="Override_documented_has_chosen"]/ul/li/input'
        override_created_date_begin = '//div[@id="override_create_date_exact_div"]/div/input'
        override_created_date_end = '//div[@id="override_create_date_exact_div"]/div[2]/input'
        override_created_days_ago = '//div[@id="override_create_date_relative_div"]/div/input'
        override_created_days_to = '//div[@id="override_create_date_relative_div"]/div[2]/input'
        override_effective_date_begin = '//div[@id="override_effective_date_exact_div"]/div/input'
        override_effective_date_end = '//div[@id="override_effective_date_exact_div"]/div[2]/input'
        override_effective_days_ago = '//div[@id="override_effective_date_relative_div"]/div/input'
        override_effective_days_to = '//div[@id="override_effective_date_relative_div"]/div[2]/input'
        override_expiration_date_begin = '//div[@id="override_expiration_date_exact_div"]/div/input'
        override_expiration_date_end = '//div[@id="override_expiration_date_exact_div"]/div[2]/input'
        override_expiration_days_ago = '//div[@id="override_expiration_date_relative_div"]/div/input'
        override_expiration_days_to = '//div[@id="override_expiration_date_relative_div"]/div[2]/input'
        license_number = '//div[@id="collapseOverrideCriteria"]/div/table/tbody/tr[6]/td[2]/div/input'


class CertificateAttributes:
    class Buttons:
        certificate_has_attributes_add_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div[3]/button'
        certificate_has_attributes_remove_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_does_not_have_attributes_add_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_does_not_have_attributes_remove_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        customer_has_any_all_attributes = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div/select'
        customer_has_attributes = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/select'
        customer_does_not_have_any_all_attributes = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div/select'
        customer_does_not_have_attributes = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/select'
        attribute_added_date = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        customer_has_attributes = '//div[@id="CertificateCode_has_chosen"]/ul/li/input'
        customer_does_not_have_attributes = '//div[@id="CertificateCode_not_has_chosen"]/ul/li/input'
        certificate_attributes_date_begin = '//div[@id="certificate_attributes_date_exact_div"]/div/input'
        certificate_attributes_date_end = '//div[@id="certificate_attributes_date_exact_div"]/div[2]/input'
        certificate_attributes_days_ago = '//div[@id="certificate_attributes_date_relative_div"]/div/input'
        certificate_attributes_days_to = '//div[@id="certificate_attributes_date_relative_div"]/div[2]/input'


class CustomerExemptExposureReasons:
    class Buttons:
        customer_reason_in_exposure_zones_add_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div[3]/button'
        customer_reason_in_exposure_zones_remove_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div[3]/button[2]'
        customer_has_documented_reasons_add_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button'
        customer_has_documented_reasons_remove_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'
        customer_does_not_have_documented_reasons_add_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button'
        customer_does_not_have_documented_reasons_remove_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button[2]'
        customer_has_expected_reasons_add_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button'
        customer_has_expected_reasons_remove_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button[2]'
        customer_does_not_have_expected_reasons_add_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button'
        customer_does_not_have_expected_reasons_remove_all = 'div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button[2]'

    class Selects:
        customer_reason_in_any_all_exposure_zones = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div/select'
        customer_reason_in_exposure_zones = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/select'
        customer_has_any_all_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div/select'
        customer_has_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/select'
        customer_does_not_have_any_all_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div/select'
        customer_does_not_have_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/select'
        customer_has_any_all_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div/select'
        customer_has_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/select'
        customer_does_not_have_any_all_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div/select'
        customer_does_not_have_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/select'
        reason_modified_date = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[6]/td[2]/div/select'

    class Inputs:
        customer_reason_in_exposure_zones = '//div[@id="CustomersTaxCode_zone_has_chosen"]/ul/li/input'
        customer_has_documented_reasons = '//div[@id="CustomersTaxCode_documented_has_chosen"]/ul/li/input'
        customer_does_not_have_documented_reasons = '//div[@id="CustomersTaxCode_documented_not_has_chosen"]/ul/li/input'
        customer_has_expected_reasons = '//div[@id="CustomersTaxCode_expected_has_chosen"]/ul/li/input'
        customer_does_not_have_expected_reasons = '//div[@id="CustomersTaxCode_expected_not_has_chosen"]/ul/li/input'
        customer_tax_code_date_begin = '//div[@id="customer_tax_code_date_exact_div"]/div/input'
        customer_tax_code_date_end = '//div[@id="customer_tax_code_date_exact_div"]/div[2]/input'
        customer_tax_code_days_ago = '//div[@id="customer_tax_code_date_relative_div"]/div/input'
        customer_tax_code_days_to = '//div[@id="customer_tax_code_date_relative_div"]/div[2]/input'


class CustomerBillShipInformation:
    class Buttons:
        customer_has_bill_ship_types_add_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr/td/div[3]/button'
        customer_has_bill_ship_types_remove_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr/td/div[3]/button[2]'
        customer_bills_to_states_provinces_add_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[2]/td/div[3]/button'
        customer_bills_to_states_provinces_remove_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[2]/td/div[3]/button[2]'
        customer_ships_to_states_provinces_add_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[3]/td/div[3]/button'
        customer_ships_to_states_provinces_remove_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[3]/td/div[3]/button[2]'
        bill_customer_state_add_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[6]/td[2]/div[2]/button'
        bill_customer_state_remove_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[6]/td[2]/div[2]/button[2]'
        ship_customer_state_add_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[9]/td[2]/div[2]/button'
        ship_customer_state_remove_all = 'div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[9]/td[2]/div[2]/button[2]'

    class Selects:
        customer_has_any_all_bill_ship_types = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr/td/div/select'
        customer_has_bill_ship_types = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr/td/select'
        customer_bills_to_any_all_states_provinces = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[2]/td/div/select'
        customer_bills_to_states_provinces = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[2]/td/select'
        customer_ships_to_any_all_states_provinces = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[3]/td/div/select'
        customer_ships_to_states_provinces = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[3]/td/select'
        bill_customer_state = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[6]/td[2]/select'
        ship_customer_state = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[9]/td[2]/select'

    class Inputs:
        bill_customer_numbers = '//textarea[@id="CustomersBillToCustomerInfo.customer_numbers"]'
        ship_customer_numbers = '//textarea[@id="CustomersShipToCustomerInfo.customer_numbers"]'
        customer_has_bill_ship_types = '//div[@id="CustomersBillShip_has_chosen"]/ul/li/input'
        customer_bills_to_states_provinces = '//div[@id="CustomersBillState_has_chosen"]/ul/li/input'
        customer_ships_to_states_provinces = '//div[@id="CustomersShipState_has_chosen"]/ul/li/input'
        bill_alternate_id = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[4]/td[4]/div/input'
        bill_customer_name = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[5]/td[2]/div/input'
        bill_customer_state = '//div[@id="CustomersBillToCustomerInfo_state_id_chosen"]/ul/li/input'
        ship_alternate_id = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[7]/td[4]/div/input'
        ship_customer_name = '//div[@id="collapseCustomerBillShip"]/div/table/tbody/tr[8]/td[2]/div/input'
        ship_customer_state = '//div[@id="CustomersShipToCustomerInfo_state_id_chosen"]/ul/li/input'


class CertificateExemptExposureReasons:
    class Buttons:
        certificate_reason_in_exposure_zones_add_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div[3]/button'
        certificate_reason_in_exposure_zones_remove_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_has_documented_reasons_add_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_has_documented_reasons_remove_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'
        certificate_does_not_have_documented_reasons_add_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button'
        certificate_does_not_have_documented_reasons_remove_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button[2]'
        certificate_has_expected_reasons_add_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button'
        certificate_has_expected_reasons_remove_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button[2]'
        certificate_does_not_have_expected_reasons_add_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button'
        certificate_does_not_have_expected_reasons_remove_all = 'div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button[2]'

    class Selects:
        certificate_reason_in_any_all_exposure_zones = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div/select'
        certificate_reason_in_exposure_zones = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/select'
        certificate_has_any_all_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div/select'
        certificate_has_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/select'
        certificate_does_not_have_any_all_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div/select'
        certificate_does_not_have_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/select'
        certificate_has_any_all_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div/select'
        certificate_has_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/select'
        certificate_does_not_have_any_all_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div/select'
        certificate_does_not_have_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/select'

    class Inputs:
        certificate_reason_in_exposure_zones = '//div[@id="CertificatesTaxCode_zone_has_chosen"]/ul/li/input'
        certificate_has_documented_reasons = '//div[@id="CertificatesTaxCode_documented_has_chosen"]/ul/li/input'
        certificate_does_not_have_documented_reasons = '//div[@id="CertificatesTaxCode_documented_not_has_chosen"]/ul/li/input'
        certificate_has_expected_reasons = '//div[@id="CertificatesTaxCode_expected_has_chosen"]/ul/li/input'
        certificate_does_not_have_expected_reasons = '//div[@id="CertificatesTaxCode_expected_not_has_chosen"]/ul/li/input'


class CertificateInvalidReasons:
    class Buttons:
        certificate_has_invalid_reasons_add_all = 'div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div[3]/button'
        certificate_has_invalid_reasons_remove_all = 'div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_does_not_have_invalid_reasons_add_all = 'div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_does_not_have_invalid_reasons_remove_all = 'div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        certificate_has_any_all_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div/select'
        certificate_has_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/select'
        certificate_does_not_have_any_all_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div/select'
        certificate_does_not_have_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/select'
        reason_added_date = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        certificate_has_invalid_reasons = '//div[@id="InvalidReason_has_chosen"]/ul/li/input'
        certificate_does_not_have_invalid_reasons = '//div[@id="InvalidReason_not_has_chosen"]/ul/li/input'
        certificate_invalid_reasons_date_begin = '//div[@id="certificate_invalid_reasons_date_exact_div"]/div/input'
        certificate_invalid_reasons_date_end = '//div[@id="certificate_invalid_reasons_date_exact_div"]/div[2]/input'
        certificate_invalid_reasons_days_ago = '//div[@id="certificate_invalid_reasons_date_relative_div"]/div/input'
        certificate_invalid_reasons_days_to = '//div[@id="certificate_invalid_reasons_date_relative_div"]/div[2]/input'


class CampaignCriteria:
    class Buttons:
        campaign_name_add_all = 'div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[2]/div[2]/button'
        campaign_name_remove_all = 'div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[2]/div[2]/button[2]'
        campaign_status_add_all = 'div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[4]/div[2]/button'
        campaign_status_remove_all = 'div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[4]/div[2]/button[2]'

    class Selects:
        customer_status = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr/td[2]/div/select'
        campaign_name = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[2]/select'
        campaign_status = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[2]/td[4]/select'
        missing_certificates = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[3]/td[2]/div/select'
        expired_certificates = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[3]/td[4]/div/select'
        invalid_certificates = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[4]/td[2]/div/select'
        valid_certificates = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[4]/td[4]/div/select'
        has_requests = '//div[@id="collapseCampaignCustomerStatus"]/div/table/tbody/tr[5]/td[2]/div/select'

    class Inputs:
        campaign_name = '//div[@id="Campaign_id_chosen"]/ul/li/input'
        campaign_status = '//div[@id="Campaign_status_chosen"]/ul/li/input'
        campaign_request_date_begin = '//div[@id="campaign_request_date_exact_div"]/div/input'
        campaign_request_date_end = '//div[@id="campaign_request_date_exact_div"]/div[2]/input'
        campaign_request_days_ago = '//div[@id="campaign_request_date_relative_div"]/div/input'
        campaign_request_days_to = '//div[@id="campaign_request_date_relative_div"]/div[2]/input'


class ResultsPage:
    class Buttons:
        search_again = '//button[@id="search_again_btn"]'
        save_search = '//button[@id="save_search_btn"]'
        email_report = '//button[@id="email_results_btn"]'
        export_report = '//button[@id="export_results_btn"]'

    class Selects:
        perform_actions_on_results = '//select[@id="bulk_action_selector"]'

    class Links:
        customer_number_header = '//div[@id="jqgh_search_results_grid_customer_number"]'
        name_header = '//*[@id="jqgh_search_results_grid_name"]'
        first_top = '//td[@id="first_t_search_results_grid_toppager"]/span'
        prev_top = '//td[@id="prev_t_search_results_grid_toppager"]/span'
        page_selector_top = '//td[@id="search_results_grid_toppager_center"]/table/tbody/tr/td[4]/div/a'
        next_top = '//td[@id="next_t_search_results_grid_toppager"]/span'
        last_top = '//td[@id="last_t_search_results_grid_toppager"]/span'
        first_bottom = '//td[@id="first_pager"]/span'
        prev_bottom = '//td[@id="prev_pager"]/span'
        page_selector_bottom = '//td[@id="pager_center"]/table/tbody/tr/td[3]/div/a'
        next_bottom = '//td[@id="next_pager"]/span'
        last_bottom = '//td[@id="last_pager"]/span'











