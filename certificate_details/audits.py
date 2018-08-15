from test_base import driver

_author_ = 'Nick Hartley'
# 6/18/2018


def verify_status_complete():
    status = driver.find_element_by_xpath('//*[@id="certificate_details_content"]/table[1]/tbody/tr/td[1]').text

    assert status == 'COMPLETE', 'Incorrect status found. Expected "COMPLETE", Found {}.'.format(status)


def verify_certificate_validation():
    status = driver.find_element_by_xpath('//*[@id="validation"]/div[2]/table/tbody/tr/td[1]/span').text

    assert status == 'Valid', 'Incorrect validation status found. Expected "Valid", Found {}'.format(status)
