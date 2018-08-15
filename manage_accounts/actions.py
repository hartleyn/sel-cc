import time
from general import helpers
from manage_accounts import locations

__author__ = 'Nick Hartley'
# 3/6/18


def click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'add account button':
        helpers.click_helper(locations.Buttons.add_account)
    elif target == 'provision avatax account button':
        helpers.click_helper(locations.Buttons.provision_avatax_account)
    elif target == 'filter button':
        helpers.click_helper(locations.Buttons.filter)
    elif target == 'account list link':
        helpers.click_helper(locations.Links.account_list)
    elif target == 'account statistics link':
        helpers.click_helper(locations.Links.account_statistics)
    elif target == 'account / database name input':
        location = locations.Inputs.account_database_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'zuora / avatax account id input':
        location = locations.Inputs.zuora_avatax_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'filter tier input':
        location = locations.Inputs.filter_tier
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'filter server input':
        location = locations.Inputs.filter_server
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'filter status input':
        location = locations.Inputs.filter_status
        helpers.input_field_click_or_select(location, **kwargs)
    elif target == 'first top button':
        location = locations.Buttons.first_top
        helpers.click_helper(location)
    elif target == 'prev top button':
        location = locations.Buttons.prev_top
        helpers.click_helper(location)
    elif target == 'next top button':
        location = locations.Buttons.next_top
        helpers.click_helper(location)
    elif target == 'last top button':
        location = locations.Buttons.last_top
        helpers.click_helper(location)
    elif target == 'first bottom button':
        location = locations.Buttons.first_bottom
        helpers.click_helper(location)
    elif target == 'prev bottom button':
        location = locations.Buttons.prev_bottom
        helpers.click_helper(location)
    elif target == 'next bottom button':
        location = locations.Buttons.next_bottom
        helpers.click_helper(location)
    elif target == 'last bottom button':
        location = locations.Buttons.last_bottom
        helpers.click_helper(location)
    elif target == 'page select top button':
        location = locations.Buttons.page_select_top
        helpers.click_helper(location)
    elif target == 'page select bottom button':
        location = locations.Buttons.page_select_bottom
        helpers.click_helper(location)
    elif target == 'id header link':
        location = locations.Links.id_header
        helpers.click_helper(location)
    elif target == 'name header link':
        location = locations.Links.name_header
        helpers.click_helper(location)
    elif target == 'tier header link':
        location = locations.Links.tier_header
        helpers.click_helper(location)
    elif target == 'zuora id header link':
        location = locations.Links.zuora_id_header
        helpers.click_helper(location)
    elif target == 'database server header link':
        location = locations.Links.database_server_header
        helpers.click_helper(location)
    elif target == 'database name header link':
        location = locations.Links.database_name_header
        helpers.click_helper(location)
    else:
        print('Invalid click target requested')


def add_account_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'account name input':
        location = locations.Inputs.add_account_modal_account_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.Inputs.add_account_modal_address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.Inputs.add_account_modal_address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.Inputs.add_account_modal_city
        helpers.click_or_type(location, **kwargs)
    elif target == 'state/province input':
        location = locations.Selects.add_account_modal_state_province
        helpers.click_or_select(location, **kwargs)
    elif target == 'country input':
        location = locations.Selects.add_account_modal_country
        helpers.click_or_select(location, **kwargs)
    elif target == 'zip input':
        location = locations.Inputs.add_account_modal_zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone input':
        location = locations.Inputs.add_account_modal_phone
        helpers.click_or_type(location, **kwargs)
    elif target == 'zuora id input':
        location = locations.Inputs.add_account_modal_zuora_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'salesforce id input':
        location = locations.Inputs.add_account_modal_salesforce_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'database name input':
        location = locations.Inputs.add_account_modal_database_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'database server select':
        location = locations.Selects.add_account_modal_database_server
        helpers.click_or_select(location, **kwargs)
    elif target == 'tier select select':
        location = locations.Selects.add_account_modal_tier
        helpers.click_or_select(location, **kwargs)
    elif target == 'upload logo button':
        location = locations.Buttons.add_account_modal_upload_logo
        helpers.click_helper(location)
    elif target == 'demo account checkbox input':
        location = locations.Inputs.add_account_modal_demo_account_checkbox
        helpers.click_helper(location)
    elif target == 'sandbox checkbox input':
        location = locations.Inputs.add_account_modal_sandbox_checkbox
        helpers.click_helper(location)
    elif target == 'x button' or target == 'close button':
        location = locations.Buttons.add_account_modal_close
        helpers.click_helper(location)
    elif target == 'add account button':
        location = locations.Buttons.add_account_modal_add_account
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.Buttons.add_account_modal_cancel
        helpers.click_helper(location)
    elif target == 'reset button':
        location = locations.Buttons.add_account_modal_reset
        helpers.click_helper(location)
    else:
        print('Invalid click target requested')


def provision_avatax_account_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'avatax account id input':
        location = locations.Inputs.provision_avatax_account_modal_avatax_account_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'import ecms data checkbox input':
        location = locations.Inputs.provision_avatax_account_modal_import_ecms_data_checkbox
        helpers.click_helper(location)
    elif target == 'provision avatax account button':
        location = locations.Buttons.provision_avatax_account_modal_provision_avatax_account
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.Buttons.provision_avatax_account_modal_cancel
        helpers.click_helper(location)
    elif target == 'x button' or target == 'close button':
        location = locations.Buttons.provision_avatax_account_modal_close
        helpers.click_helper(location)
    else:
        print('Invalid click target requested')


def complete_add_account_form(account_name, address_line_1, address_line_2, city, state_province, country, zip, phone):
    # Click the 'Account Name' field and fill field
    add_account_modal_click('Account Name input', text=account_name)

    # Click the 'Address Line 1' field and fill field
    add_account_modal_click('Address Line 1 input', text=address_line_1)

    # Click the 'Address Line 2' field and fill field
    add_account_modal_click('Address Line 2 input', text=address_line_2)

    # Click the 'City' field and fill field
    add_account_modal_click('City input', text=city)

    # Click the 'State/Province' field and fill field
    add_account_modal_click('state/province input', select=state_province)

    # Click the 'Country' field and fill field
    add_account_modal_click('country input', select=country)

    # Click the 'Zip' field and fill field
    add_account_modal_click('Zip input',text=zip)

    # Click the 'Phone' field and fill field
    add_account_modal_click('Phone input', text=phone)

    # Append account name to the 'Database Name' field
    add_account_modal_click('Database Name input', text=account_name)

    # Set 'Zuora ID' to 'Internal'
    add_account_modal_click('Zuora ID input', text='internal')

    # Set the 'Database Server' field
    add_account_modal_click('Database Server select', select='dbrds.ec2.beta.certcapture.net')

    # Set the 'Tier' field
    add_account_modal_click('Tier select', select='CertCapture Enterprise')

    time.sleep(2)
