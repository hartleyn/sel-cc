
'''
	Created by Nick Hartley
	12/12/2017
'''

class Links:
	claim_documents = '//div[@id="data_entry_search"]/div/ul/li/a'
	release_documents = '//div[@id="data_entry_search"]/div/ul/li[2]/a'
	download_document = '//div[@id="data_entry_search"]/div/ul/li[3]/a'
	page_selector = '//td[@id="DataEntrySearch_toppager_center"]/table/tbody/tr/td[4]/div/a'
	
	
class Buttons:
	upload_document = '//div[@id="content"]/div[2]/div/div[2]/button'
	search = '//form[@id="DataEntrySearchForm"]/div[5]/button'
	clear = '//form[@id="DataEntrySearchForm"]/div[5]/button[2]'
	action = '//div[@id="data_entry_search"]/div/button'
	x = '//div[@id="upload_stack_modal"]/div/div/div/button'
	upload_stack = '//div[@id="upload_stack_modal"]/div/div/div[3]/button'
	search_type_label = '//md-switch[@id="stack_adv_search"]/div[2]/span'
	search_type_selection = "//md-switch[@id='stack_adv_search']/div/div[2]/div"
	
class Fields:
	data_entry_search_field_customer_number = "//input[@name='customer']"
	data_entry_search_field_certificate_id = "//input[@name='certificate_id']"
	data_entry_search_field_filename = "//input[@name='certificate_id']"
	data_entry_search_field_exposure_zone = "//div[@id='exposure_zone_chosen']/ul/li/input"
	data_entry_search_field_document_type = "//input[@value='Select Document Types']"
	data_entry_search_field_exempt_reasons_list_tag = "//div[@id='exempt_reason_chosen']/div[1]/ul[1]/li[1]"
	data_entry_search_field_exempt_reasons_div_tag = "//div[@id='exempt_reason_chosen']"
	data_entry_search_field_exempt_reasons_input_tag = "//div[@id='exempt_reason_chosen']/ul[1]/li[1]/input[1]"
	data_entry_search_field_certificate_status = "//select[@name='status']"
	data_entry_search_field_certificate_priority = "//select[@name='priority']"
	data_entry_search_field_certificate_source = "//select[@name='source']"
	data_entry_search_field_certificate_bucket = "//select[@name='bucket']"
	data_entry_search_field_certificate_location = "//select[@name='location']"
	
class IDs:
	data_entry_certificate_id_table_header_link = "jqgh_DataEntrySearch_certificate_or_filename"
	data_entry_customer_number_table_header_link = "jqgh_DataEntrySearch_customer_number"
	data_entry_status_table_header_link = "jqgh_DataEntrySearch_status"
	data_entry_exposure_zone_table_header_link = "jqgh_DataEntrySearch_exposure_zone"
	data_entry_source_table_header_link = "jqgh_DataEntrySearch_source"
	data_entry_priority_table_header_link = "jqgh_DataEntrySearch_priority"
	data_entry_age_table_header_link = "jqgh_DataEntrySearch_age"
	data_entry_account_table_header_link = "jqgh_DataEntrySearch_account"
	data_entry_stage_table_header_link = "jqgh_DataEntrySearch_status"	
	data_entry_pages_table_header_link = "jqgh_DataEntrySearch_merge_pages"
	search_next_page = "next_pager"
	search_first_page = "first_pager"
	search_prev_page = "prev_pager"
	search_last_page = "last_t_DataEntrySearch_toppager"
	select_stack_filter = "stack_filter"
	select_exposure_zone = "exposure_zone_chosen"
	exempt_reason = "exempt_reason_chosen"
	data_entry_search_field_created_date = 'created'
	
	
	