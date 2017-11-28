import time
import capture_login_actions
import unittest
import datetime
import json
import gspread
import test_base
import data_entry_actions
import data_entry_actions_data
import xpath_locators
import general_actions
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\nick.hartley\\Desktop\\Auto\\client_secret.json', scope)
client = gspread.authorize(creds)

'''
driver = test_base.get_webdriver()
driver.get('https://beta.certcapture.com/url/f5549937e6')
capture_login_actions.cc_login_from_google_sheet('Nick')
driver.get('https://beta.certcapture.com/url/f5549937e6')
print(data_entry_actions.verify_search_count(1))
'''

driver = test_base.driver
now = datetime.datetime.now()

print(now)

'''
# Open CertCapture
capture_login_actions.capture_open_portal()

# Login to CertCapture
capture_login_actions.cc_login_from_google_sheet('Nick')

# Navigate to Data Entry -> Validate Documents
general_actions.go_to_validate_documents_page()
data_entry_actions.search_type_toggle('basic search')
time.sleep(3)
assert driver.find_element_by_xpath(xpath_locators.data_entry_search_field_filename).is_displayed() == False
print('cool')
time.sleep(5)


# Change company
data_entry_actions.change_company('QA_Automation_Clark')

# Change client
data_entry_actions.change_client('Data_Entry')


# Navigate to Data Entry -> Validate Documents
general_actions.go_to_validate_documents_page()
time.sleep(2)
actions = ActionChains(driver)
time.sleep(3)
actions.context_click()
time.sleep(5)


# 'Data Entry' link
driver.find_element_by_xpath('//div[@id="menu_container"]/ul/li[4]/a').click()
time.sleep(2)
# 'Validate Documents' link
driver.find_element_by_xpath('//div[@id="menu_container"]/ul/li[4]/ul/li[1]/a').click()
time.sleep(2)
data_entry_actions.go_to_upload()
time.sleep(2)
driver.find_element_by_id('StackDataFile').send_keys('open_pages')
time.sleep(5)
'''
'''
data_entry_actions.sort_search_results('filename')
time.sleep(2)
data_entry_actions.sort_search_results('customer number')
time.sleep(2)
data_entry_actions.sort_search_results('stage')
time.sleep(2)
data_entry_actions.sort_search_results('account')
time.sleep(2)
data_entry_actions.sort_search_results('exposure zone')
time.sleep(2)
data_entry_actions.sort_search_results('source')
time.sleep(2)
data_entry_actions.sort_search_results('priority')
time.sleep(2)
data_entry_actions.sort_search_results('pages')
time.sleep(2)
data_entry_actions.sort_search_results('age')
time.sleep(5)


capture_login_actions.capture_open_portal()
capture_login_actions.cc_login_from_google_sheet('Nick')
data_entry_actions.change_company('034Motorsport')
data_entry_actions.change_client('Tallhouse Co.')


with open('sample.json', 'r') as fp:
    obj = json.load(fp)
	
print(obj['test'])

today = datetime.date.today()

final_date = datetime.date(2017, 11, 10)
time = today - final_date
days = time.days

print(days)


driver = CaptureLoginActions.GetDriver()

CaptureLoginActions.CaptureOpenPortal()
CaptureLoginActions.CC_LoginFromGoogleSheet('Nick')
time.sleep(5)

# 'Data Entry' link
driver.find_element_by_xpath('//div[@id="menu_container"]/ul/li[4]/a').click()
time.sleep(2)
# 'Validate Documents' link
driver.find_element_by_xpath('//div[@id="menu_container"]/ul/li[4]/ul/li[1]/a').click()
time.sleep(5)
# 'Validate Documents' search button link
driver.find_element_by_id('DataEntrySearchButton').click()
time.sleep(2)
# 'Validate Documents' search result count
if driver.find_element_by_xpath('//td[@id="DataEntrySearch_toppager_right"]/div').is_displayed():
	print(True)
	results = driver.find_element_by_xpath('//td[@id="DataEntrySearch_toppager_right"]/div').text
	print(results)
else:
	print(False)

driver.close()


class Search(unittest.TestCase):

	def test_CC_DataEntry_Search_BasicSearch_0001():
		






driver = webdriver.Chrome()
driver.get("https://avalara.okta.com/login/default")

time.sleep(5)

elem = driver.find_element_by_id("okta-signin-username")
elem.clear()
elem.send_keys("nick.hartley@avalara.com")

pass_field = driver.find_element_by_id("okta-signin-password")
pass_field.clear()
pass_field.send_keys("WTcc2009")
pass_field.send_keys(Keys.RETURN)
#driver.close()

time.sleep(5)

beta4 = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/ul[2]/li[12]/a") # xpath to the beta4.certcapture Okta link
beta4.click()
'''