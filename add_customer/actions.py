import time
from utilities import warnings as warn
from general import helpers
from add_customer import locations


def click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'customer number input':
        location = locations.Inputs.customer_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'name input':
        location = locations.Inputs.name
        helpers.click_or_type(location, **kwargs)
    elif target == 'contact name input':
        location = locations.Inputs.contact_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'alternate id input':
        location = locations.Inputs.alternate_id
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone number input':
        location = locations.Inputs.phone_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'fax number input':
        location = locations.Inputs.fax_number
        helpers.click_or_type(location, **kwargs)
    elif target == 'email address input':
        location = locations.Inputs.email_address
        helpers.click_or_type(location, **kwargs)
    elif target == 'fein input':
        location = locations.Inputs.fein
        helpers.click_or_type(location, **kwargs)
    elif target == 'attention name input':
        location = locations.Inputs.attention_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.Inputs.address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.Inputs.address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.Inputs.city
        helpers.click_or_type(location, **kwargs)
    elif target == 'zip input':
        location = locations.Inputs.zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'state select':
        location = locations.Selects.state
        helpers.click_or_select(location, **kwargs)
    elif target == 'country select':
        location = locations.Selects.country
        helpers.click_or_select(location, **kwargs)
    elif target == 'generate button':
        location = locations.Buttons.generate
        helpers.click_helper(location)
    elif target == 'add new customer button':
        location = locations.Buttons.add_new_customer
        helpers.click_helper(location)
        time.sleep(3)  # Wait for processing
    elif target == 'reset button':
        location = locations.Buttons.reset
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def set_up_add_new_customer(customer_number, name, phone, email, address, city, state, zip):
    click('customer number input', text=customer_number)

    click('name input', text=name)

    click('phone number input', text=phone)

    click('email address input', text=email)

    click('address line 1 input', text=address)

    click('city input', text=city)

    click('state select', select=state)

    click('zip input', text=zip)
