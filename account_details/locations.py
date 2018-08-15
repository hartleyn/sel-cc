
__author__ = 'Nick Hartley'
# 3/8/18


class Links:
    details_tab = '//ul[@id="company_account_tab"]/li[1]/a'
    company_hierarchy_tab = '//ul[@id="company_account_tab"]/li[2]/a'
    document_types_tab = '//ul[@id="company_account_tab"]/li[3]/a'
    features_tab = '//ul[@id="company_account_tab"]/li[4]/a'


class DetailsTab:
    class Inputs:
        account_name = '//form[@id="company_edit_form"]/div/input'
        zuora_id = '//form[@id="company_edit_form"]/div[2]/input'
        salesforce_id = '//form[@id="company_edit_form"]/div[3]/div/input'
        address_line_1 = '//form[@id="company_edit_form"]/div[3]/div[2]/input'
        address_line_2 = '//form[@id="company_edit_form"]/div[3]/div[3]/input'
        city = '//form[@id="company_edit_form"]/div[3]/div[4]/input'
        zip = '//form[@id="company_edit_form"]/div[3]/div[7]/input'
        phone = '//form[@id="company_edit_form"]/div[3]/div[8]/input'
        internal_checkbox = '//form[@id="company_edit_form"]/div[3]/div[11]/input'
        sandbox_checkbox = '//form[@id="company_edit_form"]/div[3]/div[12]/input'

    class Selects:
        country = '//select[@id="country_id"]'
        state_province = '//select[@id="state_id"]'

    class Buttons:
        update_account = '//div[@id="div_update"]/button'
        reset = '//div[@id="div_update"]/button[2]'

    class Links:
        update_company_logo = '//*[@id="details"]/div[1]/div[1]/div[1]/a'


class CompanyHierarchyTab:
    class Inputs:
        add_company_modal_display_name = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input'
        add_company_modal_legal_name = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[2]'
        add_company_modal_use_address_checkbox = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/label[3]/input'
        add_company_modal_address_line_1 = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[3]'
        add_company_modal_address_line_2 = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[4]'
        add_company_modal_city = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[5]'
        add_company_modal_zip = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[6]'
        add_company_modal_phone = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[7]'
        add_company_modal_fein = '//div[@id="add_client_entity_modal"]/div/div/div[2]/div/div/input[8]'
        add_company_grouping_modal_name = '//input[@id="division_name"]'

    class Buttons:
        add_company_grouping = '//div[@id="hierarchy"]/div/button'
        add_company_grouping_modal_add = '//button[@id="add_company_division"]'
        add_company_grouping_modal_cancel = '//*[@id="add_company_division_modal"]/div/div/div[3]/button[2]'
        add_company_grouping_modal_close = '//*[@id="add_company_division_modal"]/div/div/div[1]/button'
        add_company = '//div[@id="hierarchy"]/div/button[2]'
        add_company_modal_close = '//div[@id="add_client_entity_modal"]/div/div/div/button'
        add_company_modal_add = '//div[@id="add_client_modal"]/div/div/div[3]/button'
        add_company_modal_cancel = '//div[@id="add_client_entity_modal"]/div/div/div[3]/button[2]'

    class Selects:
        add_company_modal_country = '//select[@id="client_country"]'
        add_company_modal_state = '//select[@id="client_state"]'


class DocumentTypesTab:
    class Inputs:
        sales_and_use_tax_checkbox = '//div[@id="settings"]/div/table/tbody/tr/td/label/input'
        federal_withholding_checkbox = '//div[@id="settings"]/div/table/tbody/tr[2]/td/label/input'
        excise_licenses_checkbox = '//div[@id="settings"]/div/table/tbody/tr[3]/td/label/input'
        vat_checkbox = '//div[@id="settings"]/div/table/tbody/tr[4]/td/label/input'
        excise_certificates_checkbox = '//div[@id="settings"]/div/table/tbody/tr[5]/td/label/input'


class FeaturesTab:
    class Inputs:
        add_customer = '//div[@id="features"]/div/table/tbody/tr/td/label/input'
        api_exclude = '//div[@id="features"]/div/table/tbody/tr[2]/td/label/input'
        auto_add = '//div[@id="features"]/div/table/tbody/tr[3]/td/label/input'
        barcode_prefix = '//div[@id="features"]/div/table/tbody/tr[4]/td/label/input'
        campaigns_v2 = '//div[@id="features"]/div/table/tbody/tr[5]/td/label/input'
        configure_template = '//div[@id="features"]/div/table/tbody/tr[6]/td/label/input'
        cover_letter = '//div[@id="features"]/div/table/tbody/tr[7]/td/label/input'
        disable_certificates = '//div[@id="features"]/div/table/tbody/tr[8]/td/label/input'
        ecommerce_plugin = '//div[@id="features"]/div/table/tbody/tr[9]/td/label/input'
        force_auto = '//div[@id="features"]/div/table/tbody/tr[10]/td/label/input'
        mobile_app = '//div[@id="features"]/div/table/tbody/tr[11]/td/label/input'
        public_wizard = '//div[@id="features"]/div/table/tbody/tr[12]/td/label/input'
        restrict_the = '//div[@id="features"]/div/table/tbody/tr[13]/td/label/input'
        terms_and = '//div[@id="features"]/div/table/tbody/tr[14]/td/label/input'
        tin_check = '//div[@id="features"]/div/table/tbody/tr[15]/td/label/input'
        vat_id = '//div[@id="features"]/div/table/tbody/tr[16]/td/label/input'
        welcome_letter = '//div[@id="features"]/div/table/tbody/tr[17]/td/label/input'
