import time
import general.helpers as helpers
import account_details.locations as locations

__author__ = 'Nick Hartley'
# 3/8/18


def tabs_click(target_name):
    target = target_name.lower()

    time.sleep(2)

    if target == 'details':
        helpers.click_helper(locations.Links.details_tab)
    elif target == 'company hierarchy':
        helpers.click_helper(locations.Links.company_hierarchy_tab)
    elif target == 'document types':
        helpers.click_helper(locations.Links.document_types_tab)
    elif target == 'features':
        helpers.click_helper(locations.Links.features_tab)
    else:
        print('Invalid target requested.')

    time.sleep(2)


def details_tab_click(target_name):
    target = target_name.lower()

    if target == 'account name input':
        helpers.click_helper(locations.DetailsTab.Inputs.account_name)
    elif target == 'zuora id input':
        helpers.click_helper(locations.DetailsTab.Inputs.zuora_id)
    elif target == 'salesforce id input':
        helpers.click_helper(locations.DetailsTab.Inputs.salesforce_id)
    elif target == 'address line 1 input':
        helpers.click_helper(locations.DetailsTab.Inputs.address_line_1)
    elif target == 'address line 2 input':
        helpers.click_helper(locations.DetailsTab.Inputs.address_line_2)
    elif target == 'city input':
        helpers.click_helper(locations.DetailsTab.Inputs.city)
    elif target == 'country select':
        helpers.click_helper(locations.DetailsTab.Selects.country)
    elif target == 'state/province select':
        helpers.click_helper(locations.DetailsTab.Selects.state_province)
    elif target == 'zip input':
        helpers.click_helper(locations.DetailsTab.Inputs.zip)
    elif target == 'phone input':
        helpers.click_helper(locations.DetailsTab.Inputs.phone)
    elif target == 'internal input':
        helpers.click_helper(locations.DetailsTab.Inputs.internal_checkbox)
    elif target == 'sandbox input':
        helpers.click_helper(locations.DetailsTab.Inputs.sandbox_checkbox)
    elif target == 'update account button':
        helpers.click_helper(locations.DetailsTab.Buttons.update_account)
    elif target == 'reset button':
        helpers.click_helper(locations.DetailsTab.Buttons.reset)
    elif target == 'update company logo':
        helpers.click_helper(locations.DetailsTab.Links.update_company_logo)
    else:
        print('Invalid target requested.')


def company_hierarchy_tab_click(target_name):
    target = target_name.lower()

    if target == 'add company button':
        location = locations.CompanyHierarchyTab.Buttons.add_company
        helpers.click_helper(location)
    elif target == 'add company grouping button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_grouping
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


def add_company_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'display name input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_display_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'legal name input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_legal_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'use address input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_use_address_checkbox
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 1 input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_address_line_1
        helpers.click_or_type(location, **kwargs)
    elif target == 'address line 2 input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_address_line_2
        helpers.click_or_type(location, **kwargs)
    elif target == 'city input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_city
        helpers.click_or_type(location, **kwargs)
    elif target == 'country select':
        location = locations.CompanyHierarchyTab.Selects.add_company_modal_country
        helpers.click_or_select(location, **kwargs)
    elif target == 'state/province select':
        location = locations.CompanyHierarchyTab.Selects.add_company_modal_state
        helpers.click_or_select(location, **kwargs)
    elif target == 'zip input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_zip
        helpers.click_or_type(location, **kwargs)
    elif target == 'phone input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_phone
        helpers.click_or_type(location, **kwargs)
    elif target == 'fein input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_modal_fein
        helpers.click_or_type(location, **kwargs)
    elif target == 'add button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_modal_add
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_modal_close
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


def add_company_grouping_modal_click(target_name, **kwargs):
    target = target_name.lower()

    if target == 'name input':
        location = locations.CompanyHierarchyTab.Inputs.add_company_grouping_modal_name
        helpers.click_or_type(location, **kwargs)
    elif target == 'add button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_add
        helpers.click_helper(location)
    elif target == 'cancel button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_cancel
        helpers.click_helper(location)
    elif target == 'close button':
        location = locations.CompanyHierarchyTab.Buttons.add_company_grouping_modal_close
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


def document_types_tab_click(target_name):
    target = target_name.lower()

    if target == 'sales and use tax input':
        location = locations.DocumentTypesTab.Inputs.sales_and_use_tax_checkbox
        helpers.click_helper(location)
    elif target == 'federal withholding input':
        location = locations.DocumentTypesTab.Inputs.federal_withholding_checkbox
        helpers.click_helper(location)
    elif target == 'excise certificates input':
        location = locations.DocumentTypesTab.Inputs.excise_licenses_checkbox
        helpers.click_helper(location)
    elif target == 'vat input':
        location = locations.DocumentTypesTab.Inputs.vat_checkbox
        helpers.click_helper(location)
    elif target == 'excise certificates input':
        location = locations.DocumentTypesTab.Inputs.excise_certificates_checkbox
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


def features_tab_click(target_name):
    target = target_name.lower()

    if target == 'add customer input':
        location = locations.FeaturesTab.Inputs.add_customer
        helpers.click_helper(location)
    elif target == 'api exclude input':
        location = locations.FeaturesTab.Inputs.api_exclude
        helpers.click_helper(location)
    elif target == 'auto add input':
        location = locations.FeaturesTab.Inputs.auto_add
        helpers.click_helper(location)
    elif target == 'barcode prefix input':
        location = locations.FeaturesTab.Inputs.barcode_prefix
        helpers.click_helper(location)
    elif target == 'campaigns v2 input':
        location = locations.FeaturesTab.Inputs.campaigns_v2
        helpers.click_helper(location)
    elif target == 'configure template input':
        location = locations.FeaturesTab.Inputs.configure_template
        helpers.click_helper(location)
    elif target == 'cover letter input':
        location = locations.FeaturesTab.Inputs.cover_letter
        helpers.click_helper(location)
    elif target == 'disable certificate input':
        location = locations.FeaturesTab.Inputs.disable_certificates
        helpers.click_helper(location)
    elif target == 'e-commerce plugin input':
        location = locations.FeaturesTab.Inputs.ecommerce_plugin
        helpers.click_helper(location)
    elif target == 'force auto input':
        location = locations.FeaturesTab.Inputs.force_auto
        helpers.click_helper(location)
    elif target == 'mobile app input':
        location = locations.FeaturesTab.Inputs.mobile_app
        helpers.click_helper(location)
    elif target == 'public wizard input':
        location = locations.FeaturesTab.Inputs.public_wizard
        helpers.click_helper(location)
    elif target == 'restrict the input':
        location = locations.FeaturesTab.Inputs.restrict_the
        helpers.click_helper(location)
    elif target == 'terms and input':
        location = locations.FeaturesTab.Inputs.terms_and
        helpers.click_helper(location)
    elif target == 'tin check input':
        location = locations.FeaturesTab.Inputs.tin_check
        helpers.click_helper(location)
    elif target == 'vat id input':
        location = locations.FeaturesTab.Inputs.vat_id
        helpers.click_helper(location)
    elif target == 'welcome letter input':
        location = locations.FeaturesTab.Inputs.welcome_letter
        helpers.click_helper(location)
    else:
        print('Invalid target requested.')


def complete_add_company_form(display_name, legal_name, use_address, address_line_1, address_line_2, city, country, state, zip, phone):
    add_company_modal_click('display name input', text=display_name)

    add_company_modal_click('legal name input', text=legal_name)

    if use_address:
        add_company_modal_click('use address input')
    else:
        add_company_modal_click('address line 1 input', text=address_line_1)

        add_company_modal_click('address line 2 input', text=address_line_2)

        add_company_modal_click('city input', text=city)

        add_company_modal_click('country select', select=country)
        # helpers.select_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_country, country)

        add_company_modal_click('state/province select', select=state)
        # helpers.select_helper(locations.CompanyHierarchyTab.Selects.add_company_modal_state, state)

        add_company_modal_click('zip input', text=zip)

    add_company_modal_click('phone input', text=phone)
