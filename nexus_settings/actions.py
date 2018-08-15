from general import helpers
from utilities import warnings as warn
import nexus_settings.locations as locations

__author__ = 'Nick Hartley'
# 3/9/2018


def click(target_name):
    target = target_name.lower()
    
    if target == 'united states':
        helpers.click_helper(locations.Links.united_states)
    elif target == 'canada':
        helpers.click_helper(locations.Links.canada)
    elif target == 'other':
        helpers.click_helper(locations.Links.other)
    elif target == 'assign nexus':
        helpers.click_helper(locations.Buttons.assign_nexus)
    else:
        print(warn.INVALID_CLICK_TARGET)


def us_edit_client_nexus_modal_click(target_name):
    target = target_name.lower()
    
    if target == 'toggle select all input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_toggle_select_all)
    elif target == 'alaska input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_alaska)
    elif target == 'alabama input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_alabama)
    elif target == 'arkansas input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_arkansas)
    elif target == 'american samoa input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_american_samoa)
    elif target == 'arizona input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_arizona)	
    elif target == 'california input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_california)
    elif target == 'colorado input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_colorado)
    elif target == 'connecticut input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_connecticut)
    elif target == 'colorado input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_colorado)
    elif target == 'connecticut input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_connecticut)
    elif target == 'district of columbia input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_district_of_columbia)
    elif target == 'delaware input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_delaware)
    elif target == 'florida input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_florida)
    elif target == 'georgia input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_georgia)
    elif target == 'guam input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_guam)
    elif target == 'hawaii input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_hawaii)
    elif target == 'iowa input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_iowa)
    elif target == 'idaho input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_idaho)
    elif target == 'illinois input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_illinois)
    elif target == 'indiana input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_indiana)
    elif target == 'kansas input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_kansas)
    elif target == 'kentucky input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_kentucky)
    elif target == 'louisiana input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_louisiana)
    elif target == 'massachusetts input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_massachusetts)
    elif target == 'maryland input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_maryland)
    elif target == 'maine input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_maine)
    elif target == 'michigan input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_michigan)
    elif target == 'minnesota input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_minnesota)
    elif target == 'missouri input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_missouri)
    elif target == 'northern mariana islands input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_northern_mariana_islands)
    elif target == 'mississippi input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_mississippi)
    elif target == 'montana input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_montana)
    elif target == 'north carolina input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_north_carolina)
    elif target == 'north dakota input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_north_dakota)
    elif target == 'nebraska input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_nebraska)
    elif target == 'new hampshire input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_hampshire)
    elif target == 'new jersey input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_jersey)
    elif target == 'new mexico input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_mexico)
    elif target == 'nevada input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_nevada)
    elif target == 'new york input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_york)
    elif target == 'ohio input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_ohio)
    elif target == 'oklahoma input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_oklahoma)
    elif target == 'oregon input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_oregon)
    elif target == 'pennsylvania input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_pennsylvania)
    elif target == 'puerto rico input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_puerto_rico)
    elif target == 'rhode island input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_rhode_island)
    elif target == 'south carolina input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_south_carolina)
    elif target == 'south dakota input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_south_dakota)
    elif target == 'tennessee input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_tennessee)
    elif target == 'texas input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_texas)
    elif target == 'utah input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_utah)
    elif target == 'virginia input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_virginia)
    elif target == 'vermont input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_vermont)
    elif target == 'washington input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_washington)
    elif target == 'wisconsin input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_wisconsin)
    elif target == 'west virginia input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_west_virginia)
    elif target == 'wyoming input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_wyoming)
    elif target == 'us virgin islands input':
        helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_us_virgin_islands)
    elif target == 'update client nexus button':
        helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_update_client_nexus)
    elif target == 'cancel button':
        helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_cancel)
    elif target == 'close button':
        helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_close)
    else:
        print(warn.INVALID_CLICK_TARGET)


def canada_edit_client_nexus_modal_click(target_name):
    target = target_name.lower()
    
    if target == 'toggle select all input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_toggle_select_all)
    elif target == 'alberta input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_alberta)
    elif target == 'british columbia input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_british_columbia)
    elif target == 'manitoba input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_manitoba)	
    elif target == 'new brunswick input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_new_brunswick)
    elif target == 'newfoundland input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_newfoundland)
    elif target == 'nova scotia input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_nova_scotia)
    elif target == 'ontario input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_ontario)
    elif target == 'prince edwards island input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_prince_edwards_island)
    elif target == 'quebec input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_quebec)
    elif target == 'sasketchewan input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_saskatchewan)
    elif target == 'yukon input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_yukon)
    elif target == 'canadian federal input':
        helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_canadian_federal)
    elif target == 'close button':
        helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_close)
    elif target == 'cancel button':
        helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_cancel)
    elif target == 'update client nexus button':
        helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_close)
    else:
        print(warn.INVALID_CLICK_TARGET)


def other_edit_client_nexus_modal_click(target_name):
    target = target_name.lower()
    
    if target == 'toggle select all input':
        helpers.click_helper(locations.Inputs.other_edit_client_nexus_modal_toggle_select_all)
    elif target == 'close button':
        helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_close)
    elif target == 'cancel button':
        helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_cancel)
    elif target == 'update client nexus button':
        helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_update_client_nexus)
    else:
        print(warn.INVALID_CLICK_TARGET)


def success_modal_click(target_name):
    target = target_name.lower()
    
    if target == 'ok button':
        helpers.click_helper(locations.Buttons.success_modal_ok)
    elif target == 'x button' or target == 'close button':
        helpers.click_helper(locations.Buttons.success_modal_x)
    else:
        print(warn.INVALID_CLICK_TARGET)
