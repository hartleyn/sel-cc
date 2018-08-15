import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
# from test_base import args, slash, driver, capture_link, express_link
from test_base import slash, driver, capture_link, express_link
from utilities import warnings as warn
from . import locations

__author__ = 'Nick Hartley'
# 11/22/2017


def capture_open_portal():
    print('Navigating to CertCapture...\n')
    print('URL:', capture_link + '\n')
    driver.get(capture_link)


def certexpress_open_portal():
    print('Navigating to CertExpress...\n')
    print('URL:', express_link + '\n')
    driver.get(express_link)


# REMOVE - TODO
'''
def cc_login_from_google_sheet(name):
    print('Attempting CertCapture login as', str(name) + '...\n')
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("logins_sheet").sheet1

    x = 1

    while sheet.acell('A' + str(x)).value != name and x <= sheet.row_count + 1:
        if x == sheet.row_count + 1:
            print('User not found.\n')
            return
        else:
            x += 1

    user = sheet.acell('B' + str(x)).value
    password = sheet.acell('C' + str(x)).value
    print('Credentials found...\n')
    
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.user))
        )
        email = driver.find_element_by_xpath(locations.Inputs.user)
        email.clear()
        email.send_keys(user)
        email.send_keys(Keys.RETURN)
    except TimeoutException:
        print(warn.TIMEOUT)

    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.password))
        )
        pass_field = driver.find_element_by_xpath(locations.Inputs.password)
        pass_field.clear()
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)
        # Automatically pause for 7 seconds after login
        time.sleep(7)
    except TimeoutException:
        print(warn.TIMEOUT)
'''


def okta_login(environment):
    env = environment.lower()
    driver.get('https://avalara.okta.com/app/UserHome')

    try:
        check = driver.find_element_by_xpath('//*[@id="okta-signin-username"]').is_displayed()
        print('Logging in to Okta...')
        driver.find_element_by_xpath('//*[@id="okta-signin-username"]').click()
        driver.find_element_by_xpath('//*[@id="okta-signin-username"]').send_keys('nick.hartley@avalara.com')

        driver.find_element_by_xpath('//*[@id="okta-signin-password"]').click()
        driver.find_element_by_xpath('//*[@id="okta-signin-password"]').send_keys('Nb1886afc')

        driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()
        time.sleep(10)
    except NoSuchElementException:
        print('Already logged in to Okta...')
    finally:

        x = 1
        check = True
        while check:
            time.sleep(2)
            try:
                link_text = driver.find_element_by_xpath('//div[@id="main-content"]'
                                                         '/div/div[2]/ul[2]/li[{}]/p'.format(x)).text
                print(link_text)

                if link_text.lower() == env:
                    check = False
                else:
                    x += 1
            except NoSuchElementException:
                check = False

        driver.find_element_by_xpath('//div[@id="main-content"]/div/div[2]/ul[2]/li[{}]/a'.format(x)).click()

        time.sleep(2)

        # Okta opens chosen portal in a new window
        driver.switch_to_window(driver.window_handles[1])

        # Always sleep to compensate for long Okta load times
        time.sleep(20)


def cc_login_from_credentials_json(name):
    # Creating a dictionary with parameters from cc_credentials.json
    with open('test_assets{}cc_credentials.json'.format(slash), 'r') as lines:
        obj = json.load(lines)

    name = name.title()

    try:
        user = obj['users'][name]['username']
        password = obj['users'][name]['password']

        print('Credentials found...\n')

        print('Attempting CertCapture login as', str(name) + '...\n')

        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.user))
            )
            email = driver.find_element_by_xpath(locations.Inputs.user)
            email.clear()
            email.send_keys(user)
            email.send_keys(Keys.RETURN)
        except TimeoutException:
            print(warn.TIMEOUT, 'Process: Entering username.')

        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.password))
            )
            pass_field = driver.find_element_by_xpath(locations.Inputs.password)
            pass_field.clear()
            pass_field.send_keys(password)
            pass_field.send_keys(Keys.RETURN)
            # Automatically pause for 7 seconds after login
            time.sleep(7)
        except TimeoutException:
            print(warn.TIMEOUT, 'Process: Entering password.')

    except KeyError:
        print('Credentials not found.')


def cc_login_from_arguments():
    user = args.username
    password = args.password

    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.user))
        )
        email = driver.find_element_by_xpath(locations.Inputs.user)
        email.clear()
        email.send_keys(user)
        email.send_keys(Keys.RETURN)
    except TimeoutException:
        print(warn.TIMEOUT, 'Process: Entering username.')

    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locations.Inputs.password))
        )
        pass_field = driver.find_element_by_xpath(locations.Inputs.password)
        pass_field.clear()
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)
        # Automatically pause for 7 seconds after login
        time.sleep(7)
    except TimeoutException:
        print(warn.TIMEOUT, 'Process: Entering password.')
