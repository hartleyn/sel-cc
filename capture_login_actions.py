import test_base
import time
import gspread
import os
import id_locators
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

'''
	Created by Nick Hartley
	11/22/2017
'''



# Get driver and client from test_base prior to actions
driver = test_base.driver
client = test_base.client

def capture_open_portal():
	driver.get(test_base.capture_link)
	
def certexpress_open_portal():
	driver.get(test_base.express_link)
	
def cc_login_from_google_sheet(name):
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open("logins_sheet").sheet1
	
	x = 1
	
	while sheet.acell('A' + str(x)).value != name and x <= sheet.row_count + 1:
		if x == sheet.row_count + 1:
			print('User not found.')
			return
		else:
			x += 1
			
	user = sheet.acell('B' + str(x)).value
	password = sheet.acell('C' + str(x)).value
	
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.login_email_field))
		)
		email = driver.find_element_by_id(id_locators.login_email_field)
		email.clear()
		email.send_keys(user)
		email.send_keys(Keys.RETURN)
	except TimeoutException as err:
		print(err)
	
	try:
		WebDriverWait(driver, 10).until(
			expected_conditions.visibility_of_element_located((By.ID, id_locators.login_password_field))
		)
		pass_field = driver.find_element_by_id(id_locators.login_password_field)
		pass_field.clear()
		pass_field.send_keys(password)
		pass_field.send_keys(Keys.RETURN)
		# Automatically pause for 10 seconds after login
		time.sleep(10)
	except TimeoutException as err:
		print(err)
	
	
	
	
	
	
	
	
	
	
	
	
	