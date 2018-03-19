import nexus_settings.locations as locations
import general_actions.helpers as helpers

'''
	Created by Nick Hartley
	3/9/2018
'''


def click(target_name):
	target = target_name.lower()
	
	if target == 'united states':
		return helpers.click_helper(locations.Links.united_states)
	elif target == 'canada':
		return helpers.click_helper(locations.Links.canada)
	elif target == 'other':
		return helpers.click_helper(locations.Links.other)
	elif target == 'assign nexus':
		return helpers.click_helper(locations.Buttons.assign_nexus)
	else:
		print('Invalid target requested.')
		
def us_edit_client_nexus_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'toggle select all input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_toggle_select_all)
	elif target == 'alaska input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_alaska)
	elif target == 'alabama input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_alabama)
	elif target == 'arkansas input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_arkansas)
	elif target == 'american samoa input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_american_samoa)
	elif target == 'arizona input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_arizona)	
	elif target == 'california input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_california)
	elif target == 'colorado input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_colorado)
	elif target == 'connecticut input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_connecticut)
	elif target == 'colorado input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_colorado)
	elif target == 'connecticut input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_connecticut)
	elif target == 'district of columbia input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_district_of_columbia)
	elif target == 'delaware input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_delaware)
	elif target == 'florida input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_florida)
	elif target == 'georgia input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_georgia)
	elif target == 'guam input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_guam)
	elif target == 'hawaii input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_hawaii)
	elif target == 'iowa input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_iowa)
	elif target == 'idaho input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_idaho)
	elif target == 'illinois input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_illinois)
	elif target == 'indiana input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_indiana)
	elif target == 'kansas input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_kansas)
	elif target == 'kentucky input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_kentucky)
	elif target == 'louisiana input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_louisiana)
	elif target == 'massachusetts input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_massachusetts)
	elif target == 'maryland input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_maryland)
	elif target == 'maine input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_maine)
	elif target == 'michigan input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_michigan)
	elif target == 'minnesota input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_minnesota)
	elif target == 'missouri input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_missouri)
	elif target == 'northern mariana islands input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_northern_mariana_islands)
	elif target == 'mississippi input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_mississippi)
	elif target == 'montana input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_montana)
	elif target == 'north carolina input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_north_carolina)
	elif target == 'north dakota input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_north_dakota)
	elif target == 'nebraska input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_nebraska)
	elif target == 'new hampshire input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_hampshire)
	elif target == 'new jersey input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_jersey)
	elif target == 'new mexico input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_mexico)
	elif target == 'nevada input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_nevada)
	elif target == 'new york input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_new_york)
	elif target == 'ohio input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_ohio)
	elif target == 'oklahoma input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_oklahoma)
	elif target == 'oregon input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_oregon)
	elif target == 'pennsylvania input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_pennsylvania)
	elif target == 'puerto rico input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_puerto_rico)
	elif target == 'rhode island input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_rhode_island)
	elif target == 'south carolina input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_south_carolina)
	elif target == 'south dakota input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_south_dakota)
	elif target == 'tennessee input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_tennessee)
	elif target == 'texas input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_texas)
	elif target == 'utah input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_utah)
	elif target == 'virginia input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_virginia)
	elif target == 'vermont input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_vermont)
	elif target == 'washington input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_washington)
	elif target == 'wisconsin input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_inconsin)
	elif target == 'west virginia input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_west_virginia)
	elif target == 'wyoming input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_wyoming)
	elif target == 'us virgin islands input':
		return helpers.click_helper(locations.Inputs.us_edit_client_nexus_modal_us_virgin_islands)
	elif target == 'update client nexus button':
		return helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_update_client_nexus)
	elif target == 'cancel button':
		return helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.Buttons.us_edit_client_nexus_modal_close)
	else:
		print('Invalid target requested.')
		
def canada_edit_client_nexus_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'toggle select all input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_toggle_select_all)
	elif target == 'alberta input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_alberta)
	elif target == 'british columbia input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_british_columbia)
	elif target == 'manitoba input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_manitoba)	
	elif target == 'new brunswick input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_new_brunswick)
	elif target == 'newfoundland input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_newfoundland)
	elif target == 'nova scotia input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_nova_scotia)
	elif target == 'ontario input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_ontario)
	elif target == 'prince edwards island input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_prince_edwards_island)
	elif target == 'quebec input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_quebec)
	elif target == 'sasketchewan input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_sasketchewan)
	elif target == 'yukon input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_yukon)
	elif target == 'canadian federal input':
		return helpers.click_helper(locations.Inputs.canada_edit_client_nexus_modal_canadian_federal)
	elif target == 'close button':
		return helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_close)
	elif target == 'cancel button':
		return helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_cancel)
	elif target == 'update client nexus button':
		return helpers.click_helper(locations.Buttons.canada_edit_client_nexus_modal_close)
	else:
		print('Invalid target requested.')

def other_edit_client_nexus_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'toggle select all input':
		return helpers.click_helper(locations.Inputs.other_edit_client_nexus_modal_toggle_select_all)
	elif target == 'close button':
		return helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_close)
	elif target == 'cancel button':
		return helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_cancel)
	elif target == 'update client nexus button':
		return helpers.click_helper(locations.Buttons.other_edit_client_nexus_modal_update_client_nexus)
	else:
		print('Invalid target requested.')







		
		