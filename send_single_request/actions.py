import time
import json
from general import helpers
from utilities import pdf_reader
from test_base import slash, driver, debug
from send_single_request import locations
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 3/14/2018


def click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'generate request button' or target == 'generate request top button':
        helpers.click_helper(locations.Buttons.generate_request_top)
        time.sleep(2)
    elif target == 'generate request bottom button':
        helpers.click_helper(locations.Buttons.generate_request_bottom)
        time.sleep(2)
    elif target == 'add exposure zone button' or target == 'add shipto state/zone button' \
            or target == 'add shipto zone button':
        helpers.click_helper(locations.Buttons.add_exposure_zone)
    elif target == 'customer search input':
        location = locations.Inputs.search_customer_name_number
        helpers.single_request_recipient_click_or_select(location, **kwargs)
    elif target == 'customer number / name input':
        location = locations.Inputs.customer
        helpers.single_request_recipient_click_or_select(location, **kwargs)
    elif target == 'return date input':
        location = locations.Inputs.return_date
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'email address input' or target == 'email input':
        location = locations.Inputs.email_address
        helpers.click_or_type(location, **kwargs)
    elif target == 'fax number input':
        location = locations.Inputs.fax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'exposure zone select all link':
        helpers.click_helper(locations.Links.exposure_zones_select_all)
    elif target == 'exposure zone select none link':
        helpers.click_helper(locations.Links.exposure_zones_select_none)
    elif target == 'exposure zone select default link':
        helpers.click_helper(locations.Links.exposure_zones_select_default)
    elif target == 'exempt reason select all link':
        helpers.click_helper(locations.Links.exempt_reasons_select_all)
    elif target == 'exempt reason deselect all link' or target == 'exempt reason de-select all link':
        helpers.click_helper(locations.Links.exempt_reasons_deselect_all)
    elif target == 'exemption certificate templates select all link' or target == 'templates select all link':
        helpers.click_helper(locations.Links.templates_select_all)
    elif target == 'exemption certificate templates deselect all link' \
            or target == 'exemption certificate templates de-select all link' \
            or target == 'templates deselect all link' \
            or target == 'templates de-select all link':
        helpers.click_helper(locations.Links.templates_deselect_all)
    elif target == 'company select':  # Disabled field...
        location = locations.Selects.company
        helpers.click_helper(location)
    elif target == 'delivery method select':
        location = locations.Selects.delivery_method
        helpers.click_or_select(location, **kwargs)
    elif target == 'cover letter select':
        location = locations.Selects.cover_letter
        helpers.click_or_select(location, **kwargs)
    elif target == 'exempt reason input' or target == 'document category input':
        location = locations.Inputs.exempt_reason
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'document type select':
        location = locations.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    else:
        print('Invalid target requested.')


def add_shipto_zone_state_modal_click(target_name):
    target = target_name.lower()

    if target == 'state link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_state_tab)
    elif target == 'excise certificates link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_excise_certificates_tab)
    elif target == 'excise licenses link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_excise_licenses_tab)
    elif target == 'federal withholding link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_federal_withholding_tab)
    elif target == 'custom zone link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_custom_zone_tab)
    elif target == 'vat link':
        helpers.click_helper(locations.Links.add_shipto_zone_state_modal_vat_tab)
    elif target == 'state select':
        location = locations.Selects.add_shipto_zone_state_modal_state
        helpers.click_helper(location)
    elif target == 'excise certificates select':
        location = locations.Selects.add_shipto_zone_state_modal_excise_certificates
        helpers.click_helper(location)
    elif target == 'excise licenses select':
        location = locations.Selects.add_shipto_zone_state_modal_excise_licenses
        helpers.click_helper(location)
    elif target == 'federal withholding select':
        location = locations.Selects.add_shipto_zone_state_modal_federal_withholding
        helpers.click_helper(location)
    elif target == 'custom zone select':
        location = locations.Selects.add_shipto_zone_state_modal_custom_zone
        helpers.click_helper(location)
    elif target == 'vat select':
        location = locations.Selects.add_shipto_zone_state_modal_vat
        helpers.click_helper(location)
    elif target == 'add shipto state button':
        location = locations.Buttons.add_shipto_zone_state_modal_add_shipto_state
        helpers.click_helper(location)
    elif target == 'add shipto zone button':
        location = locations.Buttons.add_shipto_zone_state_modal_add_shipto_zone
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.Buttons.add_shipto_zone_state_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button' or target == 'x button':
        location = locations.Buttons.add_shipto_zone_state_modal_close
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


'''
def select_document_type(doc_type):
    doc_type = doc_type.title()

    if doc_type == 'Sales And Use Tax':
        doc_type = 'Sales and Use Tax'
    elif doc_type == 'Vat':
        doc_type = 'VAT'

    helpers.select_helper(locations.Selects.document_type, doc_type)



def select_company(company):
    helpers.select_helper(locations.Selects.company, company)



def select_cover_letter(letter):
    letter = letter.title()

    if letter == 'Standard_Request':
        letter = letter.upper()
    elif letter[-17:] == 'Sales And Use Tax':
        letter = letter[:-17] + 'Sales and Use Tax'
    elif letter == 'Standard Request - Vat Identification Information':
        letter = 'Standard Request - VAT Identification Information'

    helpers.select_helper(locations.Selects.cover_letter, letter)


def select_delivery_method(method):
    helpers.select_helper(locations.Selects.delivery_method, method.capitalize())


def set_email_address(email):
    field = click('email address input')
    field.clear()
    field.send_keys(email)
'''


def select_exempt_reasons(reasons):
    if debug:
        print('Selecting reasons')

    # Cast argument to a list if one wasn't passed in
    if type(reasons) is not list:
        reasons = [reasons]

    for reason in reasons:
        if debug:
            print('clicking exempt reason input, searching for {}'.format(reason))
            time.sleep(2)
        click('exempt reason input')

        x = 1
        check = True

        while check:
            try:
                if reason.upper() == driver.find_element_by_xpath('//*[@id="tax_code_id_chosen"]'
                                                                  '/div/ul/li[{}]'.format(x)).text:
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="tax_code_id_chosen"]/div/ul/li[{}]'.format(x)).click()
                    check = False
                else:
                    x += 1
            except NoSuchElementException:
                print('Unable to locate exempt reason.')
                check = False


def select_exposure_zones(zones):  # :O - Almost 100 lines?
    if debug:
        print('Selecting zones')

    # Cast argument to a list if one wasn't passed in
    if type(zones) is not list:
        zones = [zones]

    # Click the 'Select None' link to ensure that all zones are unchecked
    click('exposure zone select none link')

    current_zone_type = ''

    for zone in zones:

        z = zone.lower()
        if z == 'state' or z == 'excise certificates' or z == 'excise licenses' or z == 'federal withholding' or z == 'custom zone' or z == 'vat':
            current_zone_type = z
        else:

            x = 1
            check = True
            found = False

            while check:
                try:
                    label = driver.find_element_by_xpath('//*[@id="send_request_exposures_table"]'
                                                         '/tbody/tr[{}]/td[1]/div/label/span[2]'.format(x)).text
                    print('Zone:', label)

                    if zone.title() == label or label == zone.title() + ' Sales Tax':
                        check = False
                        found = True
                        print('found')
                    else:
                        x += 1
                except NoSuchElementException:
                    check = False

            if found:
                driver.find_element_by_xpath('//*[@id="send_request_exposures_table"]'
                                             '/tbody/tr[{}]/td[1]/div/label/input'.format(x)).click()
            else:
                if current_zone_type == '':
                    print('No zone type set. Pass "state", "excise certificates", "excise licenses", '
                          '"federal withholding", "custom zone", or "vat" in the zones array to set zone type.')
                else:
                    zone = zone.title()
                    time.sleep(2)
                    click('add shipto zone button')

                    if current_zone_type == 'state':
                        try:
                            add_shipto_zone_state_modal_click('state link')
                            helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_state, zone)
                            add_shipto_zone_state_modal_click('add shipto state button')
                        except NoSuchElementException:
                            if zone.endswith(' Sales Tax'):
                                zone_list = zone.split( )
                                new_zone = ''

                                for x in range(0, len(zone_list)):
                                    if zone_list[x] != 'Sales' or zone_list[x] != 'Tax':
                                        new_zone += zone_list[x]

                                zone = new_zone
                            else:
                                zone += ' Sales Tax'

                            try:
                                add_shipto_zone_state_modal_click('state link')
                                helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_state, zone)
                                add_shipto_zone_state_modal_click('add shipto state button')
                            except NoSuchElementException:
                                print('Sales and Use Tax exposure zone not found.')

                    elif current_zone_type == 'excise certificates':
                        add_shipto_zone_state_modal_click('excise certificates link')
                        helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_excise_certificates, zone)
                        add_shipto_zone_state_modal_click('add shipto zone button')
                    elif current_zone_type == 'excise licenses':
                        add_shipto_zone_state_modal_click('excise licenses link')
                        helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_excise_licenses, zone)
                        add_shipto_zone_state_modal_click('add shipto zone button')
                    elif current_zone_type == 'federal withholding':
                        add_shipto_zone_state_modal_click('federal withholding link')
                        helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_federal_withholding, zone)
                        add_shipto_zone_state_modal_click('add shipto zone button')
                    elif current_zone_type == 'custom zone':
                        add_shipto_zone_state_modal_click('custom zone link')
                        helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_custom_zone, zone)
                        add_shipto_zone_state_modal_click('add shipto zone button')
                    elif current_zone_type == 'vat':
                        add_shipto_zone_state_modal_click('vat link')
                        helpers.select_helper(locations.Selects.add_shipto_zone_state_modal_vat, zone)
                        add_shipto_zone_state_modal_click('add shipto zone button')
                    else:
                        print('Some zone type error occurred.')


def store_request_url_in_json():
    link = pdf_reader.get_request_link_from_request_pdf()
    print('Opening request link:', link)

    my_data = {'url': link}

    with open('send_single_request{}request.json'.format(slash), 'w') as f:
        json.dump(my_data, f)
