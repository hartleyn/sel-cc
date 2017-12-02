import atexit
import unittest
import platform
import os
import json
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

# Enabling Ctrl-C keyboard interrupts while running tests
unittest.installHandler()

# Establishing path separator based on the OS
slash = ''
sys = platform.system()
if sys == 'Darwin':
	slash = '/'
elif sys == 'Windows':
	slash = '\\'
else:
	slash = '/'
	
def close_webdriver():
	driver.close()
	
atexit.register(close_webdriver)

