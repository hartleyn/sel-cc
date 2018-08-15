import time
import unittest
from utilities.report_test_result import ReportTestResult

__author__ = 'Nick Hartley'
# 2/27/2018


class DummyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n************* TEST STARTING *************\n')

    def setUp(self):
        print('Running a test.')

    @staticmethod
    def test_dummy_1():
        time.sleep(4)
        assert True

    @staticmethod
    def test_dummy_2():
        time.sleep(3)
        assert False

    @staticmethod
    def test_dummy_3():
        time.sleep(4)
        num = 1 / 0
        assert num

    @staticmethod
    def test_dummy_4():
        time.sleep(2)
        assert True

    @staticmethod
    def test_dummy_5():
        time.sleep(5)
        assert False

    @staticmethod
    def test_dummy_6():
        time.sleep(3)
        num = 1 / 0
        assert num


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(DummyTest('test_dummy_1'))
    test_suite.addTest(DummyTest('test_dummy_2'))
    test_suite.addTest(DummyTest('test_dummy_3'))
    test_suite.addTest(DummyTest('test_dummy_4'))
    test_suite.addTest(DummyTest('test_dummy_5'))
    test_suite.addTest(DummyTest('test_dummy_6'))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ReportTestResult)
    runner.run(suite())
