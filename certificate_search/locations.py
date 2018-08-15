
__author__ = 'Nick Hartley'
# 5/15/2018

class Buttons:
    # None = '//div[@id="save_search_model"]/div/div/div/button'
    save_search_add = '//div[@id="save_search_model"]/div/div/div[3]/button'
    # None = '//div[@id="export_results_modal"]/div/div/div/button'
    export_results_add = '//div[@id="export_results_modal"]/div/div/div[3]/button'
    # None = '//div[@id="email_report_modal"]/div/div/div/button'
    email_report_add = '//div[@id="div_add"]/button'
    # None = '//div[@id="bulk_api_resend_modal"]/div/div/div/button'
    resend_btn = '//div[@id="bulk_api_resend_modal"]/div/div/div[3]/button'
    # None = '//div[@id="bulk_delete_certificate_modal"]/div/div/div/button'
    delete_btn = '//div[@id="bulk_delete_certificate_modal"]/div/div/div[3]/button'
    saved_search_btn = '//div[@id="search_buttons"]/button'
    search_config = '//div[@id="mainsearch_config_div"]/button'
    basic = '//div[@id="search_options"]/button'
    advanced = '//div[@id="search_options"]/button[2]'
    get_search_results = '//div[@id="content"]/div[10]/button'


class Selects:
    bulk_action_selector = '//div[@id="search_actions"]/select'


class Inputs:
    SearchName = '//div[@id="save_search_model"]/div/div/div[2]/form/input'
    # None = '//div[@id="save_search_model"]/div/div/div[2]/form/input[2]'
    ReportExportName = '//div[@id="export_results_modal"]/div/div/div[2]/form/input'
    ReportExportFormat = '//div[@id="export_results_modal"]/div/div/div[2]/form/input[2]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[2]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[3]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[4]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[5]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[6]'
    # None = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[7]'
    ReportEmailName = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/input[8]'
    ReportEmailFormat = '//div[@id="email_report_modal"]/div/div/div[2]/form/fieldset/div/input'
    search_data = '//div[@id="bulk_api_resend_modal"]/div/div/div[2]/input'
    resend = '//div[@id="bulk_api_resend_modal"]/div/div/div[2]/input[2]'
    del_search_data = '//div[@id="bulk_delete_certificate_modal"]/div/div/div[2]/input'
    deleteChk = '//div[@id="bulk_delete_certificate_modal"]/div/div/div[2]/input[2]'
    bulk_action_criteria = '//form[@id="bulk_action"]/input'
    human_explain = '//form[@id="bulk_action"]/input[2]'
    search_result_count = '//form[@id="bulk_action"]/input[3]'
    filter_with_search_criteria = '//div[@id="mainsearch_config_div"]/ul/li[2]/a/input'
    show_all_linked_customers = '//div[@id="mainsearch_config_div"]/ul/li[3]/a/input'
    exact_match = '//div[@id="mainsearch_config_div"]/ul/li[5]/a/input'
    case_insensitive_exact_match = '//div[@id="mainsearch_config_div"]/ul/li[6]/a/input'
    begins_with_match = '//div[@id="mainsearch_config_div"]/ul/li[7]/a/input'
    full_wildcard_match = '//div[@id="mainsearch_config_div"]/ul/li[8]/a/input'
    # search_data = '//form[@id="run_search"]/input'
    bookmark_title = '//div[@id="bookmark_add"]/div/div/div[2]/div/div/input'
    from_email = '//div[@id="support_center_div"]/div/div/div[2]/div/div/input'
    subject = '//div[@id="support_center_div"]/div/div/div[2]/div[2]/div/input'
    # None = '//html/body/input'
    # None = '//html/body/input[2]'


class Links:
    @staticmethod
    def results_row_link(row):
        row = int(row)
        row += 1  # values start in tr[2]
        return '//*[@id="search_results_grid"]/tbody/tr[{}]/td[1]/a'.format(row)

    certificate_criteria = '//*[@id="CertificateCriteria"]/div[1]/h4/a'
    certificate_attributes = '//*[@id="CertificateAttributes"]/div[1]/h4/a'
    customer_criteria = '//*[@id="CustomerCriteria"]/div[1]/h4/a'
    customer_attributes = '//*[@id="CustomerAttributes"]/div[1]/h4/a'
    customer_exempt_exposure_reasons = '//*[@id="CustomerTaxCodes"]/div[1]/h4/a'
    certificate_exempt_exposure_reasons = '//*[@id="CertificateTaxCodes"]/div[1]/h4/a'
    certificate_invalid_reasons = '//*[@id="CertificateInvalidReason"]/div[1]/h4/a'
    validator_criteria = '//*[@id="ValidatorCriteria"]/div[1]/h4/a'
    retail_location = '//*[@id="Location"]/div[1]/h4/a'
    clear_search_results = '//*[@id="CertificateCriteria"]/div[1]/h4/span'


class CertificateCriteria:
    class Buttons:
        status_add_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button'
        status_remove_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button[2]'
        exposure_zone_add_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[4]/td[2]/div[2]/button'
        exposure_zone_remove_all = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[4]/td[2]/div[2]/button[2]'

    class Selects:
        has_customer = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr/td[4]/div/select'
        valid = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[2]/td[2]/div/select'
        expired = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[5]/td[2]/div/select'
        link_type = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[5]/td[4]/div/select'
        is_single = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[6]/td[2]/div/select'
        certificate_create_date_format = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[9]/td[2]/div/select'
        certificate_modified_date_format = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[10]/td[2]/div/select'
        certificate_signed_date_format = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[11]/td[2]/div/select'
        certificate_signed_date_day_range = '//div[@id="certificate_signed_date_relative_div"]/div[3]/select'
        certificate_expiration_date_format = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[12]/td[2]/div/select'
        certificate_expiration_date_day_range = '//div[@id="certificate_expiration_date_relative_div"]/div[3]/select'

    class Inputs:
        certificate_ids = '//*[@id="collapseCertificateCriteria"]/div/table/tbody/tr[1]/td[2]/textarea'
        status = '//div[@id="Certificate_certificate_status_id_chosen"]/ul/li/input'
        exposure_zone = '//div[@id="Certificate_exposure_zone_id_chosen"]/ul/li/input'
        exempt_percent = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[6]/td[4]/div/input'
        po_number = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[7]/td[2]/div/input'
        tax_number = '//div[@id="collapseCertificateCriteria"]/div/table/tbody/tr[7]/td[4]/div/input'
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


class CertificateAttributes:
    class Buttons:
        certificate_has_add_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div[3]/button'
        certificate_has_remove_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_does_not_have_add_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_does_not_have_remove_all = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        certificate_has = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr/td/div/select'
        certificate_does_not_have = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[2]/td/div/select'
        attribute_added_date = '//div[@id="collapseCertificateAttributes"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        certificate_has = '//div[@id="CertificateCode_has_chosen"]/ul/li/input'
        certificate_does_not_have = '//div[@id="CertificateCode_not_has_chosen"]/ul/li/input'
        certificate_attribute_added_date_begin = '//div[@id="certificate_attributes_date_exact_div"]/div/input'
        certificate_attribute_added_date_end = '//div[@id="certificate_attributes_date_exact_div"]/div[2]/input'
        certificate_attribute_added_date_ago = '//div[@id="certificate_attributes_date_relative_div"]/div/input'
        certificate_attribute_added_date_to = '//div[@id="certificate_attributes_date_relative_div"]/div[2]/input'


class CustomerCriteria:
    class Buttons:
        state_add_all = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button'
        state_remove_all = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[3]/td[2]/div[2]/button[2]'

    class Selects:
        customer_create_date_format = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[11]/td[2]/div/select'
        customer_modified_date_format = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[12]/td[2]/div/select'
        last_transaction_date_format = '//div[@id="collapseCustomerCriteria"]/div/table/tbody/tr[13]/td[2]/div/select'

    class Inputs:
        customer_numbers = '//*[@id="collapseCustomerCriteria"]/div/table/tbody/tr[1]/td[2]/textarea'
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
        customer_has_add_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div[3]/button'
        customer_has_remove_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div[3]/button[2]'
        customer_does_not_have_add_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div[3]/button'
        customer_does_not_have_remove_all = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        customer_has = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr/td/div/select'
        customer_does_not_have = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[2]/td/div/select'
        attribute_added_date = '//div[@id="collapseCustomerAttributes"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        customer_has = '//div[@id="CustomerCode_has_chosen"]/ul/li/input'
        customer_does_not_have = '//div[@id="CustomerCode_not_has_chosen"]/ul/li/input'
        customer_attributes_date_begin = '//div[@id="customer_attributes_date_exact_div"]/div/input'
        customer_attributes_date_end = '//div[@id="customer_attributes_date_exact_div"]/div[2]/input'
        customer_attributes_days_ago = '//div[@id="customer_attributes_date_relative_div"]/div/input'
        customer_attributes_days_to = '//div[@id="customer_attributes_date_relative_div"]/div[2]/input'


class CustomerExemptExposureReasons:
    class Buttons:
        customer_reason_in_exposure_zones_add_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div[3]/button'
        customer_reason_in_exposure_zones_remove_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div[3]/button[2]'
        customer_has_documented_reasons_add_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button'
        customer_has_documented_reasons_remove_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'
        customer_does_not_have_documented_reasons_add_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button'
        customer_does_not_have_documented_reasons_remove_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button[2]'
        customer_has_expected_reasons_add_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button'
        customer_has_expected_reasons_remove_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button[2]'
        customer_does_not_have_expected_reasons_add_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button'
        customer_does_not_have_expected_reasons_remove_all = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button[2]'

    class Selects:
        customer_reason_in_exposure_zones = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr/td/div/select'
        customer_has_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[2]/td/div/select'
        customer_does_not_have_documented_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[3]/td/div/select'
        customer_has_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[4]/td/div/select'
        customer_does_not_have_expected_reasons = '//div[@id="collapseCustomerTaxCodes"]/div/table/tbody/tr[5]/td/div/select'
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


class CertificateExemptExposureReasons:
    class Buttons:
        certificate_reason_in_exposure_zones_add_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div[3]/button'
        certificate_reason_in_exposure_zones_remove_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_has_documented_reasons_add_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_has_documented_reasons_remove_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div[3]/button[2]'
        certificate_does_not_have_documented_reasons_add_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button'
        certificate_does_not_have_documented_reasons_remove_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div[3]/button[2]'
        certificate_has_expected_reasons_add_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button'
        certificate_has_expected_reasons_remove_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div[3]/button[2]'
        certificate_does_not_have_expected_reasons_add_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button'
        certificate_does_not_have_expected_reasons_remove_all = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div[3]/button[2]'

    class Selects:
        certificate_reason_in_exposure_zones = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr/td/div/select'
        certificate_has_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[2]/td/div/select'
        certificate_does_not_have_documented_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[3]/td/div/select'
        certificate_has_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[4]/td/div/select'
        certificate_does_not_have_expected_reasons = '//div[@id="collapseCertificateTaxCodes"]/div/table/tbody/tr[5]/td/div/select'

    class Inputs:
        certificate_reason_in_exposure_zones = '//div[@id="CertificatesTaxCode_zone_has_chosen"]/ul/li/input'
        certificate_has_documented_reasons = '//div[@id="CertificatesTaxCode_documented_has_chosen"]/ul/li/input'
        certificate_does_not_have_documented_reasons = '//div[@id="CertificatesTaxCode_documented_not_has_chosen"]/ul/li/input'
        certificate_has_expected_reasons = '//div[@id="CertificatesTaxCode_expected_has_chosen"]/ul/li/input'
        certificate_does_not_have_expected_reasons = '//div[@id="CertificatesTaxCode_expected_not_has_chosen"]/ul/li/input'


class CertificateInvalidReasons:
    class Buttons:
        certificate_has_invalid_reasons_add_all = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div[3]/button'
        certificate_has_invalid_reasons_remove_all = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div[3]/button[2]'
        certificate_does_not_have_invalid_reasons_add_all = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div[3]/button'
        certificate_does_not_have_invalid_reasons_remove_all = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div[3]/button[2]'

    class Selects:
        certificate_has_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr/td/div/select'
        certificate_does_not_have_invalid_reasons = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[2]/td/div/select'
        reason_added_date = '//div[@id="collapseCertificateInvalidReason"]/div/table/tbody/tr[3]/td[2]/div/select'

    class Inputs:
        certificate_has_invalid_reasons = '//div[@id="InvalidReason_has_chosen"]/ul/li/input'
        certificate_does_not_have_invalid_reasons = '//div[@id="InvalidReason_not_has_chosen"]/ul/li/input'
        certificate_invalid_reasons_date_begin = '//div[@id="certificate_invalid_reasons_date_exact_div"]/div/input'
        certificate_invalid_reasons_date_end = '//div[@id="certificate_invalid_reasons_date_exact_div"]/div[2]/input'
        certificate_invalid_reasons_days_ago = '//div[@id="certificate_invalid_reasons_date_relative_div"]/div/input'
        certificate_invalid_reasons_days_to = '//div[@id="certificate_invalid_reasons_date_relative_div"]/div[2]/input'


class ValidatorCriteria:
    class Selects:
        validation_date = '//div[@id="collapseValidatorCriteria"]/div/table/tbody/tr[2]/td[2]/div/select'

    class Inputs:
        validator_names = '//*[@id="collapseValidatorCriteria"]/div/table/tbody/tr[1]/td[2]/textarea'
        certificate_validation_date_begin = '//div[@id="certificate_validation_date_exact_div"]/div/input'
        certificate_validation_date_end = '//div[@id="certificate_validation_date_exact_div"]/div[2]/input'
        certificate_validation_days_ago = '//div[@id="certificate_validation_date_relative_div"]/div/input'
        certificate_validation_days_to = '//div[@id="certificate_validation_date_relative_div"]/div[2]/input'


class RetailLocation:
    class Buttons:
        state_add_all = '//div[@id="collapseLocation"]/div/table/tbody/tr[4]/td[2]/div[2]/button'
        state_remove_all = '//div[@id="collapseLocation"]/div/table/tbody/tr[4]/td[2]/div[2]/button[2]'

    class Selects:
        limit_search = '//div[@id="collapseLocation"]/div/table/tbody/tr/td[2]/div/select'

    class Inputs:
        name = '//div[@id="collapseLocation"]/div/table/tbody/tr[2]/td[2]/div/input'
        location_codes = '//*[@id="collapseLocation"]/div/table/tbody/tr[3]/td[2]/textarea'
        state = '//div[@id="Location_state_id_chosen"]/ul/li/input'


class ResultsPage:
    class Buttons:
        search_again = '//div[@id="search_buttons"]/button[2]'
        save_search = '//div[@id="search_buttons"]/button[3]'
        email_report = '//div[@id="search_buttons"]/button[4]'
        export_report = '//div[@id="search_buttons"]/button[5]'

    class Selects:
        perform_actions_on_results = '//*[@id="bulk_action_selector"]'

    class Links:
        certificate_id_header = '//*[@id="jqgh_search_results_grid_id"]'
        zone_header = '//*[@id="jqgh_search_results_grid_exposure_zone"]'
        exempt_reason_header = '//*[@id="jqgh_search_results_grid_tax_code"]'
        effective_header = '//*[@id="jqgh_search_results_grid_signed_date"]'
        expiration_header = '//*[@id="jqgh_search_results_grid_expiration_date"]'
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