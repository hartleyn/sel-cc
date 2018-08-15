import json
from test_base import slash, driver
from public_certexpress import locations

__author__ = 'Nick Hartley'
# 5/10/2018


def store_public_certexpress_link_in_json():
    link = driver.find_element_by_xpath(locations.Links.public_certexpress_url).text
    print('Found Public CertExpress link:', link)

    data = {'url': link}

    with open('public_certexpress{}request.json'.format(slash), 'w') as f:
        json.dump(data, f)
