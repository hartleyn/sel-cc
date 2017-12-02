import time
import gspread
import datetime
import test_base
import xpath_locators
import id_locators
import os
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''
	Created by Nick Hartley
	12/01/2017
'''


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds_string = os.getcwd() + test_base.slash + 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_string, scope)
client = gspread.authorize(creds)


driver = test_base.driver


def verify_search_grid(row_num, cust_num, name, address, phone, certs):
	print('Checking result from row:', row_num - 1, '\n')

	actual_cust_num = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[3]').text
	print('Customer Number:')
	print('	', 'Extracted:', actual_cust_num)
	print('	', 'Expected: ', cust_num, '\n')
	assert actual_cust_num.lower() == cust_num.lower()
	time.sleep(2)
	actual_name = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[4]').text
	print('Name:')
	print('	', 'Extracted:', actual_name)
	print('	', 'Expected: ', name, '\n')
	assert actual_name.lower() == name.lower()
	time.sleep(2)
	actual_address = address_formatter(row_num)
	print('Address:')
	print('	', 'Extracted:', actual_address)
	print('	', 'Expected: ', address, '\n')
	assert actual_address.lower() == address.lower()
	time.sleep(2)
	actual_phone = driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[6]').text
	print('Phone:')
	print('	', 'Extracted:', phone_number_formatter(actual_phone))
	print('	', 'Expected: ', phone_number_formatter(phone), '\n')
	assert actual_phone == str(phone)
	time.sleep(2)
	actual_certs = get_certs_from_search_result_row(row_num)
	print('Certificates:')
	x = 0
	for cert in actual_certs:
		print('	', 'Extracted:', cert)
		print('	', 'Expected: ', certs[x], '\n')
		assert cert.lower() == certs[x].lower()
		x += 1
	time.sleep(2)
	print('PASS\n\n')
	
	
# Retrieve all the certs from a search result row
def get_certs_from_search_result_row(row_num):
	if driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[1]').is_displayed():
		x = 1
		certs = []
		
		try:
			while driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[' + str(x) + ']/td[1]').is_displayed() == True:
				certs.append(driver.find_element_by_xpath('//table[@id="QuickSearch"]/tbody/tr[' + str(row_num) + ']/td[7]/table/tbody/tr[' + str(x) + ']/td[3]').text)
				x += 1
		except NoSuchElementException:
			return certs

			
# Retrieve and format customer address from a search result row
def address_formatter(row_num):
	addr = driver.find_element_by_xpath('//tr[@id="' + str(row_num - 1) + '"]/td[5]').text
	
	stripped = addr.replace(',', '')

	parsed = stripped.split( )
	
	output = ''
	for x in range(0, len(parsed)):
		output += parsed[x]
		
		if x != len(parsed) - 1:
			output += ' '

	return output


# Phone number format helper
def phone_number_formatter(digits):
	number = str(digits)
	formatted = ''
	for x in range(0, len(number)):
		if x == 0:
			formatted += '('
		elif x == 6:
			formatted += ' - '
			
		formatted += number[x]
		
		if x == 2:
			formatted += ') '

	return formatted
	
	
	
	
	
	
	