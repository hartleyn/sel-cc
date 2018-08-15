import time
from test_base import driver
from selenium.common.exceptions import NoSuchElementException


def verify_data_entry_set(zones):
    time.sleep(3)  # Wait for data entry set exposure zone population

    screen_zones = []

    check = True
    x = 2  # Values start in tr[2]
    while check:
        try:
            screen_zone = driver.find_element_by_xpath(
                '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[{}]/td[1]'.format(x)
            ).text

            screen_zones.append(screen_zone)
            x += 1
        except NoSuchElementException:
            check = False

    assert len(screen_zones) == len(zones), \
        'Incorrect number of exposure zones found. Expected: {}. Found {}.'.format(len(zones), len(screen_zones))
    print('Found {} exposure zones.'.format(len(screen_zones)))

    # Check each zone on the screen matches with an expected zone
    for screen_zone in screen_zones:
        assert any(screen_zone == zone for zone in zones), 'Unexpected exposure zone found: {}'.format(screen_zone)
        print('Found expected exposure zone: {}'.format(screen_zone))
