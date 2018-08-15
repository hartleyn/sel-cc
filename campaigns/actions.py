import time
import json
import utilities.warnings as warn
import general.helpers as helpers
import campaigns.locations as locations
from test_base import slash, driver
from utilities import pdf_reader
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 4/19/2018


def set_up_campaign_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'campaign title input':
        location = locations.SetUpCampaign.Inputs.campaign_title
        helpers.click_or_type(location, **kwargs)
    elif target == 'include customers input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.include_customers)
    elif target == 'omit customers input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.omit_customers)
    elif target == 'missing exemption input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.missing_exemption)
    elif target == 'invalid exemption input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.invalid_exemption)
    elif target == 'expired certificate input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.expired_certificate)
    elif target == 'include soon to expire input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.include_soon_to_expire)
    elif target == 'include soon to expire days input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.include_soon_to_expire_days)
    elif target == 'taxable exposures input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.taxable_exposures)
    elif target == 'override input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.override)
    elif target == 'billing customers input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.billing_customers)
    elif target == 'shipping customers input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.shipping_customers)
    elif target == 'exclude same as input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.exclude_same_as)
    elif target == 'expand bill to ship input':
        return helpers.click_helper(locations.SetUpCampaign.Inputs.expand_bill_to_ship)
    elif target == 'exempt reasons input':
        location = locations.SetUpCampaign.Inputs.exempt_reasons
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'select all link':
        return helpers.click_helper(locations.SetUpCampaign.Links.select_all)
    elif target == 'deselect all link':
        return helpers.click_helper(locations.SetUpCampaign.Links.deselect_all)
    elif target == 'document type select':
        location = locations.SetUpCampaign.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'prepare campaign button':
        # Attempting to return this element causes an error
        # driver.find_element_by_xpath(locations.SetUpCampaign.Buttons.prepare_campaign).click()
        location = locations.SetUpCampaign.Buttons.prepare_campaign
        helpers.click_helper(location)
        time.sleep(2)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_campaign_click(target_name, **kwargs):
    """

    :rtype: object
    """
    target = target_name.lower()

    if target == 'send date input':
        location = locations.EditCampaign.Inputs.send_date
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'requested return date input':
        location = locations.EditCampaign.Inputs.requested_return_date
        # Clear field if date is auto-generated; Maybe this should be in a helper?
        driver.find_element_by_xpath(location).clear()
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'generate date input':
        location = locations.EditCampaign.Inputs.generate_date
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'include most recent invalid input':
        location = locations.EditCampaign.Inputs.include_most_recent
        helpers.click_or_type(location, **kwargs)
    elif target == 'cover letter only input':
        location = locations.EditCampaign.Inputs.cover_letter_only
        helpers.click_or_type(location, **kwargs)
    elif target == 'include certexpress access input':
        location = locations.EditCampaign.Inputs.include_certexpress_access
        helpers.click_or_type(location, **kwargs)
    elif target == 'automatically send round input':
        location = locations.EditCampaign.Inputs.automatically_send_round
        helpers.click_or_type(location, **kwargs)
    elif target == 'notes input':
        location = locations.EditCampaign.Inputs.notes
        helpers.click_or_type(location, **kwargs)
    elif target == 'method select':
        location = locations.EditCampaign.Selects.method
        helpers.click_or_select(location, **kwargs)
    elif target == 'email template cover letter select':
        location = locations.EditCampaign.Selects.email_template_cover_letter
        helpers.click_or_select(location, **kwargs)
    elif target == 'overview link':
        helpers.click_helper(locations.EditCampaign.Links.overview)
    elif target == 'add round link':
        helpers.click_helper(locations.EditCampaign.Links.add_round)
    elif target == 'scheduling and delivery link':
        helpers.click_helper(locations.EditCampaign.Links.scheduling_and_delivery)
    elif target == 'select customers link':
        helpers.click_helper(locations.EditCampaign.Links.select_customers)
    elif target == 'preview link':
        helpers.click_helper(locations.EditCampaign.Links.preview)
    elif target == 'print link':
        helpers.click_helper(locations.EditCampaign.Links.print)
    elif target == 'send emails link':
        helpers.click_helper(locations.EditCampaign.Links.send_emails)
    elif target == 'clone round link':
        helpers.click_helper(locations.EditCampaign.Links.clone_round)
    elif target == 'delete round link':
        helpers.click_helper(locations.EditCampaign.Links.delete_round)
    elif target == 'customer number header link':
        helpers.click_helper(locations.EditCampaign.Links.customer_number_header)
    elif target == 'name header link':
        helpers.click_helper(locations.EditCampaign.Links.name_header)
    elif target[0:5] == 'round' and target[-4:] == 'link':
        if target[7] == ' ':
            number = target[6]  # Supports single digits
            helpers.click_helper(locations.EditCampaign.Links.round(number))
        elif target[8] == ' ':
            number = target[6:8]  # Supports double digits
            helpers.click_helper(locations.EditCampaign.Links.round(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target == 'delete campaign button':
        helpers.click_helper(locations.EditCampaign.Buttons.delete_campaign)
    elif target == 'save campaign changes button':
        helpers.click_helper(locations.EditCampaign.Buttons.save_campaign_changes)
        time.sleep(2)
    elif target == 'send compliance document requests button':
        driver.find_element_by_xpath(locations.EditCampaign.Buttons.send_compliance_document_requests).click()
        time.sleep(2)
        Alert(driver).accept()
    elif target == 'export overview data button':
        helpers.click_helper(locations.EditCampaign.Buttons.export_overview_data)
    elif target == 'first button':
        helpers.click_helper(locations.EditCampaign.Buttons.first)
    elif target == 'prev button':
        helpers.click_helper(locations.EditCampaign.Buttons.prev)
    elif target == 'page selector select':
        location = locations.EditCampaign.Selects.page_selector
        helpers.click_or_select(location, **kwargs)
    elif target == 'next button':
        helpers.click_helper(locations.EditCampaign.Buttons.next)
    elif target == 'last button':
        helpers.click_helper(locations.EditCampaign.Buttons.last)
    elif target == 'pdf - 1 merged file input':
        helpers.click_helper(locations.EditCampaign.Inputs.merged_file)
    elif target == 'zip - individual pdfs input':
        helpers.click_helper(locations.EditCampaign.Inputs.zip_individual)
    elif target == 'zip - merged pdf by page count input':
        helpers.click_helper(locations.EditCampaign.Inputs.zip_merged)
    elif target == 'create printable file button':
        helpers.click_helper(locations.EditCampaign.Buttons.create_printable_file)
    else:
        print(warn.INVALID_CLICK_TARGET)


def set_up_campaign(title, doc_type, reasons):
    '''
        Sets up the campaign
        title - campaign title
        doc_type - document type
        reasons - a list of exempt reasons; a single string may also be passed in
    '''

    # Set 'Campaign Title'
    set_up_campaign_click('campaign title input', text=title)

    # Click 'Include Customers already in another campaign' radio button
    set_up_campaign_click('include customers input')

    # Set 'Document Type'
    try:
        helpers.select_helper(locations.SetUpCampaign.Selects.document_type, doc_type)
        time.sleep(1)
    except NoSuchElementException:
        pass

    # Cast reasons to a list if one was not passed in
    if type(reasons) is not list:
        reasons = [reasons]

    # Set 'Exempt Reasons'
    set_up_campaign_click('exempt reasons input', select=reasons)


def set_up_scheduling_and_delivery(send_date, return_date, method, letter):
    # Set 'Send Date'
    edit_campaign_click('send date input', date=send_date)

    # Set 'Requested Return Date'
    edit_campaign_click('requested return date input', date=return_date)

    # Set 'Generate Date'
    # edit_campaign_click('generate date input').send_keys(gen_date)

    # Set 'Method'
    edit_campaign_click('method select', select=method)

    # Set 'Email Template/Cover Letter'
    edit_campaign_click('email template cover letter select', select=letter)


def store_request_links_in_json():
    links = pdf_reader.get_request_links_from_merged_pdf_file()
    print('Storing request links:', links)

    my_data = {'urls': links}
    print(my_data)

    with open('campaigns{}requests.json'.format(slash), 'w') as f:
        json.dump(my_data, f)


def find_and_click_in_progress_campaign(campaign_name):
    time.sleep(5)
    x = 2
    check = True
    while check:
        try:
            label = driver.find_element_by_xpath('//*[@id="incomplete_mailout_list"]/tbody/tr[{}]/td[2]'.format(x)).text

            if campaign_name.lower() == label.lower():
                print('Found campaign: {}'.format(campaign_name))
                check = False
                driver.find_element_by_xpath('//*[@id="incomplete_mailout_list"]/tbody/tr[{}]/td[6]/a'.format(x)).click()
                time.sleep(5)
            else:
                x += 1
        except NoSuchElementException:
            check = False
            print('Finished searching in-progress campaigns. Campaign not found.')
