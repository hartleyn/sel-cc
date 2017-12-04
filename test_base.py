import atexit
import unittest
import platform
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver

'''
	Created by Nick Hartley
	11/24/2017
'''

with open('test_config.json', 'r') as lines:
	obj = json.load(lines)

browser = obj['browser'].lower()
	
if browser == 'firefox':
	driver = webdriver.Firefox()
elif browser == 'chrome':
	driver = webdriver.Chrome()
elif browser == 'ie' or browser == 'internet explorer':
	driver = webdriver.Ie()
elif browser == 'edge':
	driver = webdriver.Edge()
else:
	print('Browser error.')

	
driver.maximize_window()


# Retrieving tester's download path from test_config.json
download_path = obj['download_path']

# Establishing path separator based on the OS
slash = ''
sys = platform.system()
if sys == 'Darwin':
	slash = '/'
elif sys == 'Windows':
	slash = '\\'
else:
	slash = '/'
	
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds_string = os.getcwd() + slash + 'client_secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_string, scope)
client = gspread.authorize(creds)

# Enabling Ctrl-C keyboard interrupts while running tests
unittest.installHandler()

def close_webdriver():
	driver.close()
	
atexit.register(close_webdriver)

