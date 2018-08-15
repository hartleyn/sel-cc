
__author__ = 'Nick Hartley'
# 6/15/2018


class Inputs:
    customer_number = '//*[@id="CustomerCustomerNumber"]'
    name = '//*[@id="CustomerName"]'
    contact_name = '//*[@id="CustomerContactName"]'
    alternate_id = '//*[@id="CustomerAlternateId"]'
    phone_number = '//*[@id="CustomerPhoneNumber"]'
    fax_number = '//*[@id="CustomerFaxNumber"]'
    email_address = '//*[@id="CustomerEmailAddress"]'
    fein = '//*[@id="CustomerFeinNumber"]'
    attention_name = '//*[@id="CustomerAttnName"]'
    address_line_1 = '//*[@id="CustomerAddressLine1"]'
    address_line_2 = '//*[@id="CustomerAddressLine2"]'
    city = '//*[@id="CustomerCity"]'
    zip = '//*[@id="CustomerZip"]'


class Selects:
    state = '//*[@id="CustomerStateId"]'
    country = '//*[@id="CustomerCountryId"]'


class Buttons:
    generate = '//*[@id="generate_customer_number"]'
    add_new_customer = '//*[@id="add_customer"]'
    reset = '//*[@id="reset_btn"]'
