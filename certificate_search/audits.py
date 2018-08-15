from test_base import driver


def verify_certexpress_certificate_validation(exposure_zone, exempt_reason):
    result_exposure_zone = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[2]').text
    result_exempt_reason = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[3]').text

    assert result_exposure_zone.lower() == exposure_zone.lower(), 'Incorrect exposure zone. Expected: {}, Found {}.'\
        .format(exposure_zone, result_exposure_zone)
    assert result_exempt_reason.lower() == exempt_reason.lower(), 'Incorrect exempt reason. Expected: {}, Found {}.'\
        .format(exempt_reason, result_exempt_reason)
    print('CertExpress certificate validated successfully...')

    certificate_id = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[1]/a').text

    print('Certificate ID: {}'.format(certificate_id))


def verify_certificate_validation(exposure_zone, exempt_reason, effective_date, customer_number):
    result_exposure_zone = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[2]').text
    result_exempt_reason = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[3]').text
    result_effective_date = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[4]').text
    result_customer_number = driver\
        .find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[7]/table/tbody/tr[2]/td[3]').text

    assert result_exposure_zone.lower() == exposure_zone.lower(), 'Incorrect exposure zone. Expected: {}, Found {}.'\
        .format(exposure_zone.lower(), result_exposure_zone)
    assert result_exempt_reason.lower() == exempt_reason.lower(), 'Incorrect exempt reason. Expected: {}, Found {}.'\
        .format(exempt_reason, result_exempt_reason)
    assert result_effective_date == effective_date, 'Incorrect effective date. Expected: {}, Found {}.'\
        .format(effective_date, result_effective_date)
    assert result_customer_number == customer_number, 'Incorrect customer number. Expected: {}, Found {}.'\
        .format(customer_number, result_customer_number)
    print('Certificate validated successfully...')

    certificate_id = driver.find_element_by_xpath('//table[@id="search_results_grid"]/tbody/tr[2]/td[1]/a').text

    print('Certificate ID: {}'.format(certificate_id))
