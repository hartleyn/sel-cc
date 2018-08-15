import time
import test_base
import utilities.warnings as warn
import dashboard.locations as locations
import general.helpers as helpers
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/19/2018

driver = test_base.driver


def click(target_name):
    target = target_name.lower()
    
    if target == 'add widget button':
        location = locations.Buttons.add_widget
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target, 'dashboard')


def message_center_click(target_name):
    target = target_name.lower()

    if target == 'minimize button':
        location = locations.MessageCenter.Buttons.minimize
        helpers.click_helper(location)
    elif target == 'maximize button':
        location = locations.MessageCenter.Buttons.maximize
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.MessageCenter.Buttons.close
        helpers.click_helper(location)
    elif target == 'prev button':
        location = locations.MessageCenter.Buttons.prev
        helpers.click_helper(location)
    elif target == 'next button':
        location = locations.MessageCenter.Buttons.next
        helpers.click_helper(location)
    elif target == 'date header link':
        location = locations.MessageCenter.Links.date_header
        helpers.click_helper(location)
    elif target == 'refresh link':
        location = locations.MessageCenter.Links.refresh
        helpers.click_helper(location)
    elif target == 'full report link':
        location = locations.MessageCenter.Links.full_report
        helpers.click_helper(location)
    elif target[0:12] == 'message row' and target[-4:] == 'link':
        if target[13] == ' ':
            row = target[12]
        elif target[14] == ' ':
            row = target[12:14]
        else:
            row = '0'
            print(warn.SOME_PROBLEM)
        location = locations.MessageCenter.Links.message_link_row(row)
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target, 'dashboard - message center')


def download_center_click(target_name):
    target = target_name.lower()

    if target == 'minimize button':
        location = locations.DownloadCenter.Buttons.minimize
        helpers.click_helper(location)
    elif target == 'maximize button':
        location = locations.DownloadCenter.Buttons.maximize
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.DownloadCenter.Buttons.close
        helpers.click_helper(location)
    elif target == 'prev button':
        location = locations.DownloadCenter.Buttons.prev
        helpers.click_helper(location)
    elif target == 'next button':
        location = locations.DownloadCenter.Buttons.next
        helpers.click_helper(location)
    elif target == 'date header link':
        location = locations.DownloadCenter.Links.created_header
        helpers.click_helper(location)
    elif target == 'refresh link':
        location = locations.DownloadCenter.Links.refresh
        helpers.click_helper(location)
    elif target == 'full report link':
        location = locations.DownloadCenter.Links.full_report
        helpers.click_helper(location)
    elif target[0:12] == 'download row' and target[-4:] == 'link':
        if target[14] == ' ':
            row = target[13]
        elif target[15] == ' ':
            row = target[13:15]
        else:
            row = '0'
            print(warn.SOME_PROBLEM)
        location = locations.DownloadCenter.Links.download_link_row(row)
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target, 'dashboard - download center')


def wait_for_download_center_job(title):
    attempts = 0
    check = True
    while check and attempts < 10:
        refresh = False
        try:
            job_title = driver.find_element_by_xpath('//*[@id="download_center_table"]/tbody/tr[2]/td[4]').text
            if title == job_title:
                try:
                    driver.find_element_by_xpath('//*[@id="download_center_table"]/tbody/tr[2]/td[6]/span/a')
                    check = False
                    print('download ready, downloading {}'.format(job_title))
                    time.sleep(2)
                    download_center_click('download row 1 link')
                    # Wait for download
                    time.sleep(10)
                except NoSuchElementException:
                    # If the 'Download' link is not yet visible
                    refresh = True
            else:
                # If the expected job is not yet visible in the download center
                refresh = True
        except NoSuchElementException:
            # If no jobs are visible in the download center
            refresh = True
        finally:
            if refresh:
                download_center_click('refresh link')
                attempts += 1
                time.sleep(5)


def wait_for_campaign_round_download_job(title):
    attempts = 0
    check = True
    while check and attempts < 10:
        refresh = False
        try:
            job_title = driver.find_element_by_xpath('//*[@id="download_center_table"]/tbody/tr[2]/td[4]').text
            if job_title[0:18] == 'Download for Round' and job_title[-len(title):] == title:
                try:
                    driver.find_element_by_xpath('//*[@id="download_center_table"]/tbody/tr[2]/td[6]/span/a')
                    check = False
                    download_center_click('download row 1 link')
                except NoSuchElementException:
                    # If the 'Download' link is not yet visible
                    refresh = True
            else:
                # If the expected job is not yet visible in the download center
                refresh = True
        except NoSuchElementException:
            # If no jobs are visible in the download center
            refresh = True
        finally:
            if refresh:
                download_center_click('refresh link')
                attempts += 1
                time.sleep(5)
    time.sleep(5)
