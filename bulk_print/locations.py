
__author__ = 'Nick Hartley'
# 5/18/2018


class Inputs:
    title = '//*[@id="title"]'
    merged_file = '//*[@id="radio1"]'
    individual_pdfs = '//*[@id="radio2"]'
    merged_pdfs = '//*[@id="radio3"]'
    footer = '//*[@id="use_footstamp"]'


class Links:
    reset_options = '//*[@id="search_form"]/div/div[1]/h4/span'


class Buttons:
    create_print_job = '//*[@id="add_bulkcertificates"]'
