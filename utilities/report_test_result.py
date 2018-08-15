import unittest
import datetime
import time
import os
# import requests
import json
from test_base import slash, report, driver

__author__ = 'Nick Hartley'
# 12/09/2017


class ReportTestResult(unittest.TestResult):
    '''
    def __init__(self):
        unittest.TestResult.__init__(self, self.stream, descriptions=True, verbosity=1)
        self.now = ''
        self.run_start_time = 0
        self.run_stop_time = 0
        self.test_start_time = 0
        self.test_stop_time = 0
        self.pass_count = 0
        self.fail_count = 0
        self.error_count = 0
        self.run_time_elapsed = 0
        self.current_test = ''
        self.screens_dir = ''
        self.test_time_elapsed = []
        self.passed_tests = []
        self.failed_tests = []
        self.error_tests = []
        self.report_data = {}
    '''

    def startTestRun(self):
        unittest.TestResult.startTestRun(self)
        self.now = ''
        self.run_start_time = 0
        self.run_stop_time = 0
        self.test_start_time = 0
        self.test_stop_time = 0
        self.pass_count = 0
        self.fail_count = 0
        self.error_count = 0
        self.run_time_elapsed = 0
        self.current_test = ''
        self.screens_dir = ''
        self.test_time_elapsed = []
        self.passed_tests = []
        self.failed_tests = []
        self.error_tests = []
        self.report_data = {}
        self.now = str(datetime.date.today()) + '_' + str(int(time.time()))
        self.tb_locals = True

        if report:
            # self.sheet = self.create_sheet()
            self.run_start_time = time.time()
            self.screens_dir = '{0}{1}screenshots{1}{2}'.format(os.getcwd(), slash, self.now)
            # self.screens_dir = os.getcwd() + test_base.slash + 'screenshots' + test_base.slash + self.now
            os.mkdir(self.screens_dir)
            os.mkdir('{}{}fails'.format(self.screens_dir, slash))
            os.mkdir('{}{}errors'.format(self.screens_dir, slash))

    def startTest(self, test):
        unittest.TestResult.startTest(self, test)
        self.current_test = str(test).split()[0]
        print('\n-----------------------------------------------\n')
        print('RUNNING TEST:', self.current_test + '\n\n')

        if report:
            self.test_start_time = time.time()

    def addSuccess(self, test):
        print('TEST PASSED\n\n')

        if report:
            # self.sheet.update_cell(self.row_counter, 1, str(test).split( )[0])
            # self.sheet.update_cell(self.row_counter, 2, 'X')
            # self.row_counter += 1
            self.test_stop_time = time.time()
            elapsed = self.test_stop_time - self.test_start_time
            self.pass_count += 1
            self.passed_tests.append((self.current_test, elapsed))

    def addFailure(self, test, err):
        unittest.TestResult.addFailure(self, test, err)
        fail = self.failures[len(self.failures)-1]
        test_name = str(fail[0]).split( )[0]
        print('TEST FAIL')

        if report:  # Changed some stuff // RE-CHECK
            file_path = '{0}{1}fails{1}{2}_{3}.png'.format(self.screens_dir, slash, test_name, self.now)
            # file_path = self.screens_dir + test_base.slash + 'fails' + test_base.slash + test_name + '_' + self.now + '.png'
            # self.sheet.update_cell(self.row_counter, 1, test_name)
            # self.sheet.update_cell(self.row_counter, 3, 'X')
            if test_name[-11:] == '_protractor':
                # screenshot stuff
                file = 'C:{0}nick.hartley{0}desktop{0}cucumber{0}' \
                       'protractor-cucumber-framework-example{0}reports{0}json{0}example.json'.format(slash)
                # file = ('C:\\nick.hartley\\desktop\\cucumber\\'
                        # 'protractor-cucumber-framework-example\\reports\\json\\example.json')
                with open(file) as f:
                    obj = json.load(f)

                steps = obj[0]['elements'][0]['steps']
                cell_data = ''
                # failed = False - Might not need this?
                for step in steps:
                    result = step['result']['status']
                    if result == 'failed':
                        cell_data += step['name'] + '\n' + step['result']['error_message']
                        # failed = True
                    elif result == 'skipped' or result == 'undefined':
                        cell_data += step['name'] + '\n' + step['result']['status'] + '\n'
                # if cell_data != '':
                    # print(cell_data)
                    # self.sheet.update_cell(self.row_counter, 5, cell_data)

                try:
                    # img_str = steps[len(steps)-1]['embeddings'][0]['data']
                    os.rename('C:{0}users{0}nick.hartley{0}desktop{0}auto{0}protractor_tests{0}reports{0}screen.png'.format(slash), file_path)

                except KeyError:
                    driver.get_screenshot_as_file(file_path)
                    # self.sheet.update_cell(self.row_counter, 5, self.format_traceback(fail[1]))
            else:
                driver.get_screenshot_as_file(file_path)
                # self.sheet.update_cell(self.row_counter, 5, self.format_traceback(fail[1]))


            # self.sheet.update_cell(self.row_counter, 6, file_path)
            # self.row_counter += 1
            traceback = self.format_traceback(fail[1])
            self.test_stop_time = time.time()
            elapsed = self.test_stop_time - self.test_start_time
            self.fail_count += 1
            self.failed_tests.append((self.current_test, elapsed, traceback))

    def addError(self, test, err):
        unittest.TestResult.addError(self, test, err)
        error = self.errors[len(self.errors)-1]
        print('TEST ERROR')
        test_name = str(error[0]).split( )[0]

        if report:
            file_path = '{0}{1}errors{1}{2}_{3}.png'.format(self.screens_dir, slash, test_name, self.now)
            # self.screens_dir + test_base.slash + 'errors' + test_base.slash + test_name + '_' + self.now + '.png'
            driver.get_screenshot_as_file(file_path)
            traceback = self.format_traceback(error[1])
            self.test_stop_time = time.time()
            elapsed = self.test_stop_time - self.test_start_time
            self.error_count += 1
            self.error_tests.append((self.current_test, elapsed, traceback))

    @staticmethod
    def format_traceback(traceback):
        trace = str(traceback).split('\n')
        string = ''
        for x in range(1, len(trace)-1):
            stripped = trace[x].strip()
            print(stripped)
            string += stripped + '\n\n'
        return string

    # def create_sheet(self):
        # print('\nCreating test results Google sheet:', self.now + '\n')
        # spreadsheet = test_base.client.open(test_base.report_sheet)
        # worksheet = spreadsheet.add_worksheet(self.now, 150, 20)
        # worksheet.update_cell(1, 1, 'Title')
        # worksheet.update_cell(1, 2, 'Pass')
        # worksheet.update_cell(1, 3, 'Fail')
        # worksheet.update_cell(1, 4, 'Error')
        # worksheet.update_cell(1, 5, 'Stack Trace')
        # worksheet.update_cell(1, 6, 'Screenshot')

        # return worksheet

    def stopTestRun(self):
        unittest.TestResult.stopTestRun(self)

        if report:
            self.run_stop_time = time.time()
            elapsed = self.run_stop_time - self.run_start_time
            self.run_time_elapsed = elapsed

            self.report_data['title'] = 'Building Reports'
            self.report_data['date'] = self.now
            self.report_data['test_count'] = self.testsRun
            self.report_data['pass_count'] = self.pass_count
            self.report_data['fail_count'] = self.fail_count
            self.report_data['error_count'] = self.error_count
            self.report_data['passed'] = self.passed_tests
            self.report_data['failed'] = self.failed_tests
            self.report_data['error'] = self.error_tests

            build_html_report(self.report_data)

            # self.test_count = str(self.testsRun) + ' tests ran' -- self.testsRun contains the count!!

            # self.sheet.update_cell(self.row_counter, 1, tests)
            # self.sheet.update_cell(self.row_counter, 2, 'Passed: ' + str(self.pass_count))
            # self.sheet.update_cell(self.row_counter, 3, 'Failed: ' + str(self.fail_count))
            # self.sheet.update_cell(self.row_counter, 4, 'Errors: ' + str(self.error_count))

            '''
            if test_base.slack:
                filename = self.now + '.xlsx'  # Change to 'with' context manager
                # export = self.sheet.export(format='xlsx')
                f = open(filename, 'wb')
                # f.write(export)
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
                # print(r.json())
            '''


def build_html_report(data):
    from yattag import Doc

    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')
    with tag('head'):
        doc.asis('<meta charset="utf-8">')
        doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
        doc.asis('<link rel="stylesheet" '
                 'href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" '
                 'integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" '
                 'crossorigin="anonymous">')
        with tag('title'):
            text('Test Report')  # Change
        with tag('body', id='page-title'):
            with tag('div', klass='container'):
                with tag('div', klass='row'):
                    with tag('div', klass='col'):
                        with tag('h1', id='header'):
                            text(data['title'])
                        with tag('p'):
                            text(data['date'])
                    with tag('div', klass='col'):
                        with tag('p'):
                            text('{} tests ran'.format(data['test_count']))
                            doc.asis('<br>')
                            text('{} passed'.format(data['pass_count']))
                            doc.asis('<br>')
                            text('{} failed'.format(data['fail_count']))
                            doc.asis('<br>')
                            text('{} errors'.format(data['error_count']))
                with tag('div', klass='row'):
                    with tag('div', klass='col'):
                        with tag('div', klass='card'):
                            with tag('div', klass='card-header alert alert-success', role='alert'):
                                text('Passed Tests')
                            with tag('div', klass='accordion', id='accordionExample'):
                                with tag('div', klass='card-body'):
                                    x = 1
                                    for test in data['passed']:
                                        with tag('div', klass='card'):
                                            with tag('div', klass='card-header', id='heading'+str(x)):
                                                with tag('button',
                                                     ('data-toggle', 'collapse'),
                                                     ('data-target', '#collapse'+str(x)),
                                                     ('aria-expanded', 'false'),
                                                     ('aria-controls', 'collapse'+str(x)),
                                                     klass='btn btn-link collapsed',
                                                     type='button'):
                                                    text(test[0])
                                            with tag('div', ('aria-labelledby', 'heading'+str(x)), ('data-parent', 'accordionExample'), klass='collapse', id='collapse'+str(x)):
                                                with tag('div', klass='card-body'):
                                                    text('Test ran in {} seconds'.format(test[1]))
                                        x += 1
                    with tag('div', klass='col'):
                        with tag('div', klass='card'):
                            with tag('div', klass='card-header alert alert-danger', role='alert'):
                                text('Failed Tests')
                            with tag('div', klass='card-body'):
                                x = 1
                                for test in data['failed']:
                                    with tag('div', klass='card'):
                                        with tag('div', klass='card-header', id='heading' + str(x) + 'b'):
                                            with tag('button',
                                                     ('data-toggle', 'collapse'),
                                                     ('data-target', '#collapse' + str(x) + 'b'),
                                                     ('aria-expanded', 'false'),
                                                     ('aria-controls', 'collapse' + str(x) + 'b'),
                                                     klass='btn btn-link collapsed',
                                                     type='button'):
                                                text(test[0])
                                        with tag('div', ('aria-labelledby', 'heading' + str(x) + 'b'),
                                                 ('data-parent', 'accordionExample'), klass='collapse',
                                                 id='collapse' + str(x) + 'b'):
                                            with tag('div', klass='card-body'):
                                                text('Test ran in {} seconds'.format(test[1]))
                                                with tag('p'):
                                                    text(test[2])
                                    x += 1
                    with tag('div', klass='col'):
                        with tag('div', klass='card'):
                            with tag('div', klass='card-header alert alert-warning', role='alert'):
                                text('Error Tests')
                            with tag('div', klass='card-body'):
                                x = 1
                                for test in data['error']:
                                    with tag('div', klass='card'):
                                        with tag('div', klass='card-header', id='heading' + str(x) + 'c'):
                                            with tag('button',
                                                     ('data-toggle', 'collapse'),
                                                     ('data-target', '#collapse' + str(x) + 'c'),
                                                     ('aria-expanded', 'false'),
                                                     ('aria-controls', 'collapse' + str(x) + 'c'),
                                                     klass='btn btn-link collapsed',
                                                     type='button'):
                                                text(test[0])
                                        with tag('div', ('aria-labelledby', 'heading' + str(x) + 'c'),
                                                 ('data-parent', 'accordionExample'), klass='collapse',
                                                 id='collapse' + str(x) + 'c'):
                                            with tag('div', klass='card-body'):
                                                text('Test ran in {} seconds'.format(test[1]))
                                                with tag('p'):
                                                    text(test[2])
                                    x += 1
            doc.asis('<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" '
                     'integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" '
                     'crossorigin="anonymous"></script>')
            doc.asis('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" '
                     'integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" '
                     'crossorigin="anonymous"></script>')
            doc.asis('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" '
                     'integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" '
                     'crossorigin="anonymous"></script>')

    page = doc.getvalue()

    with open('utilities\\html_report.html', 'w') as f:
        f.write(page)

    print('HTML report created')
