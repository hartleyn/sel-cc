from test_base import driver
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 6/11/2018


def verify_campaign_completion():
    print('Checking for campaign completion...')
    x = 2  # Visible information start in tr 2
    check = True
    while check:
        try:
            completion_percentage = driver\
                .find_element_by_xpath('//*[@id="completion_table"]/tbody/tr[{}]/td[5]/div/div'.format(x)).text

            customer_number = driver\
                .find_element_by_xpath('//*[@id="completion_table"]/tbody/tr[{}]/td[3]/label'.format(x)).text

            assert completion_percentage == '100%', \
                'Campaign incomplete.\n    Customer: {}\n    Completed: {}'\
                .format(customer_number, completion_percentage)
            print('Customer: {}\n    Response completed.'.format(customer_number))
        except NoSuchElementException:
            check = False
