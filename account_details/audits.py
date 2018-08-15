import time
from test_base import driver
from account_details import actions
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/27/2018


def verify_company_exists(company_name):
    actions.tabs_click('Company Hierarchy')

    time.sleep(2)

    x = 1
    check = True
    while check:
        try:
            label = driver.find_element_by_xpath('//*[@id="company_entity"]/ul/li[{}]/div/span'.format(x)).text
            if company_name.lower() == label.lower():
                assert company_name.lower() == label.lower()
                print('Company found.')
                check = False
            else:
                x += 1
        except NoSuchElementException:
            print('Company not found.')
            assert False, print(company_name)  # Look will exit when there are no more elements present
