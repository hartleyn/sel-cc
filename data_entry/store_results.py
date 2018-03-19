import test_base
import data_entry.audits
import datetime

'''
	Created by Nick Hartley
	12/13/2017
'''


driver = test_base.driver
client = test_base.client

def store_results_in_google_sheet(filename, sheetname, sheet_exists):
	count = data_entry.audits.data_entry_search_count()
	if sheet_exists:
		sheet = client.open(filename).worksheet(sheetname)
	else:
		sheet = client.open(filename).add_worksheet(sheetname, count + 1, 10)	
	
	for x in range(1, count + 1):
		x += 1
		cert_id = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[4]').text
		cust_num = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[5]').text
		stage = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[6]').text
		exposure = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[9]').text
		source = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[10]').text
		priority = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[11]').text
		pages = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[12]').text
		age = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[' + str(x) + ']/td[13]').text
		
		date = calculate_creation_date(int(age))
		
		x -= 1
		
		apply_to_google_sheet(sheet, x, cert_id, cust_num, stage, exposure, source, priority, pages, date)

def calculate_creation_date(days_diff):
	today = datetime.date.today()
	diff = datetime.timedelta(days=days_diff)
	return today - diff
		
def apply_to_google_sheet(sheet, row_num, cert_id, cust_num, stage, exposure, source, priority, pages, age):
	if row_num == 1:
		update_google_sheet_row(sheet, row_num, 'Document', 'Customer Number', 'Stage', 'Exposure Zone', 'Source', 'Priority', 'Pages', 'Age')

	row_num += 1
	update_google_sheet_row(sheet, row_num, cert_id, cust_num, stage, exposure, source, priority, pages, age)
	
def update_google_sheet_row(sheet, row_num, a, b, c, d, e, f, g, h):
	sheet.update_cell(row_num, 1, a)
	sheet.update_cell(row_num, 2, b)
	sheet.update_cell(row_num, 3, c)
	sheet.update_cell(row_num, 4, d)
	sheet.update_cell(row_num, 5, e)
	sheet.update_cell(row_num, 6, f)
	sheet.update_cell(row_num, 7, g)
	sheet.update_cell(row_num, 8, h)