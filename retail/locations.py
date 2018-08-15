
__author__ = 'Nick Hartley'
# 12/13/2017
# Updated: 5/24/2018


class Buttons:
    search = '//button[@id="launch_search_btn"]'
    new_exemption = '//button[@id="show_customer_modal"]'


class Links:
    customer_header = '//div[@id="jqgh_QuickSearch_customer_number"]'
    name_header = '//div[@id="jqgh_QuickSearch_name"]'
    address_header = '//div[@id="jqgh_QuickSearch_address"]'
    phone_header = '//div[@id="jqgh_QuickSearch_phone_number"]'
    certificates_header = '//div[@id="jqgh_QuickSearch_certs"]'

    @staticmethod
    def result_row_number(row):
        row = int(row)
        row += 1  # Nothing in first row
        xpath = '//table[@id="QuickSearch"]/tbody/tr[{}]'.format(row)
        return xpath


class ExemptionSearchModal:
    class Inputs:
        customer_name = '//input[@id="retail_customer_name"]'
        phone_number = '//input[@id="retail_phone_number"]'
        email = '//input[@id="retail_email"]'
        city = '//input[@id="retail_city"]'
        zip_code = '//input[@id="retail_zip"]'
        customer_number = '//input[@id="retail_customer_number"]'
        document_id = '//input[@id="retail_certificate_id"]'

    class Selects:
        customer_state = '//select[@id="retail_state"]'
        document_zone = '//select[@id="retail_certificate_zone"]'

    class Buttons:
        close = '//button[@id="exemption_search_modal_close"]'
        search = '//button[@id="customer_search_btn"]'
        clear_screen = '//button[@id="customer_clear_btn"]'


class CreateNewCustomerAndDocumentModal:
    class Inputs:
        name_of_business = '//input[@id="CustomerName"]'
        contact_email = '//input[@id="CustomerEmailAddress"]'
        business_phone = '//input[@id="CustomerPhoneNumber"]'
        address_line_1 = '//input[@id="CustomerAddressLine1"]'
        address_line_2 = '//input[@id="CustomerAddressLine2"]'
        business_city = '//input[@id="CustomerCity"]'
        business_zip_code = '//input[@id="CustomerZip"]'
        contact_name = '//input[@id="CustomerContactName"]'

    class Selects:
        business_country = '//select[@id="CustomerCountryId"]'
        business_state = '//select[@id="CustomerStateId"]'

    class Buttons:
        close = '//button[@id="customer_add"]/div/div/div[1]/button'
        next = '//button[@id="add_customer_btn"]'
        cancel = '//button[@id="customer_add"]/div/div/div[3]/div/div[2]/button'


class CustomerInformationModal:
    class Buttons:
        close = '//button[@id="customer_details_modal_close"]'
        edit_customer = '//span[@id="edit_customer"]'
        view = '//button[@id="view_certificate"]'
        print = '//div[@id="certificate_details_table"]/div[2]/div[2]/a'  # Actually a link
        download = '//a[@id="download_certificate"]'  # Actually a link
        renew_certificate = '//button[@id="certificate_renew"]'
        add_new_jurisdiction = '//button[@id="add_new_exposure"]'


class EditCustomerDetailsModal:
    class Buttons:
        close = '//div[@id="customer_edit_modal"]/div/div[1]/button'
        finish = '//button[@id="edit_customer_btn"]'
        cancel = '//button[@id="edit_customer_btn_cancel"]'

'''
class ButtonsOld:
    # = '//div[@id="division-dropdown"]/button'
    select_location = '//div[@id="location-dropdown"]/button'
    retail_search = '//div[@id="content"]/div[2]/div/div/button'
    retail_new_exemption = '//div[@id="content"]/div[2]/footer/button'
    search = '//div[@id="content"]/div[2]/footer/div/span/button'
    #new_exemption = '//div[@id="content"]/div[2]/footer/div/span[2]/button'
    #× = '//div[@id="clerk_gencert_modal"]/div/div/div/button'
    #× = '//div[@id="creation_results_modal"]/div/div/div/button'
    view = '//div[@id="creation_results_modal"]/div/div/div[2]/div[2]/div/button'
    #× = '//div[@id="customer_details_modal_dialog"]/div/div/button'
    view = '//div[@id="certificate_details_table"]/div[2]/div/button'
    renew_document = '//div[@id="certificate_details_table"]/div[2]/div[4]/button'
    add_new_jurisdiction = '//div[@id="certificate_details_modal_body"]/button'
    view = '//ul[@id="retail_mobile_nav_bar"]/li/button'
    download = '//ul[@id="retail_mobile_nav_bar"]/li[2]/button'
    jurisdiction = '//ul[@id="retail_mobile_nav_bar"]/li[3]/button'
    renew = '//ul[@id="retail_mobile_nav_bar"]/li[4]/button'
    #x = '//div[@id="certificate_preview"]/div/div/div/button'
    exemption_search_modal_close = '//div[@id="customer_search_modal"]/div/div/div/button'
    exemption_search_modal_search = '//div[@id="customer_search_modal"]/div/div/div[3]/div/div/button'
    exemption_search_modal_clear_screen = '//div[@id="customer_search_modal"]/div/div/div[3]/div/div[2]/button'
    new_customer_and_document_modal_next = '//div[@id="customer_add"]/div/div/div[3]/div/div/button'
    new_customer_and_document_modal_cancel = '//div[@id="customer_add"]/div/div/div[3]/div/div[2]/button'
    cancel = '//div[@id="customer_edit_modal"]/div/div[3]/button'
    finish = '//div[@id="customer_edit_modal"]/div/div[3]/button[2]'
    #x = '//div[@id="support_center_div"]/div/div/div/button'
    send = '//div[@id="support_center_div"]/div/div/div[3]/button'
    cancel = '//div[@id="support_center_div"]/div/div/div[3]/button[2]'


class Fields:
    # customer_name = 'retail_customer_name'
    # phone_number = 'retail_phone_number'
    # email = 'retail_email'
    # city = 'retail_city'
    # zip_code = 'retail_zip'
    # customer_number = 'retail_customer_number'
    # document_id = 'retail_certificate_id'
    name_of_business = 'CustomerName'
    contact_email = 'CustomerEmailAddress'
    main_business_phone_number = 'CustomerPhoneNumber'
    address_line_1 = 'CustomerAddressLine1'
    address_line_2 = 'CustomerAddressLine2'
    business_city = 'CustomerCity'
    business_zip_code = 'CustomerZip'
    contact_name = 'CustomerContactName'
    customer_number = 'CustomerCustomerNumber'
    customer_name = 'CustomerEditName'
    customer_email = 'CustomerEditEmailAddress'
    phone_number = 'CustomerEditPhoneNumber'
    address_line_1 = 'CustomerEditAddressLine1'
    address_line_2 = 'CustomerEditAddressLine2'
    city = 'CustomerEditCity'
    zip_code = 'CustomerEditZip'
    contact_name = 'CustomerEditContactName'
    customer_number = 'CustomerEditCustomerNumber'
    # customer_state = 'retail_state'
    # document_zone = 'retail_certificate_zone'
    business_country = 'CustomerCountryId'
    business_state = 'CustomerStateId'
    completed_for_a_corporation = 'CustomerCustomField82'
    tax_classification = 'CustomerCustomField76'


class Modals:
    exemption_search_modal = 'customer_search_modal'
    new_customer_and_document_modal = 'customer_add'


class Headers:
    customer_number = 'jqgh_QuickSearch_customer_number'
    name = 'jqgh_QuickSearch_name'
    address = 'jqgh_QuickSearch_address'
    phone = 'jqgh_QuickSearch_phone_number'
    certificates = 'jqgh_QuickSearch_certs'
'''
