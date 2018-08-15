import time
from test_base import driver, debug
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/29/2018


def verify_all_states_assigned():
    if debug:
        print('Checking exposure zone assignments.')
    time.sleep(2)

    for col in range(1, 5):
        for row in range(1, 15):
            if debug:
                zone = driver.find_element_by_xpath('//*[@id="accordion"]/div/div[2]/table/tbody'
                                                    '/tr/td[{}]/table/tbody/tr[{}]/td[2]/p'.format(col, row)).text
                if debug:
                    print('Checking: {}'.format(zone))
            try:
                driver.find_element_by_xpath('//*[@id="accordion"]/div/div[2]/table/tbody'
                                             '/tr/td[{}]/table/tbody/tr[{}]/td[2]/p/span'.format(col, row))
                if debug:
                    print('    Assigned')
            except NoSuchElementException:
                zone = driver.find_element_by_xpath('//*[@id="accordion"]/div/div[2]/table/tbody'
                                                    '/tr/td[{}]/table/tbody/tr[{}]/td[2]/p'.format(col, row)).text
                assert False, '{} is unassigned.'.format(zone)
    print('All exposure zones assigned in nexus.')
    assert True
