from general import helpers
from utilities import warnings as warn
from certificate_details import locations


def click(target_name):
    target = target_name.lower()

    if target == 'details link':
        location = locations.Links.details
        helpers.click_helper(location)
    elif target == 'customers link':
        location = locations.Links.customers
        helpers.click_helper(location)
    elif target == 'validation link':
        location = locations.Links.validation
        helpers.click_helper(location)
    elif target == 'history link':
        location = locations.Links.history
        helpers.click_helper(location)
    elif target == 'comments and files link':
        location = locations.Links.comments_and_files
        helpers.click_helper(location)
    elif target == 'rebuild pdf image button':
        location = locations.Buttons.rebuild_pdf_image
        helpers.click_helper(location)
    elif target == 'delete certificate button':
        location = locations.Buttons.delete_certificate
        helpers.click_helper(location)
    elif target == 'edit button':
        location = locations.Buttons.edit
        helpers.click_helper(location)
    elif target == 'view all pages button':
        location = locations.Buttons.view_all_pages
        helpers.click_helper(location)
    elif target == 'download button':
        location = locations.Buttons.download
        helpers.click_helper(location)
    elif target == 'add po number button':
        location = locations.Buttons.add_po_number
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)
