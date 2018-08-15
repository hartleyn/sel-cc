import json
from general import helpers
from retail import locations
from test_base import driver, slash
from utilities import warnings as warn
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 12/12/2017
# Updated: 5/24/18


def click(target_name):
    target = target_name.lower()

    if target == 'search button':
        location = locations.Buttons.search
        helpers.click_helper(location)
    elif target == 'new exemption button':
        location = locations.Buttons.new_exemption
        helpers.click_helper(location)
    elif target == 'customer header link':
        location = locations.Links.customer_header
        helpers.click_helper(location)
    elif target == 'name header link':
        location = locations.Links.name_header
        helpers.click_helper(location)
    elif target == 'address header link':
        location = locations.Links.address_header
        helpers.click_helper(location)
    elif target == 'phone header link':
        location = locations.Links.phone_header
        helpers.click_helper(location)
    elif target == 'certificate header link':
        location = locations.Links.certificates_header
        helpers.click_helper(location)
    elif target[0:10] == 'result row' and target[-4:] == 'link':
        if target[12] == ' ':
            number = target[11]  # Supports single digits
            location = locations.Links.result_row_number(number)
            helpers.click_helper(location)
        elif target[13] == ' ':
            number = target[11:13]  # Supports double digits
            location = locations.Links.result_row_number(number)
            helpers.click_helper(location)
        else:
            print(warn.SOME_PROBLEM)
    else:
        print(warn.INVALID_CLICK_TARGET)


def results_exposure_zone_click(row, zone):
    xpath = locations.Links.result_row_number(row)

    x = 1
    check = True
    while check:
        try:
            xpath = '{}/td[7]/table/tbody/tr[{}]/td[3]'.format(xpath, x)
            label = driver.find_element_by_xpath(xpath).text

            if zone.lower() == label.lower():
                check = False
                helpers.click_helper(xpath)
            else:
                x += 1
        except NoSuchElementException:
            check = False
            print('Exposure zone: {} not found in result row {}.'.format(zone, row))


def exemption_search_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer name input':
        location = locations.ExemptionSearchModal.Inputs.customer_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone number input':
        location = locations.ExemptionSearchModal.Inputs.phone_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'email input':
        location = locations.ExemptionSearchModal.Inputs.email
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.ExemptionSearchModal.Inputs.city
        helpers.click_or_type(location, **kwargs)
    elif target == 'zip code input':
        location = locations.ExemptionSearchModal.Inputs.zip_code
        helpers.click_or_type(location, **kwargs)
    elif target == 'customer number input':
        location = locations.ExemptionSearchModal.Inputs.customer_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'document id input':
        location = locations.ExemptionSearchModal.Inputs.document_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'customer state select':
        location = locations.ExemptionSearchModal.Selects.customer_state
        helpers.click_or_select(location, **kwargs)
    elif target == 'document zone select':
        location = locations.ExemptionSearchModal.Selects.document_zone
        helpers.click_or_select(location, **kwargs)
    elif target == 'close button':
        location = locations.ExemptionSearchModal.Buttons.close
        helpers.click_helper(location)
    elif target == 'search button':
        location = locations.ExemptionSearchModal.Buttons.search
        helpers.click_helper(location)
    elif target == 'clear screen button':
        location = locations.ExemptionSearchModal.Buttons.clear_screen
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def create_new_customer_and_certificate_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'name of business input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.name_of_business
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact email input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.contact_email
        helpers.click_or_type(location, **kwargs)
    elif target == 'business phone input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.business_phone
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'business city input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.business_city
        helpers.click_or_type(location, **kwargs)
    elif target == 'business zip code input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.business_zip_code
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact name input':
        location = locations.CreateNewCustomerAndDocumentModal.Inputs.contact_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'business country select':
        location = locations.CreateNewCustomerAndDocumentModal.Selects.business_country
        helpers.click_or_select(location, **kwargs)
    elif target == 'business state select':
        location = locations.CreateNewCustomerAndDocumentModal.Selects.business_state
        helpers.click_or_select(location, **kwargs)
    elif target == 'close button':
        location = locations.CreateNewCustomerAndDocumentModal.Buttons.close
        helpers.click_helper(location)
    elif target == 'next button':
        location = locations.CreateNewCustomerAndDocumentModal.Buttons.next
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CreateNewCustomerAndDocumentModal.Buttons.cancel
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def customer_information_modal_click(target_name):
    target = target_name.lower()

    if target == 'close button':
        location = locations.CustomerInformationModal.Buttons.close
        helpers.click_helper(location)
    elif target == 'edit customer button':
        location = locations.CustomerInformationModal.Buttons.edit_customer
        helpers.click_helper(location)
    elif target == 'view button':
        location = locations.CustomerInformationModal.Buttons.view
        helpers.click_helper(location)
    elif target == 'print button':
        location = locations.CustomerInformationModal.Buttons.print
        helpers.click_helper(location)
    elif target == 'download button':
        location = locations.CustomerInformationModal.Buttons.download
        helpers.click_helper(location)
    elif target == 'renew certificates button':
        location = locations.CustomerInformationModal.Buttons.renew_certificate
        helpers.click_helper(location)
    elif target == 'add new jurisdiction button':
        location = locations.CustomerInformationModal.Buttons.add_new_jurisdiction
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_customer_details_modal_click(target_name):  # Add input fields?
    target = target_name.lower()

    if target == 'close button':
        location = locations.EditCustomerDetailsModal.Buttons.close
        helpers.click_helper(location)
    elif target == 'finish button':
        location = locations.EditCustomerDetailsModal.Buttons.finish
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.EditCustomerDetailsModal.Buttons.cancel
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def parse_protractor_test_report():
    with open('C:{0}users{0}nick.hartley{0}desktop{0}cucumber{0}'
              'protractor-cucumber-framework-example{0}reports{0}json{0}retail-test.json'.format(slash)) as lines:
        obj = json.load(lines)
        steps = obj[0]['elements'][0]['steps']

    line = 'Checking result for test: {}'.format(obj[0]['elements'][0]['name'])
    print(line)

    for step in steps:
        line = '    {} - {}'.format(step['name'], step['result']['status'])
        print(line)
