import os
import json
import atexit
import unittest
import platform
from selenium import webdriver

__author__ = 'Nick Hartley'
# 11/24/2017

'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('username', default=1)
parser.add_argument('password', default=2)
args = parser.parse_args()
'''

# Establishing path separator based on the OS
slash = ''
system = platform.system()
sys = system.lower()
if sys == 'darwin':
    slash = '/'
elif sys == 'windows':
    slash = '\\'
else:
    slash = '/'

project_directory = os.getcwd()

# Creating a dictionary with parameters from test_config.json
with open('test_assets{}test_config.json'.format(slash), 'r') as lines:
    obj = json.load(lines)

# Retrieving browser name
browser = obj['browser'].lower()

# Launching requested browser
if browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'ie' or browser == 'internet explorer':
    driver = webdriver.Ie()
elif browser == 'edge':
    driver = webdriver.Edge()
elif browser == 'safari' and sys == 'darwin':
    driver = webdriver.Safari()
elif browser == 'phantom':
    if sys == 'windows':
        driver = webdriver.PhantomJS('C:\\phantomjs.exe')  # CHANGE - TODO
    else:
        driver = webdriver.PhantomJS()
else:
    driver = webdriver.Chrome()  # Default to Chrome
    print('Browser error.')

# Maximize automation window	
driver.maximize_window()

# Retrieving tester's CertCapture and CertExpress environments
capture_link = obj["capture_env"]
express_link = obj["express_env"]

# Retrieving tester's download path
download_path = obj['download_path']

# Checking for reporting and slack report
report = obj['reporting'].lower()
slack = obj['slack_report'].lower()

if report == 'true' or report == 'on':
    report = True

    if slack == 'true' or slack == 'on':
        slack = True
        slack_token = obj['slack_token']
        slack_channels = obj['slack_channels']
else:
    report = False
    slack = False

# Retrieving the name of the Google sheet being used for reporting
report_sheet = obj['reporting_sheet']	

# Check for quick fail option
quick_fails = obj['quick_fails'].lower()

if quick_fails == 'true' or quick_fails == 'on':
    quick_fails = True


# use creds to create a client to interact with the Google Drive API - REMOVE - TODO
'''
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds_string = '{0}{1}test_assets{1}client_secret.json'.format(os.getcwd(), slash)
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_string, scope)
client = gspread.authorize(creds)
'''


# Check for debug setting
debug = obj['debug'].lower()

if debug == 'true' or debug == 'on':
    debug = True
else:
    debug = False


# Enabling Ctrl-C keyboard interrupts while running tests
unittest.installHandler()


# Quit function that closes all windows associated with the driver
def quit_webdriver():
    driver.quit()


# Registering the quit_webdriver function to run as the script exits	
atexit.register(quit_webdriver)
