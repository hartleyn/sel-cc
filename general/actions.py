import time
from test_base import driver
from general import helpers, locations
from selenium.webdriver.common.keys import Keys

__author__ = 'Nick Hartley'
# 12/12/2017


def click(link_name):
    print('Attempting to click {}...\n'.format(link_name))
    link = link_name.title()

    if link == 'Profile':
        helpers.click_helper(locations.Links.profile)
    elif link == 'My Profile':
        helpers.ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.my_profile)
    elif link == 'Message Center':
        helpers.ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.message_center)
    elif link == 'Download Center':
        helpers.ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.download_center)
    elif link == 'Logout':
        helpers.ensure_child_is_visible_before_click(locations.Links.profile, locations.Links.logout)
    elif link == 'Dashboard':
        helpers.click_helper(locations.Links.dashboard)
    elif link == 'Search':
        helpers.click_helper(locations.Links.search)
    elif link == 'Customer Search':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.search, link)
    elif link == 'Document Search' or link == 'Certificate Search':
        helpers.ensure_child_is_visible_before_click_find_by_link_document_or_certificate(locations.Links.search)
    elif link == 'Job Search':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.search, link)
    elif link == 'Saved Searches':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.search, link)
    elif link == 'Customers':
        helpers.click_helper(locations.Links.customers)
    elif link == 'Add Customer':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.customers, link)
    elif link == 'Add Job':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.customers, link)
    elif link == 'Import Customers':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.customers, link)
    elif link == 'Delete Multiple Customers':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.customers, link)
    elif link == 'Same-As Editor':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.customers, link)
    elif link == 'Manage Documents':
        helpers.click_helper(locations.Links.manage_documents)
    elif link == 'Validate Documents':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.manage_documents, link)
    elif link == 'All Companies':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.manage_documents, link)
    elif link == 'Send Single Request':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.manage_documents, link)
    elif link == 'Campaigns':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.manage_documents, link)
    elif link == 'Email Templates And Cover Letters':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.manage_documents, 'Email Templates and Cover Letters')
    elif link == 'Content Library':
        helpers.click_helper(locations.Links.content_library)
    elif link == 'Document Library':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.content_library, link)
    elif link == 'Nexus Settings':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.content_library, link)
    elif link == 'Exemption Matrix':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.content_library, link)
    elif link == 'Reports':
        helpers.click_helper(locations.Links.reports)
    elif link == 'Document Reports':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.reports, link)
    elif link == 'Customer Reports':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.reports, link)
    elif link == 'Logistic Reports':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.reports, link)
    elif link == 'User Reports':
        helpers.ensure_child_is_visible_before_click_find_by_link(locations.Links.reports, link)
    elif link == 'Settings':
        helpers.click_helper(locations.Links.settings)
    elif link == 'SysAdmin':
        helpers.hover_settings_link('SysAdmin')
    elif link == 'User Accounts':
        helpers.hover_settings_link('SysAdmin')
        helpers.click_find_by_link_helper(link)
    elif link == 'Manage Accounts':
        print('hovering settings')
        helpers.hover_settings_link('SysAdmin')
        print('clicking link')
        helpers.click_find_by_link_helper(link)
    elif link == 'Account Messages':
        helpers.hover_settings_link('SysAdmin')
        helpers.click_find_by_link_helper(link)
    elif link == 'Manage Graphs':
        helpers.hover_settings_link('SysAdmin')
        helpers.click_find_by_link_helper(link)
    elif link == 'Kibana':
        helpers.hover_settings_link('SysAdmin')
        helpers.click_find_by_link_helper(link)
    elif link == 'Log Tool':
        helpers.hover_settings_link('SysAdmin')
        helpers.click_find_by_link_helper(link)
    elif link == 'Account Settings':
        helpers.hover_settings_link('Account')
    elif link == 'Account Details':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Exposure Zones':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Exposure Zones Attributes':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Invalid Reasons':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Document Categories':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Document Attributes':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Customer Attributes':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Manage Users':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'User Roles':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Notification Subscriptions':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'External Apis':
        helpers.hover_settings_link('Account')
        helpers.click_find_by_link_helper(link)
    elif link == 'Company Settings':
        helpers.hover_settings_link('Company')
    elif link == 'Company Details':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Company Same-As':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Custom Fields':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Assign Users':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Data Entry Sets':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Locations':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Buckets':
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper(link)
    elif link == 'Public Certexpress':  # Special Capitalization
        helpers.hover_settings_link('Company')
        helpers.click_find_by_link_helper('Public CertExpress')
    elif link == 'Retail':
        helpers.click_helper(locations.Links.retail)
    else:
        print('Invalid link requested.')


def change_account(account):
    driver.find_element_by_id('dropdownCompanyButton').click()
    time.sleep(3)

    comp_input = driver.find_element_by_id('companyInput')
    comp_input.send_keys(account)
    time.sleep(2)
    # comp_input.send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//*[@id="company-drop"]').click()
    time.sleep(5)


def change_company(company):
    driver.find_element_by_id('dropdownDivisionButton').click()
    time.sleep(3)

    div_input = driver.find_element_by_id('divisionInput')
    div_input.send_keys(company)
    time.sleep(2)
    # div_input.send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//*[@id="division-drop"]').click()
    time.sleep(5)


def change_document_type(doc_type):
    doc_type = doc_type.title()

    if doc_type == 'Sales And Use Tax':
        doc_type = 'Sales and Use Tax'
    elif doc_type == 'Vat':
        doc_type = 'VAT'

    driver.find_element_by_xpath(locations.Buttons.doc_type_button).click()
    time.sleep(2)

    driver.find_element_by_link_text(doc_type).click()
    time.sleep(2)
