
__author__ = 'Nick Hartley'
# 3/14/2018


class Buttons:
    generate_request_top = '//*[@id="content"]/div[1]/div/button'
    generate_request_bottom = '//*[@id="content"]/div[4]/button'
    add_exposure_zone = '//button[@id="add_shipto_state_or_zone_btn"]'
    add_shipto_zone_state_modal_add_shipto_state = '//button[@id="add_shipstate_btn"]'
    add_shipto_zone_state_modal_add_shipto_zone = '//button[@id="add_shipzone_btn"]'
    add_shipto_zone_state_modal_cancel = '//*[@id="ship_to_state_or_zone_modal"]/div/div/div[3]/button[4]'
    add_shipto_zone_state_modal_close = '//*[@id="ship_to_state_or_zone_modal"]/div/div/div[1]/button'


class Inputs:
    search_customer_name_number = '//input[@id="customer_number_search"]'
    customer = '//input[@id="customer_number_search"]'
    return_date = '//input[@id="return_date"]'
    email_address = '//input[@id="email_address"]'
    fax_number = '//input[@id="fax_number"]'
    exempt_reason = '//*[@id="tax_code_id_chosen"]/ul/li/input'


class Links:
    exposure_zones_select_all = '//a[@id="include_all_exposure_zones"]'
    exposure_zones_select_none = '//a[@id="include_no_exposure_zones"]'
    exposure_zones_select_default = '//a[@id="include_default_exposure_zones"]'
    exempt_reasons_select_all = '//a[@id="include_all_exposure_reasons"]'
    exempt_reasons_deselect_all = '//a[@id="include_no_exposure_reasons"]'
    templates_select_all = '//a[@id="include_all_templates"]'
    templates_deselect_all = '//a[@id="include_no_templates"]'
    add_shipto_zone_state_modal_state_tab = '//*[@id="tabs"]/li[1]/a'
    add_shipto_zone_state_modal_excise_certificates_tab = '//*[@id="tabs"]/li[2]/a'
    add_shipto_zone_state_modal_excise_licenses_tab = '//*[@id="tabs"]/li[3]/a'
    add_shipto_zone_state_modal_federal_withholding_tab = '//*[@id="AddShipZoneExposureZoneId3"]'
    add_shipto_zone_state_modal_custom_zone_tab = '//*[@id="tabs"]/li[5]/a'
    add_shipto_zone_state_modal_vat_tab = '//*[@id="tabs"]/li[6]/a'


class Selects:
    company = '//select[@id="client_id"]'
    delivery_method = '//select[@id="delivery_type"]'
    cover_letter = '//select[@id="cover_letter_id"]'
    document_type = '//select[@id="send-request-document-type"]'
    add_shipto_zone_state_modal_state = '//*[@id="AddShipStateStateId"]'
    add_shipto_zone_state_modal_excise_certificates = '//*[@id="AddShipZoneExposureZoneId5"]'
    add_shipto_zone_state_modal_excise_licenses = '//*[@id="AddShipZoneExposureZoneId3"]'
    add_shipto_zone_state_modal_federal_withholding = '//*[@id="AddShipZoneExposureZoneId2"]'
    add_shipto_zone_state_modal_custom_zone = '//*[@id="AddShipZoneExposureZoneId1"]'
    add_shipto_zone_state_modal_vat = '//*[@id="AddShipZoneExposureZoneId4"]'
