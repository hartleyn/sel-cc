import test_base
import time
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
	Created by Nick Hartley
	11/22/2017
'''



# Get driver and client from test_base prior to actions
driver = test_base.driver
client = test_base.client

def capture_open_portal():
	driver.get("https://beta.certcapture.com/logins/login")
	
def certexpress_open_portal():
	driver.get("https://beta.certexpress.com/home")
	
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
	
	email = driver.find_element_by_id("email")
	email.clear()
	email.send_keys(user)
	email.send_keys(Keys.RETURN)
	
	pass_field = driver.find_element_by_id("password")
	pass_field.clear()
	pass_field.send_keys(password)
	pass_field.send_keys(Keys.RETURN)
	# Automatically pause for 10 seconds after login
	time.sleep(10)

	
	
	
	
	
	
	
	
	
	
	
	
	