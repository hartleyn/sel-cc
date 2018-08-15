import os
import time
from general import helpers
from bulk_import import locations
from test_base import slash, driver
from utilities import warnings as warn

__author__ = 'Nick Hartley'
# 3/14/2018


def click(target_name):
    target = target_name.lower()

    if target == 'choose file input':
        return helpers.click_helper(locations.Inputs.choose_file)
    elif target == 'upload button':
        return helpers.click_helper(locations.Buttons.upload)
    elif target == 'import customer data button':
        return helpers.click_helper(locations.Buttons.import_customer_data)
    elif target == 'success modal ok button':  # Not working for some reason? Other seem to work fine.
        return helpers.click_helper(locations.Buttons.success_modal_ok)
    elif target == 'success modal close button':
        return helpers.click_helper(locations.Buttons.success_modal_close)
    elif target == 'error modal ok button':
        return helpers.click_helper(locations.Buttons.error_modal_ok)
    elif target == 'error modal close button':
        return helpers.click_helper(locations.Buttons.error_modal_close)
    else:
        print(warn.INVALID_CLICK_TARGET)


def import_customers_from_file(filename):
    filepath = '{0}{1}test_assets{1}{2}'.format(os.getcwd(), slash, filename)
    print('file:', filepath)
    driver.find_element_by_xpath(locations.Inputs.choose_file).send_keys(filepath)

    click('upload button')
    # time.sleep(2)
    click('import customer data button')
    time.sleep(2)
    driver.find_element_by_xpath(locations.Buttons.success_modal_ok).click()
