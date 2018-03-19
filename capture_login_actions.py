import test_base
import time
import gspread
import os
import id_locators
import json
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

'''
	Created by Nick Hartley
	11/22/2017
'''



# Get driver and client from test_base prior to actions
driver = test_base.driver
client = test_base.client

def capture_open_portal():
	print('Navigating to CertCapture...\n')
	print('URL:', test_base.capture_link + '\n')
	driver.get(test_base.capture_link)
	
def certexpress_open_portal():
	print('Navigating to CertExpress...\n')
	print('URL:', test_base.express_link + '\n')
	driver.get(test_base.express_link)
	
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
		# Automatically pause for 7 seconds after login
		time.sleep(7)
	except TimeoutException as err:
		print(err)

def okta_login(environment):
	env = environment.lower()
	driver.get('https://avalara.okta.com/app/UserHome')
	
	try:
		check = driver.find_element_by_xpath('//*[@id="okta-signin-username"]').is_displayed()
		print('Logging in to Okta...')
		driver.find_element_by_xpath('//*[@id="okta-signin-username"]').click()
		driver.find_element_by_xpath('//*[@id="okta-signin-username"]').send_keys('nick.hartley@avalara.com')
		
		driver.find_element_by_xpath('//*[@id="okta-signin-password"]').click
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
				link_text = driver.find_element_by_xpath('//div[@id="main-content"]/div/div[2]/ul[2]/li[' + str(x) + ']/p').text
				print(link_text)
				
				if link_text.lower() == env:
					check = False
				else:
					x += 1
			except NoSuchElementException:
				check = False
		
		driver.find_element_by_xpath('//div[@id="main-content"]/div/div[2]/ul[2]/li[' + str(x) + ']/a').click()
		
		time.sleep(2)
		
		# Okta opens chosen portal in a new window
		driver.switch_to_window(driver.window_handles[1])
		
		# Always sleep to compensate for long Okta load times
		time.sleep(25)
			
def cc_login_from_credentials_json(name):
	# Creating a dictionary with parameters from cc_credentials.json
	with open('cc_credentials.json', 'r') as lines:
		obj = json.load(lines)
		
	name = name.title()
	
	try:
		user = obj['users'][name]['username']
		password = obj['users'][name]['password']
		
		print('Credentials found...\n')
		
		print('Attempting CertCapture login as', str(name) + '...\n')
		
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.login_email_field))
			)
			email = driver.find_element_by_id(id_locators.login_email_field)
			email.clear()
			email.send_keys(user)
			email.send_keys(Keys.RETURN)
		except TimeoutException:
			print('Timeout while entering username.')
		
		try:
			WebDriverWait(driver, 10).until(
				expected_conditions.visibility_of_element_located((By.ID, id_locators.login_password_field))
			)
			pass_field = driver.find_element_by_id(id_locators.login_password_field)
			pass_field.clear()
			pass_field.send_keys(password)
			pass_field.send_keys(Keys.RETURN)
			# Automatically pause for 7 seconds after login
			time.sleep(7)
		except TimeoutException:
			print('Timeout while entering password.')
			
	except KeyError:
		print('Credentials not found.')
	
	
	
	
	
	