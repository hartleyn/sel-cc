
__author__ = 'Nick Hartley'
# 3/6/18


class Buttons:
    add_account = '//button[@id="add_company_btn"]'
    provision_avatax_account = '//button[@id="provision_avatax_account"]'
    filter = '//button[@id="btnFilter"]'
    add_account_modal_upload_logo = '//button[@id="CompanyLogoFile"]'
    add_account_modal_close = '//div[@id="add_company"]/div/div/div[1]/button'
    add_account_modal_cancel = '//div[@id="div_add"]/button[2]'
    add_account_modal_reset = '//button[@id="insert_reset_btn"]'
    add_account_modal_add_account = '//button[@id="insert_company_btn"]'
    provision_avatax_account_modal_provision_avatax_account = '//button[@id="provision_avatax_account_btn"]'
    provision_avatax_account_modal_cancel = '//div[@id="provision_avatax_account_modal"]/div/div/div[3]/button[2]'
    provision_avatax_account_modal_close = '//div[@id="provision_avatax_account_modal"]/div/div/div[1]/button'
    first_top = '//td[@id="first_t_company_account_list_toppager"]'
    prev_top = '//td[@id="prev_t_company_account_list_toppager"]'
    next_top = '//td[@id="next_t_company_account_list_toppager"]'
    last_top = '//td[@id="last_t_company_account_list_toppager"]'
    first_bottom = '//td[@id="first_pager"]'
    prev_bottom = '//td[@id="prev_pager"]'
    next_bottom = '//td[@id="next_pager"]'
    last_bottom = '//td[@id="last_pager"]'
    page_select_top = '//*[@id="company_account_list_toppager_center"]/table/tbody/tr/td[4]/div/a'
    page_select_bottom = '//*[@id="pager_center"]/table/tbody/tr/td[3]/div/a'


class Inputs:
    account_database_name = '//input[@id="searchCompany"]'
    zuora_avatax_id = '//input[@id="searchZuora"]'
    add_account_modal_account_name = '//input[@id="name"]'
    add_account_modal_address_line_1 = '//input[@id="address_line1"]'
    add_account_modal_address_line_2 = '//input[@id="address_line2"]'
    add_account_modal_city = '//input[@id="city"]'
    add_account_modal_zip = '//input[@id="zip"]'
    add_account_modal_phone = '//input[@id="phone"]'
    add_account_modal_database_name = '//input[@id="database_name"]'
    add_account_modal_zuora_id = '//input[@id="zuora_id"]'
    add_account_modal_salesforce_id = '//input[@id="salesforce_id"]'
    add_account_modal_demo_account_checkbox = '//input[@id="internal"]'
    add_account_modal_sandbox_checkbox = '//input[@id="sandbox"]'
    provision_avatax_account_modal_import_ecms_data_checkbox = '//input[@id="import_ecms"]'
    provision_avatax_account_modal_avatax_account_id = '//input[@id="provision_avatax_account_id"]'
    filter_tier = '//div[@id="searchTier_chosen"]/ul/li/input'
    filter_server = '//div[@id="searchServer_chosen"]/ul/li/input'
    filter_status = '//div[@id="searchActive_chosen"]/ul/li/input'


class Links:
    account_list = '//a[@id="tab_list"]'
    account_statistics = '//a[@id="tab_statistics"]'
    id_header = '//div[@id="jqgh_company_account_list_id"]'
    name_header = '//div[@id="jqgh_company_account_list_name"]'
    tier_header = '//div[@id="jqgh_company_account_list_tier"]'
    zuora_id_header = '//div[@id="jqgh_company_account_list_zuora_id"]'
    database_server_header = '//div[@id="jqgh_company_account_list_hostname"]'
    database_name_header = '//div[@id="jqgh_company_account_list_database_name"]'


class Selects:
    add_account_modal_state_province = '//select[@id="state_id"]'
    add_account_modal_country = '//select[@id="country_id"]'
    add_account_modal_database_server = '//select[@id="database_server"]'
    add_account_modal_tier = '//select[@id="tier"]'
