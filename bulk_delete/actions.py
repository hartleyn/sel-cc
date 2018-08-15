import os
import time
import utilities.warnings as warn
import general.helpers as helpers
import bulk_delete.locations as locations
from test_base import slash, driver

__author__ = 'Nick Hartley'
# 5/19/2018


def click(target_name):
    target = target_name.lower()

    if target == 'choose file input':
        helpers.click_helper(locations.Inputs.choose_file)
    elif target == 'upload button':
        helpers.click_helper(locations.Buttons.upload)
    elif target == 'delete customer data button':
        helpers.click_helper(locations.Buttons.delete_customer_data)
    elif target == 'confirm modal ok button':
        helpers.click_helper(locations.Buttons.confirm_modal_ok)
    elif target == 'success modal cancel button':
        helpers.click_helper(locations.Buttons.confirm_modal_cancel)
    elif target == 'success modal close button':
        helpers.click_helper(locations.Buttons.confirm_modal_close)
    elif target == 'success modal ok button':  # Didn't work on bulk import page... Have to test
        helpers.click_helper(locations.Buttons.success_modal_ok)
    elif target == 'success modal close button':
        helpers.click_helper(locations.Buttons.success_modal_close)
    elif target == 'error modal ok button':
        helpers.click_helper(locations.Buttons.error_modal_ok)
    elif target == 'error modal close button':
        helpers.click_helper(locations.Buttons.error_modal_close)
    else:
        print(warn.INVALID_CLICK_TARGET)


def delete_customers_from_file(filename):
    filepath = '{0}{1}test_assets{1}{2}'.format(os.getcwd(), slash, filename)
    print('file:', filepath)
    driver.find_element_by_xpath(locations.Inputs.choose_file).send_keys(filepath)

    click('upload button')
    # time.sleep(2)
    click('delete customer data button')
    time.sleep(2)
    driver.find_element_by_xpath(locations.Buttons.success_modal_ok).click()
