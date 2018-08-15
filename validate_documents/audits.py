from test_base import driver
from selenium.common.exceptions import NoSuchElementException


def verify_certexpress_certificate_creation(customer):
    validation_screen_customer_number = driver.\
        find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[5]').text
    validation_screen_days = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[13]').text

    assert validation_screen_customer_number == customer, 'Incorrect customer number. Expected: {}, Found {}.'\
        .format(customer, validation_screen_customer_number)
    assert int(validation_screen_days) == 0, 'Incorrect day count. Expected: {}, Found {}.'\
        .format(0, validation_screen_days)  # Certificate was created 0 days ago
    print('CertExpress certificate created successfully...')


def verify_document_upload(filename, exposure_zone=None, stage='Ready For Merge', source='Upload', age='0'):
    validation_screen_filename = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[2]/td[4]').text
    validation_screen_stage = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[2]/td[6]').text
    validation_screen_exposure_zone = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[2]/td[9]').text
    validation_screen_source = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[2]/td[10]').text
    validation_screen_age = driver.find_element_by_xpath('//*[@id="DataEntrySearch"]/tbody/tr[2]/td[13]').text

    assert validation_screen_filename.lower() == filename.lower(), 'Incorrect filename. Expected: {}, Found {}.'\
        .format(filename, validation_screen_filename)

    assert validation_screen_stage.lower() == stage.lower(), 'Incorrect stage. Expected: {}, Found {}.'\
        .format(stage, validation_screen_stage)

    assert validation_screen_exposure_zone.lower() == exposure_zone.lower(), \
        'Incorrect exposure zone. Expected: {}, Found {}.'.format(exposure_zone, validation_screen_exposure_zone)

    assert validation_screen_source.lower() == source.lower(), 'Incorrect source. Expected: {}, Found {}.'\
        .format(source, validation_screen_source)

    assert validation_screen_age == age

    print('Certificate uploaded successfully...')


def verify_certificate_escalation():
    validation_screen_stage = driver.find_element_by_xpath('//table[@id="DataEntrySearch"]/tbody/tr[2]/td[6]').text

    stage = 'Ready For Validation (Escalated 0 days ago)'

    assert validation_screen_stage.lower() == stage.lower(), 'Incorrect stage. Expected: {}, Found {}.'\
        .format(stage, validation_screen_stage)

    print('Certificate escalated successfully...')
