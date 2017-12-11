import unittest
import test_base
import gspread
import datetime
import time
import os
import test_base
import requests


'''
	Created by Nick Hartley
	12/09/2017
'''

class ReportTestResult(unittest.TestResult):
	
	def startTestRun(self):
		unittest.TestResult.startTestRun(self)
		self.row_counter = 2
		self.now = str(datetime.date.today()) + '_' + str(int(time.time()))
		self.tb_locals = True
		
		if test_base.report == True:
			self.sheet = self.create_sheet()
			self.pass_count = 0
			self.fail_count = 0
			self.error_count = 0
			self.screens_dir = os.getcwd() + test_base.slash + 'screenshots' + test_base.slash + self.now
			os.mkdir(self.screens_dir)
			os.mkdir(self.screens_dir + test_base.slash + 'fails')
			os.mkdir(self.screens_dir + test_base.slash + 'errors')
		
	def startTest(self, test):
		unittest.TestResult.startTest(self, test)
		print('RUNNING TEST:', str(test).split( )[0] + '\n')
		
	def addSuccess(self, test):
		print('TEST PASSED\n')
		
		if test_base.report == True:
			self.sheet.update_cell(self.row_counter, 1, str(test).split( )[0])
			self.sheet.update_cell(self.row_counter, 2, 'X')
			self.row_counter += 1
			self.pass_count += 1
		
	def addFailure(self, test, err):
		unittest.TestResult.addFailure(self, test, err)
		print('TEST FAIL\n')
		fail = self.failures[len(self.failures)-1]
		test_name = str(fail[0]).split( )[0]
		
		
		file_path = self.screens_dir + test_base.slash + 'fails' + test_base.slash + test_name + '_' + self.now + '.png'
		test_base.driver.get_screenshot_as_file(file_path)

		if test_base.report == True:
			self.sheet.update_cell(self.row_counter, 1, test_name)
			self.sheet.update_cell(self.row_counter, 3, 'X')		
			self.sheet.update_cell(self.row_counter, 5, self.format_traceback(fail[1]))
			self.sheet.update_cell(self.row_counter, 6, file_path)
			self.row_counter += 1
			self.fail_count += 1
	
	def addError(self, test, err):
		unittest.TestResult.addError(self, test, err)
		print('TEST ERROR\n')
		
		error = self.errors[len(self.errors)-1]
		test_name = str(error[0]).split( )[0]
		
		
		file_path = self.screens_dir + test_base.slash + 'errors' + test_base.slash + test_name + '_' + self.now + '.png'
		test_base.driver.get_screenshot_as_file(file_path)
	
		if test_base.report == True:
			self.sheet.update_cell(self.row_counter, 1, test_name)
			self.sheet.update_cell(self.row_counter, 4,'X')		
			self.sheet.update_cell(self.row_counter, 5, self.format_traceback(error[1]))
			self.sheet.update_cell(self.row_counter, 6, file_path)
			self.row_counter += 1
			self.error_count += 1
	
	def format_traceback(self, traceback):
		trace = str(traceback).split('\n')
		string = ''
		for x in range(1, len(trace)-1):
			stripped = trace[x].strip( )
			print(stripped)
			string += stripped + '\n'
		return string
	
	def create_sheet(self):
		print('\nCreating test results Google sheet:', self.now + '\n')
		spreadsheet = test_base.client.open(test_base.report_sheet)
		worksheet = spreadsheet.add_worksheet(self.now, 150, 20)
		worksheet.update_cell(1, 1, 'Title')
		worksheet.update_cell(1, 2, 'Pass')
		worksheet.update_cell(1, 3, 'Fail')
		worksheet.update_cell(1, 4, 'Error')
		worksheet.update_cell(1, 5, 'Stack Trace')
		worksheet.update_cell(1, 6, 'Screenshot')		
		
		return worksheet
		
	def stopTestRun(self):
		unittest.TestResult.stopTestRun(self)
		
		if test_base.report == True:
			tests = str(self.testsRun) + ' tests ran'
			
			self.sheet.update_cell(self.row_counter, 1, tests)
			self.sheet.update_cell(self.row_counter, 2, 'Passed: ' + str(self.pass_count))
			self.sheet.update_cell(self.row_counter, 3, 'Failed: ' + str(self.fail_count))
			self.sheet.update_cell(self.row_counter, 4, 'Errors: ' + str(self.error_count))
			
			if test_base.slack == True:
				filename = self.now + '.xlsx'
				export = self.sheet.export(format='xlsx')
				f = open(filename, 'wb')
				f.write(export)
				f.close()

				url = 'https://slack.com/api/files.upload'
				headers = {'Authorization': 'token'}
				payload = {
					'token': test_base.slack_token, 
					'channels': test_base.slack_channels,
					'title': str(self.testsRun) + ' Tests Completed',
				}
				files = {'file': open(filename, 'rb')}
				r = requests.post(url, headers=headers, files=files, data=payload)
				print(r.json())
	
	
	
	
	
	
	
	
	
	
	
	
	
	