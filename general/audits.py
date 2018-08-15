import time
from test_base import driver, debug
from general import actions, helpers
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/29/2018


def verify_enabled_public_certexpress_and_retail():
    time.sleep(2)

    actions.click('Company Settings')

    try:
        label = driver.find_element_by_xpath('//*[@id="menu_container"]/ul/li[7]/ul/li[3]/ul/li[8]/a').text
        if debug:
            print('{} enabled.'.format(label))
    except NoSuchElementException:
        assert False, 'Public CertExpress is not enabled'

    try:
        label = driver.find_element_by_xpath('//*[@id="menu_container"]/ul/li[8]/a').text
        if debug:
            print('{} enabled.'.format(label))
    except NoSuchElementException:
        assert False, 'Retail is not enabled.'

    assert True
    if debug:
        print('Public CertExpress and Retail are enabled.')


def verify_bulk_print(first_pdf):
    new_pdf = helpers.get_latest_pdf()

    assert new_pdf != first_pdf, 'Incorrect file found. Expected file to be something other than {}'.format(first_pdf)
