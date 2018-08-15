import time
from test_base import driver
from manage_accounts import actions

__author__ = 'Nick Hartley'
# 5/27/2018


def verify_account_exists(account_name):
    actions.click('account / database name input', text=account_name)

    actions.click('filter button')

    time.sleep(2)
    result_account_name = driver.find_element_by_xpath('//*[@id="31549"]/td[3]').text

    assert account_name.lower() == result_account_name.lower()
