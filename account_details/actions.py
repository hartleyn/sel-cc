import general_actions.helpers as helpers
import account_details.locations as locations

'''
	Created by Nick Hartley
	3/8/18
'''


def tabs_click(target_name):
	target = target_name.lower()
	
	if target == 'details':
		return helpers.click_helper(locations.Links.details_tab)
	elif target == 'company hierarchy':
		return helpers.click_helper(locations.Links.company_hierarchy_tab)
	elif target == 'document types':
		return helpers.click_helper(locations.Links.document_types_tab)
	elif target == 'features':
		return helpers.click_helper(locations.Links.features_tab)
	else:
		print('Invalid target requested.')

def details_tab_click(target_name):
	target = target_name.lower()
	
	if target == 'account name input':
		return helpers.click_helper(locations.DetailsTab.Inputs.account_name)
	elif target == 'zuora id input':
		return helpers.click_helper(locations.DetailsTab.Inputs.zuora_id)
	elif target == 'salesforce id input':
		return helpers.click_helper(locations.DetailsTab.Inputs.salesforce_id)
	elif target == 'address line 1 input':
		return helpers.click_helper(locations.DetailsTab.Inputs.address_line_1)
	elif target == 'address line 2 input':
		return helpers.click_helper(locations.DetailsTab.Inputs.address_line_2)
	elif target == 'city input':
		return helpers.click_helper(locations.DetailsTab.Inputs.city)
	elif target == 'country select':
		return helpers.click_helper(locations.DetailsTab.Selects.country)
	elif target == 'state/province select':
		return helpers.click_helper(locations.DetailsTab.Selects.state_province)
	elif target == 'zip input':
		return helpers.click_helper(locations.DetailsTab.Inputs.zip)
	elif target == 'phone input':
		return helpers.click_helper(locations.DetailsTab.Inputs.phone)
	elif target == 'internal input':
		return helpers.click_helper(locations.DetailsTab.Inputs.internal_checkbox)
	elif target == 'sandbox input':
		return helpers.click_helper(locations.DetailsTab.Inputs.sandbox_checkbox)
	elif target == 'update account button':
		return helpers.click_helper(locations.DetailsTab.Buttons.update_account)
	elif target == 'reset button':
		return helpers.click_helper(locations.DetailsTab.Buttons.reset)
	elif target == 'update company logo':
		return helpers.click_helper(locations.DetailsTab.Links.update_company_logo)
	else:
		print('Invalid target requested.')
	
def company_hierarchy_click(target_name):
	target = target_name.lower()
	
	if target == 'add company button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company)
	elif target == 'add company grouping button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_grouping)
	else:
		print('Invalid target requested.')
	
def add_company_modal_click(target_name):
	target = target_name.lower()
	
	if target == 'display name input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_display_name)
	elif target == 'legal name input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_legal_name)
	elif target == 'use address input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_use_address_checkbox)
	elif target == 'address line 1 input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_address_line_1)
	elif target == 'address line 2 input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_address_line_2)
	elif target == 'city input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_city)	
	elif target == 'country select':
		return helpers.click_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_address_line_country)
	elif target == 'state/province select':
		return helpers.click_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_address_line_state_province)
	elif target == 'zip input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_zip)
	elif target == 'phone input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_phone)
	elif target == 'fein input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_modal_fein)
	elif target == 'add button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_modal_add)
	elif target == 'cancel button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_modal_close)
	else:
		print('Invalid target requested.')

def add_company_grouping_modal_click(target_name):
	target = target.lower()
	
	if target == 'name input':
		return helpers.click_helper(locations.CompanyHierarchyTab.Inputs.add_company_grouping_modal_name)
	elif target == 'add button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_add)
	elif target == 'cancel button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_cancel)
	elif target == 'close button':
		return helpers.click_helper(locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_close)		
	else:
		print('Invalid target requested.')
		
def document_types_tab_click(target_name):
	target = target_name.lower()
		
	if target == 'sales and use tax input':
		return helpers.click_helper(locations.DocumentTypesTab.Inputs.sales_and_use_tax_checkbox)
	elif target == 'federal withholding input':
		return helpers.click_helper(locations.DocumentTypesTab.Inputs.federal_withholding_checkbox)
	elif target == 'excise certificates input':
		return helpers.click_helper(locations.DocumentTypesTab.Inputs.excise_licenses_checkbox)
	elif target == 'vat input':
		return helpers.click_helper(locations.DocumentTypesTab.Inputs.vat_checkbox)
	elif target == 'excise certificates input':
		return helpers.click_helper(locations.DocumentTypesTab.Inputs.excise_certificates_checkbox)
	else:
		print('Invalid target requested.')
		
def features_tab_click(target_name):
	target = target_name.lower()
	
	if target == 'add customer input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.add_customer)
	elif target == 'api exclude input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.api_exlude)
	elif target == 'auto add input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.auto_add)
	elif target == 'barcode prefix input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.barcode_prefix)
	elif target == 'campaigns v2 input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.campaigns_v2)
	elif target == 'configure template input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.configure_template)
	elif target == 'cover letter input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.cover_letter)
	elif target == 'disable certificate input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.disable_certificates)
	elif target == 'e-commerce plugin input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.ecommerce_plugin)
	elif target == 'force auto input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.force_auto)
	elif target == 'mobile app input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.mobile_app)
	elif target == 'public wizard input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.public_wizard)
	elif target == 'restrict the input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.restrict_the)
	elif target == 'terms and input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.terms_and)
	elif target == 'tin check input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.tin_check)
	elif target == 'vat id input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.vat_id)
	elif target == 'welcome letter input':
		return helpers.click_helper(locations.FeaturesTab.Inputs.welcome_letter)
	else:
		print('Invalid target requested.')
		
def complete_add_company_form(display_name, legal_name, use_address, address_line_1, address_line_2, city, country, state, zip, phone):
	add_company_modal_click('display name input').send_keys(display_name)
	
	add_company_modal_click('legal name input').send_keys(legal_name)
	
	if use_address:
		add_company_modal_click('use address input')
	else:
		add_company_modal_click('address line 1 input').send_keys(address_line_1)
		
		add_company_modal_click('address line 2 input').send_keys(address_line_2)
		
		add_company_modal_click('city input').send_keys(city)
		
		helpers.select_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_country, country)
		
		helpers.select_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_state, state)
		
		add_company_modal_click('zip input').send_keys(zip)
	
	add_company_modal_click('phone input').send_keys(phone)
	
		
		
		
		
		
		
		
	
	
