import test_base
import utilities.warnings as warn
import general.helpers as helpers
import bulk_print.locations as locations

__author__ = 'Nick Hartley'
# 5/15/2018


def click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'title input':
        location = locations.Inputs.title
        if kwargs:
            # Clear field if text kwarg is used
            test_base.driver.find_element_by_xpath(location).clear()
        helpers.click_or_type(location, **kwargs)
    elif target == 'merged file input':
        location = locations.Inputs.merged_file
        helpers.click_helper(location)
    elif target == 'individual pdfs input':
        location = locations.Inputs.individual_pdfs
        helpers.click_helper(location)
    elif target == 'merged pdfs input':
        location = locations.Inputs.merged_pdfs
        helpers.click_helper(location)
    elif target == 'footer input':
        location = locations.Inputs.footer
        helpers.click_helper(location)
    elif target == 'reset options link':
        location = locations.Links.reset_options
        helpers.click_helper(location)
    elif target == 'create print job button':
        location = locations.Buttons.create_print_job
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET, target, 'bulk print page')
