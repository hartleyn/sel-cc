import time
import datetime
from test_base import driver
from general import helpers
from utilities import warnings as warn
from validate_documents import locations
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/4/2018


def click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer input':
        location = locations.Inputs.customer
        helpers.click_or_type(location, **kwargs)
    elif target == 'exposure zone input':
        location = locations.Inputs.exposure_zone
        helpers.click_or_type(location, **kwargs)
    elif target == 'document category input':
        location = locations.Inputs.document_category
        helpers.click_or_type(location, **kwargs)
    elif target == 'document id input' or target == 'certificate id input' or target == 'filename input':
        location = locations.Inputs.document_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'created date input':
        location = locations.Inputs.created
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'document type input':
        location = locations.Inputs.document_type
        helpers.click_or_type(location, **kwargs)
    elif target == 'check all documents input':
        location = locations.Inputs.check_all_documents
        helpers.click_helper(location)
    elif target[0:11] == 'results row' and target[-14:] == 'checkbox input':
        if target[13] == ' ':
            number = target[12]  # Supports single digits
            helpers.click_helper(locations.Inputs.results_row_checkbox(number))
        elif target[14] == ' ':
            number = target[12:13]  # Supports double digits
            helpers.click_helper(locations.Inputs.results_row_checkbox(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target == 'stack filter select':
        location = locations.Selects.stack_filter
        helpers.click_or_select(location, **kwargs)
    elif target == 'stage select':
        location = locations.Selects.stage
        helpers.click_or_select(location, **kwargs)
    elif target == 'priority select':
        location = locations.Selects.priority
        helpers.click_or_select(location, **kwargs)
    elif target == 'source select':
        location = locations.Selects.source
        helpers.click_or_select(location, **kwargs)
    elif target == 'bucket select':
        location = locations.Selects.bucket
        helpers.click_or_select(location, **kwargs)
    elif target == 'location select':
        location = locations.Selects.location
        helpers.click_or_select(location, **kwargs)
    elif target == 'page selector top select':
        location = locations.Selects.top_page_selector
        helpers.click_or_select(location, **kwargs)
    elif target == 'page selector bottom select':
        location = locations.Selects.bottom_page_selector
        helpers.click_or_select(location, **kwargs)
    elif target == 'search type toggle button':
        location = locations.Buttons.search_type_toggle
        helpers.click_helper(location)
    elif target == 'upload document button':
        location = locations.Buttons.upload_document
        helpers.click_helper(location)
    elif target == 'search button':
        location = locations.Buttons.search
        helpers.click_helper(location)
        time.sleep(3)
    elif target == 'clear button':
        location = locations.Buttons.clear
        helpers.click_helper(location)
    elif target == 'action button':
        location = locations.Buttons.action
        helpers.click_helper(location)
    elif target == 'first top button':
        location = locations.Buttons.top_first
        helpers.click_helper(location)
    elif target == 'prev top button':
        location = locations.Buttons.top_prev
        helpers.click_helper(location)
    elif target == 'next top button':
        location = locations.Buttons.top_next
        helpers.click_helper(location)
    elif target == 'last top button':
        location = locations.Buttons.top_last
        helpers.click_helper(location)
    elif target == 'first bottom button':
        location = locations.Buttons.bottom_first
        helpers.click_helper(location)
    elif target == 'prev bottom button':
        location = locations.Buttons.bottom_prev
        helpers.click_helper(location)
    elif target == 'next bottom button':
        location = locations.Buttons.bottom_next
        helpers.click_helper(location)
    elif target == 'last bottom button':
        location = locations.Buttons.bottom_last
        helpers.click_helper(location)
    elif target[0:11] == 'results row' and target[-4:] == 'link':
        if target[13] == ' ':
            number = target[12]  # Supports single digits
            helpers.click_helper(locations.Links.results_row(number))
            time.sleep(2)
            helpers.switch_to_new_window()
            time.sleep(2)
        elif target[14] == ' ':
            number = target[12:13]  # Supports double digits
            helpers.click_helper(locations.Links.results_row(number))
            time.sleep(2)
            helpers.switch_to_new_window()
            time.sleep(2)
        else:
            print(warn.SOME_PROBLEM)
    elif target == 'document header link':
        location = locations.Links.document_header
        helpers.click_helper(location)
    elif target == 'customer number header link':
        location = locations.Links.customer_number_header
        helpers.click_helper(location)
    elif target == 'stage header link':
        location = locations.Links.stage_header
        helpers.click_helper(location)
    elif target == 'account header link':
        location = locations.Links.account_header
        helpers.click_helper(location)
    elif target == 'exposure zone header link':
        location = locations.Links.exposure_zone_header
        helpers.click_helper(location)
    elif target == 'source header link':
        location = locations.Links.source_header
        helpers.click_helper(location)
    elif target == 'priority header link':
        location = locations.Links.priority_header
        helpers.click_helper(location)
    elif target == 'pages header link':
        location = locations.Links.pages_header
        helpers.click_helper(location)
    elif target == 'age header link':
        location = locations.Links.age_header
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def upload_document_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'choose file input':
        location = locations.UploadDocumentModal.Inputs.choose_file
        helpers.click_or_type(location, **kwargs)
    elif target == 'claim document input':
        location = locations.UploadDocumentModal.Inputs.claim_document
        helpers.click_or_type(location, **kwargs)
    elif target == 'auto split page count input':
        location = locations.UploadDocumentModal.Inputs.auto_split_page_count
        helpers.click_or_type(location, **kwargs)
    elif target == 'priority select':
        location = locations.UploadDocumentModal.Selects.priority
        helpers.click_or_select(location, **kwargs)
    elif target == 'auto split select':
        location = locations.UploadDocumentModal.Selects.auto_split
        helpers.click_or_select(location, **kwargs)
    elif target == 'bucket select':
        location = locations.UploadDocumentModal.Selects.bucket
        helpers.click_or_select(location, **kwargs)
    elif target == 'document type select':
        location = locations.UploadDocumentModal.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'exposure zone select':
        location = locations.UploadDocumentModal.Selects.exposure_zone
        helpers.click_or_select(location, **kwargs)
    elif target == 'exempt reason select':
        location = locations.UploadDocumentModal.Selects.exempt_reason
        helpers.click_or_select(location, **kwargs)
    elif target == 'close button':
        location = locations.UploadDocumentModal.Buttons.close
        helpers.click_helper(location)
    elif target == 'upload stack button':
        location = locations.UploadDocumentModal.Buttons.upload_stack_button
        helpers.click_helper(location)
        time.sleep(3)
    else:
        print(warn.INVALID_CLICK_TARGET)


def validate_document_window_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customers input':
        location = locations.ValidateDocumentWindow.Inputs.customers
        helpers.validation_customers_click_or_select(location, **kwargs)
    elif target == 'created date input':
        location = locations.ValidateDocumentWindow.Inputs.created_date
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'effective date input':
        location = locations.ValidateDocumentWindow.Inputs.effective_Date
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'single use checkbox input':
        location = locations.ValidateDocumentWindow.Inputs.single_use_checkbox
        helpers.click_or_type(location, **kwargs)
    elif target == 'exposure zones input':
        location = locations.ValidateDocumentWindow.Inputs.exposure_zones
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'invalid reasons input':
        location = locations.ValidateDocumentWindow.Inputs.invalid_reasons
        helpers.click_or_type(location, **kwargs)
    elif target == 'customer attributes input':
        location = locations.ValidateDocumentWindow.Inputs.customer_attributes
        helpers.click_helper(location)
    elif target == 'documents attributes input':
        location = locations.ValidateDocumentWindow.Inputs.document_attributes
        helpers.click_or_type(location, **kwargs)
    elif target[0:24] == 'exposure zone tax id row' and target[-5:] == 'input':
        if target[26] == ' ':
            number = target[25]  # Supports single digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_tax_id_row(number))
        elif target[27] == ' ':
            number = target[25:26]  # Supports double digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_tax_id_row(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target[0:29] == 'exposure zone expire date row' and target[-5:] == 'input':
        if target[31] == ' ':
            number = target[30]  # Supports single digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_expire_date_row(number))
        elif target[32] == ' ':
            number = target[30:31]  # Supports double digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_expire_date_row(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target[0:24] == 'exposure zone exempt percentage row' and target[-5:] == 'input':
        if target[37] == ' ':
            number = target[36]  # Supports single digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_exempt_percentage_row(number))
        elif target[38] == ' ':
            number = target[36:37]  # Supports double digits
            helpers.click_helper(locations.ValidateDocumentWindow.Inputs.exposure_zone_exempt_percentage_row(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target == 'escalate explain input':
        location = locations.ValidateDocumentWindow.Inputs.escalate_explain
        helpers.click_or_type_date(location, **kwargs)
    elif target == 'document type select':
        location = locations.ValidateDocumentWindow.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'exempt reason select':
        location = locations.ValidateDocumentWindow.Selects.exempt_reason
        helpers.click_or_select(location, **kwargs)
    elif target == 'location select':
        location = locations.ValidateDocumentWindow.Selects.location
        helpers.click_or_select(location, **kwargs)
    elif target == 'state select':
        location = locations.ValidateDocumentWindow.Selects.filter_state
        helpers.click_or_select(location, **kwargs)
    elif target == 'attribute group select':
        location = locations.ValidateDocumentWindow.Selects.filter_attribute_group
        helpers.click_or_select(location, **kwargs)
    elif target == 'attribute select':
        location = locations.ValidateDocumentWindow.Selects.filter_attribute
        helpers.click_or_select(location, **kwargs)
    elif target == 'escalate reason select':
        location = locations.ValidateDocumentWindow.Selects.escalate_reason
        helpers.click_or_select(location, **kwargs)
    elif target == 'delete button':
        location = locations.ValidateDocumentWindow.Buttons.delete
        helpers.click_helper(location)
    elif target == 'defaults button':
        location = locations.ValidateDocumentWindow.Buttons.defaults
        helpers.click_helper(location)
    elif target == 'release button':
        location = locations.ValidateDocumentWindow.Buttons.release
        helpers.click_helper(location)
    elif target == 'download button':
        location = locations.ValidateDocumentWindow.Buttons.download
        helpers.click_helper(location)
    elif target == 'escalate button':
        location = locations.ValidateDocumentWindow.Buttons.escalate
        helpers.click_helper(location)
    elif target == 'validate button':
        location = locations.ValidateDocumentWindow.Buttons.validate
        helpers.click_helper(location)
    elif target == 'advanced search button':
        location = locations.ValidateDocumentWindow.Buttons.advanced_search
        helpers.click_helper(location)
    elif target == 'add customer button':
        location = locations.ValidateDocumentWindow.Buttons.add_customer
        helpers.click_helper(location)
    elif target == 'bulk add button':
        location = locations.ValidateDocumentWindow.Buttons.bulk_add
        helpers.click_helper(location)
    elif target == 'effective date button':
        location = locations.ValidateDocumentWindow.Buttons.date_picker_effective_date
        helpers.click_helper(location)
    elif target == 'clear button':
        location = locations.ValidateDocumentWindow.Buttons.clear
        helpers.click_helper(location)
    elif target == 'expire date button':
        location = locations.ValidateDocumentWindow.Buttons.date_picker_expire_date
        helpers.click_helper(location)
    elif target == 'never expire button':
        location = locations.ValidateDocumentWindow.Buttons.never_expire
        helpers.click_helper(location)
    elif target == 'validate ids button':
        location = locations.ValidateDocumentWindow.Buttons.validate_ids
        helpers.click_helper(location)
    elif target == 'success ok button':
        location = locations.ValidateDocumentWindow.Buttons.success_ok
        helpers.click_helper(location)
        time.sleep(2)
        helpers.close_extra_windows()
    elif target == 'escalate x button':
        location = locations.ValidateDocumentWindow.Buttons.escalate_x
        helpers.click_helper(location)
    elif target == 'escalate escalate button':
        location = locations.ValidateDocumentWindow.Buttons.escalate_escalate
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def merge_document_window_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'document type select':
        location = locations.MergeDocumentWindow.Selects.document_type
        helpers.click_or_select(location, **kwargs)
    elif target == 'exposure zone select':
        location = locations.MergeDocumentWindow.Selects.exposure_zone
        helpers.click_or_select(location, **kwargs)
    elif target == 'document category select':
        location = locations.MergeDocumentWindow.Selects.document_category
        helpers.click_or_select(location, **kwargs)
    elif target == 'submit button':
        location = locations.MergeDocumentWindow.Buttons.submit
        helpers.click_helper(location)
    elif target == 'release document button':
        location = locations.MergeDocumentWindow.Buttons.release_document
        helpers.click_helper(location)
    elif target == 'flip all images button':
        location = locations.MergeDocumentWindow.Buttons.flip_all_images
        helpers.click_helper(location)
    elif target == 'rotate 90 left button':
        location = locations.MergeDocumentWindow.Buttons.rotate_90_left
        helpers.click_helper(location)
    elif target == 'rotate 90 right button':
        location = locations.MergeDocumentWindow.Buttons.rotate_90_right
        helpers.click_helper(location)
    elif target == 'rotate 180 button':
        location = locations.MergeDocumentWindow.Buttons.rotate_180
        helpers.click_helper(location)
    elif target == 'darken contrast button':
        location = locations.MergeDocumentWindow.Buttons.darken_contrast
        helpers.click_helper(location)
    elif target == 'delete button':
        location = locations.MergeDocumentWindow.Buttons.delete
        helpers.click_helper(location)
    elif target == 'successful merge x button':
        location = locations.MergeDocumentWindow.Buttons.successful_merge_x
        helpers.click_helper(location)
        helpers.switch_to_old_window()
        time.sleep(10)  # wait for processing
    elif target == 'successful merge close button':
        location = locations.MergeDocumentWindow.Buttons.successful_merge_close
        helpers.click_helper(location)
        helpers.switch_to_old_window()
        time.sleep(10)  # wait for processing
    elif target == 'successful merge next button':
        location = locations.MergeDocumentWindow.Buttons.successful_merge_next
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def set_up_document_upload(filepath, doc_type, zone, reason):
    # Select upload file
    driver.find_element_by_xpath(locations.UploadDocumentModal.Inputs.choose_file).send_keys(filepath)

    # Set 'Document Type'
    upload_document_modal_click('document type select', select=doc_type)

    # Set 'Exposure Zone'
    upload_document_modal_click('exposure zone select', select=zone)

    # Set 'Exempt Reason'
    upload_document_modal_click('exempt reason select', select=reason.upper())


def set_up_document_merge(doc_type, zone, reason):
    # Set 'Document Type'
    merge_document_window_click('document type select', select=doc_type)

    # Set 'Exposure Zone'
    merge_document_window_click('exposure zone select', select=zone)

    # Set 'Exempt Reason'
    merge_document_window_click('exempt reason select', select=reason)


def set_up_document_validation(customer):
    # Select customer
    validate_document_window_click('customers input', select=customer)

    # Clicking too fast
    time.sleep(2)

    # Click never expire button
    validate_document_window_click('never expire button')


def set_up_search_for_document(filename=None, today=True, **kwargs):
    try:
        click('stage select', select=kwargs['stage'])
    except KeyError:
        pass

    try:
        click('source select', select=kwargs['source'])
    except KeyError:
        pass

    if today:
        today = str(datetime.date.today())
        click('created date input', date=today)  # Automatically search for documents uploaded today

    if filename:
        click('certificate id input', text=filename)
    time.sleep(3)


def set_up_sst_validation(customer=None):
    if customer:
        # Select customer
        validate_document_window_click('customers input', select=customer)

    check = True
    x = 1
    while check:
        try:
            elem = driver.find_element_by_xpath(locations.ValidateDocumentWindow.Inputs.exposure_zone_tax_id_row(x))
            elem.send_keys('1')
            helpers.click_helper(locations.ValidateDocumentWindow.Buttons.exposure_zone_never_expire_row(x))
            x += 1
        except NoSuchElementException:
            check = False


def get_certificate_id():
    cert_id = driver.find_element_by_xpath('//*[@id="dataEntryForm"]/div[2]/div/p/strong').text
    return cert_id
