import os
import glob
import time
from test_base import driver, slash, download_path
from general import locations
from utilities import warnings as warn
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

__author__ = 'Nick Hartley'
# 3/6/2018


def hover_settings_link(link_name):
    link = link_name.lower()

    if link == 'sysadmin':
        try:
            link_element = driver.find_element_by_partial_link_text('SysAdmin')
        except NoSuchElementException:
            click_helper(locations.Links.settings)
            link_element = driver.find_element_by_partial_link_text('SysAdmin')

        ActionChains(driver).move_to_element(link_element).perform()

    elif link == 'account':
        try:
            link_element = driver.find_element_by_partial_link_text('Account Settings')
        except NoSuchElementException:
            click_helper(locations.Links.settings)
            link_element = driver.find_element_by_partial_link_text('Account Settings')

        ActionChains(driver).move_to_element(link_element).perform()

    elif link == 'company':
        try:
            link_element = driver.find_element_by_partial_link_text('Company Settings')
        except NoSuchElementException:
            click_helper(locations.Links.settings)
            link_element = driver.find_element_by_partial_link_text('Company Settings')

        ActionChains(driver).move_to_element(link_element).perform()

    else:
        print('Invalid settings submenu requested.')


def ensure_child_is_visible_before_click(parent_location, child_location):
    if driver.find_element_by_xpath(child_location).is_displayed() is False:
        click_helper(parent_location)
        time.sleep(1)
    click_helper(child_location)


def ensure_child_is_visible_before_click_find_by_link(parent_location, link):
    try:
        link_element = driver.find_element_by_link_text(link)
    except NoSuchElementException:
        click_helper(parent_location)
        time.sleep(1)
        link_element = driver.find_element_by_link_text(link)
    click_find_by_link_helper(link_element.text)


def ensure_child_is_visible_before_click_find_by_link_document_or_certificate(parent_location):
    options = ('Document Search', 'Certificate Search')

    x = 0
    check = True
    while x < len(options) and check:
        try:
            # link_element = driver.find_element_by_link_text(options[x])
            driver.find_element_by_link_text(options[x])
            check = False
        except NoSuchElementException:
            if x == 0:
                click_helper(parent_location)
                time.sleep(5)
        try:
            # link_element = driver.find_element_by_link_text(options[x])
            driver.find_element_by_link_text(options[x])
            check = False
        except NoSuchElementException:
            x += 1
    click_find_by_link_helper(options[x])


def click_helper(location):
    """

    :rtype:
    """
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, location))
        )
        driver.find_element_by_xpath(location).click()
        # return driver.find_element_by_xpath(location)
    except TimeoutException:
        print(warn.TIMEOUT, 'click_helper', location)


def click_find_by_link_helper(link_name):
    time.sleep(2)
    driver.find_element_by_link_text(link_name).click()


def select_helper(location, value):
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, location))
        )
        driver.find_element_by_xpath(location).click()
        time.sleep(1)
        box = Select(driver.find_element_by_xpath(location))
        box.select_by_visible_text(value)
    except TimeoutException:
        print(warn.TIMEOUT, 'select_helper', location)


def click_or_select(location, **kwargs):
    if kwargs:
        try:
            select_helper(location, kwargs['select'])
        except KeyError:
            print(warn.INVALID_KWARG_SELECT)
    else:
        click_helper(location)


def state_input_field_click_or_select(location, **kwargs):
    """ Created to alleviate California v. Baja California issue
    :param location: xpath of the input element to be clicked;
                     As of 5/25/18, the two possible fields are the state input fields on the customer
                     and certificate search pages.

    :param kwargs: 'select' - states/exposure zones to be selected

    :return: No return
    """
    if kwargs:
        try:
            choices = kwargs['select']
            if type(choices) is not list:
                choices = [ choices ]
            loc = driver.find_element_by_xpath(location)
            click_helper(location)
            for choice in choices:
                loc.send_keys(choice)
                try:
                    driver.find_element_by_xpath('//*[@id="Customer_state_id_chosen"]/div/ul/li[2]')
                    x = 1
                    check = True
                    while check:
                        try:
                            elem = driver.find_element_by_xpath('//*[@id="Customer_state_id_chosen"]'
                                                                '/div/ul/li[{}]'.format(x))
                            text = elem.text
                            if text == choice:
                                elem.click()
                                check = False
                            else:
                                x += 1
                        except NoSuchElementException:
                            check = False
                            print('Something went wrong.')
                except NoSuchElementException:
                    loc.send_keys(Keys.RETURN)
        except KeyError:
            print(warn.INVALID_KWARG_SELECT)
    else:
        print('no kwargs')
        click_helper(location)


def input_field_click_or_select(location, **kwargs):
    if kwargs:
        try:
            choices = kwargs['select']
            if type(choices) is not list:
                choices = [ choices ]
            loc = driver.find_element_by_xpath(location)
            click_helper(location)
            for choice in choices:
                loc.send_keys(choice)
                loc.send_keys(Keys.RETURN)
        except KeyError:
            print(warn.INVALID_KWARG_SELECT)
    else:
        print('no kwargs')
        return click_helper(location)


def validation_customers_click_or_select(location, **kwargs):
    if kwargs:
        try:
            choices = kwargs['select']
            if type(choices) is not list:
                choices = [ choices ]
            loc = driver.find_element_by_xpath(location)
            click_helper(location)
            for choice in choices:
                loc.send_keys(choice)
                # Click first result row
                click_helper('//*[@id="dataEntryForm"]/div[3]/div[1]/div[4]/div/span/span/div/span/div[1]/div')
        except KeyError:
            print(warn.INVALID_KWARG_SELECT)
    else:
        print('no kwargs')
        return click_helper(location)


def single_request_recipient_click_or_select(location, **kwargs):
    time.sleep(2)
    if kwargs:
        try:
            customer = kwargs['select']
            keep_trying = True
            attempts = 0
            while keep_trying and attempts < 10:
                try:

                    ActionChains(driver).move_to_element(driver.find_element_by_xpath(location)) \
                        .click().send_keys(customer).perform()
                    print('passed first try block')
                    keep_trying = False
                except NoSuchElementException:
                    attempts += 1
                    time.sleep(2)
                    print('attempting to click input field again, failed attempt {}'.format(attempts))

            time.sleep(4)

            keep_trying = True
            attempts = 0
            while keep_trying and attempts < 10:
                try:

                    result = '//*[@id="content"]/div[2]/table/tbody/tr[1]/td/table' \
                             '/tbody/tr/td[2]/span/span/div/span/div[1]/div'
                    ActionChains(driver).move_to_element(
                        driver.find_element_by_xpath(result)).click().perform()
                    print('passed second try block')
                    keep_trying = False
                except NoSuchElementException:
                    attempts += 1
                    time.sleep(2)
                    print('attempting to click chosen option, failed attempt {}'.format(attempts))

        except KeyError:
            print(warn.INVALID_KWARG_SELECT)
    else:
        print('no kwargs')
        click_helper(location)


def textarea_field_click_or_type(location, **kwargs):
    if kwargs:
        values = kwargs['text']
        if type(values) is not list:
            values = [ values ]
        loc = driver.find_element_by_xpath(location)
        click_helper(location)
        for value in values:
            loc.send_keys(value)
            loc.send_keys(Keys.RETURN)
    else:
        return click_helper(location)


def click_or_type_date(location, **kwargs):
    if kwargs:
        try:
            text = kwargs['date']
            elem = driver.find_element_by_xpath(location)
            # date fields are sometimes prepopulated
            elem.clear()
            click_helper(location)
            elem.send_keys(text)
            elem.send_keys(Keys.RETURN)
            time.sleep(1)
        except KeyError:
            print(warn.INVALID_KWARG_TEXT)
    else:
        return click_helper(location)


def click_or_type(location, **kwargs):
    if kwargs:
        try:
            text = kwargs['text']
            elem = driver.find_element_by_xpath(location)
            click_helper(location)
            elem.send_keys(text)
        except KeyError:
            print(warn.INVALID_KWARG_TEXT)
    else:
        return click_helper(location)


def switch_to_new_window():
    print(driver.window_handles)
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to_window(windows[1])
        time.sleep(2)


def switch_to_old_window():
    print(driver.window_handles)
    windows = driver.window_handles
    driver.switch_to_window(windows[0])


def close_new_window():
    # Switch to and close pop up window. Then return to original window.
    print(driver.window_handles)
    time.sleep(2)
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to_window(windows[1])
        # print(driver.current_window_handle)
        time.sleep(2)
        driver.close()
        driver.switch_to_window(windows[0])
        time.sleep(2)
        # print(driver.window_handles)


def close_old_window():
    # Switch to and close pop up window. Then return to original window.
    print(driver.window_handles)
    time.sleep(2)
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to_window(windows[1])
        # print(driver.current_window_handle)
        time.sleep(2)
        driver.close()
        driver.switch_to_window(windows[0])
        time.sleep(2)


def close_extra_windows():
    windows = driver.window_handles
    base = windows[0]
    if len(windows) > 1:
        for window in windows:
            if window != base:
                driver.switch_to_window(window)
                time.sleep(1)
                driver.close()
    driver.switch_to_window(base)


def get_latest_pdf():
    full_path = '{}{}*.pdf'.format(download_path, slash)
    list_of_files = glob.glob(full_path)
    latest_file = max(list_of_files, key=os.path.getctime)

    return latest_file
