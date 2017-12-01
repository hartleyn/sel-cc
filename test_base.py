import atexit
import unittest
from selenium import webdriver

'''
	Created by Nick Hartley
	11/24/2017
'''

driver = webdriver.Chrome()
driver.maximize_window()

# Enabling Ctrl-C keyboard interrupts while running tests
unittest.installHandler()
	
def close_webdriver():
	driver.close()
	
atexit.register(close_webdriver)

