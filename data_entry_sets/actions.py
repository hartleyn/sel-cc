import test_base
from utilities import warnings as warn
import data_entry_sets.locations as locations
import general.helpers as helpers
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Nick Hartley'
# 5/7/2018

driver = test_base.driver


def click(target_name):
    target = target_name.lower()

    if target == 'add data entry set button':
        location = locations.Buttons.add_data_entry_set
        helpers.click_helper(location)
    elif target == 'name header link':
        location = locations.Links.name_header
        helpers.click_helper(location)
    elif target[0:3] == 'row' and target[-9:] == 'edit link':
        if target[5] == ' ':
            number = target[4]  # Supports single digits
            helpers.click_helper(locations.Links.data_entry_set_edit(number))
        elif target[6] == ' ':
            number = target[4:5]  # Supports double digits
            helpers.click_helper(locations.Links.data_entry_set_edit(number))
        else:
            print(warn.SOME_PROBLEM)
    elif target[0:3] == 'row' and target[-11:] == 'delete link':
        if target[5] == ' ':
            number = target[4]  # Supports single digits
            helpers.click_helper(locations.Links.data_entry_set_edit(number))
        elif target[6] == ' ':
            number = target[4:5]  # Supports double digits
            helpers.click_helper(locations.Links.data_entry_set_edit(number))
        else:
            print(warn.SOME_PROBLEM)
    else:
        print(warn.INVALID_CLICK_TARGET)


def add_data_entry_set_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'name input':
        location = locations.AddDataEntrySetModal.Inputs.name
        helpers.click_or_type(location, **kwargs)
    elif target == 'add button':
        location = locations.AddDataEntrySetModal.Buttons.add
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.AddDataEntrySetModal.Buttons.cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.AddDataEntrySetModal.Buttons.close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def edit_data_entry_set_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'name input':
        location = locations.EditDataEntrySetModal.Inputs.name
        helpers.click_or_type(location, **kwargs)
    elif target == 'update button':
        location = locations.EditDataEntrySetModal.Buttons.update
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.EditDataEntrySetModal.Buttons.cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.EditDataEntrySetModal.Buttons.close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def delete_modal_click(target_name):
    target = target_name.lower()

    if target == 'ok button':
        location = locations.DeleteModal.Buttons.ok
        helpers.click_or_type(location)
    elif target == 'cancel button':
        location = locations.DeleteModal.Buttons.cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.DeleteModal.Buttons.close
        helpers.click_helper(location)
    else:
        print(warn.INVALID_CLICK_TARGET)


def click_exposure_zone_checkboxes(zones):
    if type(zones) is not list:
        zones = [ zones ]

    for zone in zones:
        limit = len(zone)

        check = True
        row = 1
        while row < 24 and check:
            col = 1
            while col < 4 and check:
                label = driver.find_element_by_xpath(locations.AddDataEntrySetModal.exposure_zone_label(row, col)).text
                if zone == label[0:limit]:
                    driver.find_element_by_xpath(locations.AddDataEntrySetModal.Inputs.exposure_zone_checkbox(row, col)).click()
                    check = False
                    print('row:', row)
                    print('col:', col)
                    print('zone:', zone)
                    print('label:', label[0:limit])
                else:
                    col += 1
            row += 1


def click_data_entry_set_edit_link(set_name):
    check = True
    x = 2
    while check:
        try:
            label = driver.find_element_by_xpath(locations.data_entry_set_name(x)).text
            if set_name.lower() == label.lower():
                helpers.click_helper(locations.Links.data_entry_set_edit(x))
                check = False
            else:
                x += 1
        except NoSuchElementException:
            check = False
            print('Set not found.')


def click_data_entry_set_delete_link(set_name):
    check = True
    x = 2
    while check:
        try:
            label = driver.find_element_by_xpath(locations.data_entry_set_name(x)).text
            if set_name.lower() == label.lower():
                helpers.click_helper(locations.Links.data_entry_set_delete(x))
                check = False
            else:
                x += 1
        except NoSuchElementException:
            check = False
            print('Set not found.')


def set_up_new_data_entry_set(name, zones):
    add_data_entry_set_modal_click('name input', text=name)

    click_exposure_zone_checkboxes(zones)


def find_checked_zones():  # take this out
    checked_zones = []

    for col in range(1, 5):
        for row in range(1, 18):
            try:
                checkbox = driver.find_element_by_xpath('//table[@id="data_entry_sets_table"]/tbody/tr/td/input'.format(col, row))
                zone_name = driver.find_element_by_xpath(
                    '//table[@id="data_entry_sets_table"]/tbody/tr/td/span'.format(col, row)
                ).text

                if checkbox.is_selected():
                    checked_zones.append(zone_name)

            except NoSuchElementException:
                print(warn.SOME_PROBLEM)

    return checked_zones
