__author__ = 'Nick Hartley'
# 5/4/2018


class Buttons:
    search_type_toggle = '//md-switch[@id="stack_adv_search"]/div[1]/div[2]/div'
    upload_document = '//div[@id="content"]/div[2]/div/div[2]/button'
    search = '//form[@id="DataEntrySearchForm"]/div[5]/button'
    clear = '//form[@id="DataEntrySearchForm"]/div[5]/button[2]'
    action = '//div[@id="data_entry_search"]/div/button'
    top_first = '//td[@id="first_t_DataEntrySearch_toppager"]/span'
    top_prev = '//td[@id="prev_t_DataEntrySearch_toppager"]/span'
    top_next = '//td[@id="next_t_DataEntrySearch_toppager"]/span'
    top_last = '//td[@id="last_t_DataEntrySearch_toppager"]/span'
    bottom_first = '//td[@id="first_pager"]/span'
    bottom_prev = '//td[@id="prev_pager"]/span'
    bottom_next = '//td[@id="next_pager"]/span'
    bottom_last = '//td[@id="last_pager"]/span'


class Selects:
    stack_filter = '//div[@id="search_stack_panel"]/div/h4/select'
    stage = '//form[@id="DataEntrySearchForm"]/div[2]/div[4]/select'
    priority = '//form[@id="DataEntrySearchForm"]/div[3]/div/div[2]/select'
    source = '//form[@id="DataEntrySearchForm"]/div[3]/div/div[3]/select'
    bucket = '//form[@id="DataEntrySearchForm"]/div[3]/div[2]/div[2]/select'
    location = '//form[@id="DataEntrySearchForm"]/div[3]/div[2]/div[3]/select'
    top_page_selector = '//td[@id="DataEntrySearch_toppager_center"]/table/tbody/tr/td[4]/div/a'
    bottom_page_selector = '//td[@id="pager_center"]/table/tbody/tr/td[3]/div/a'


class Inputs:
    customer = '//form[@id="DataEntrySearchForm"]/div[2]/div/input'
    exposure_zone = '//div[@id="exposure_zone_chosen"]/ul/li/input'
    document_category = '//div[@id="exempt_reason_chosen"]/ul/li/input'
    document_id = '//form[@id="DataEntrySearchForm"]/div[3]/div/div/input'
    created = '//form[@id="DataEntrySearchForm"]/div[3]/div/div[4]/input'
    document_type = '//div[@id="document_type_chosen"]/ul/li/input'
    check_all_documents = '//div[@id="jqgh_DataEntrySearch_cb"]/input'

    @staticmethod
    def results_row_checkbox(row):
        row = int(row)
        row += 1
        return '//table[@id="DataEntrySearch"]/tbody/tr[' + str(row) + ']/td/input'


class Links:
    @staticmethod
    def results_row(row):
        row = int(row)
        row += 1
        return '//table[@id="DataEntrySearch"]/tbody/tr[' + str(row) + ']'

    document_header = '//*[@id="jqgh_DataEntrySearch_certificate_or_filename"]'
    customer_number_header = '//*[@id="jqgh_DataEntrySearch_customer_number"]'
    stage_header = '//*[@id="jqgh_DataEntrySearch_status"]'
    account_header = '//*[@id="jqgh_DataEntrySearch_account"]'
    exposure_zone_header = '//*[@id="jqgh_DataEntrySearch_exposure_zone"]'
    source_header = '//*[@id="jqgh_DataEntrySearch_source"]'
    priority_header = '//*[@id="DataEntrySearch_priority"]'
    pages_header = '//*[@id="jqgh_DataEntrySearch_merge_pages"]'
    age_header = '//*[@id="jqgh_DataEntrySearch_age"]'


class UploadDocumentModal:
    class Buttons:
        close = '//div[@id="upload_stack_modal"]/div/div/div/button'
        upload_stack_button = '//div[@id="upload_stack_modal"]/div/div/div[3]/button'
        
    class Selects:
        priority = '//form[@id="upload_stack_form"]/div[2]/select'
        auto_split = '//form[@id="upload_stack_form"]/div[2]/div/select'
        bucket = '//form[@id="upload_stack_form"]/div[3]/div/select'
        document_type = '//form[@id="upload_stack_form"]/div[4]/div/div/select'
        exposure_zone = '//form[@id="upload_stack_form"]/div[4]/div/div/div/div/select'
        exempt_reason = '//form[@id="upload_stack_form"]/div[4]/div/div/div[2]/div/select'

    class Inputs:
        choose_file = '//form[@id="upload_stack_form"]/div/input'
        claim_document = '//form[@id="upload_stack_form"]/div[3]/input[2]'
        auto_split_page_count = '//div[@id="auto_merge_row"]/input'


class ValidateDocumentWindow:
    @staticmethod
    def exposure_zone_info_row(row):
        row = int(row)
        row += 1
        return '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[' + str(row) + ']'

    class Buttons:
        delete = '//div[@id="navbarCollapse"]/ul/li/button'
        defaults = '//div[@id="navbarCollapse"]/ul/li[2]/button'
        release = '//div[@id="navbarCollapse"]/ul/li[3]/button'
        download = '//div[@id="navbarCollapse"]/ul/li[4]/button'
        escalate = '//div[@id="navbarCollapse"]/ul/li[5]/button'
        validate = '//div[@id="navbarCollapse"]/ul/li[6]/label/button'
        advanced_search = '//*[@id="dataEntryForm"]/div[3]/div[1]/div[3]/div[2]/span[3]'
        add_customer = '//*[@id="dataEntryForm"]/div[3]/div[1]/div[3]/div[2]/span[2]'
        bulk_add = '//*[@id="dataEntryForm"]/div[3]/div[1]/div[3]/div[2]/span[1]'
        date_picker_effective_date = '//form[@id="dataEntryForm"]/div[3]/div/div[8]/div[2]/div/md-datepicker/button'
        clear = '//form[@id="dataEntryForm"]/div[3]/div/div[11]/div[2]/span'
        # clear = '//form[@id="dataEntryForm"]/div[3]/div/div[10]/div[2]/div[2]/div[2]/button'
        date_picker_expire_date = '//form[@id="dataEntryForm"]/div[3]/div/div[13]/div/table/tbody/tr[2]/td[3]/md-datepicker/button'
        never_expire = '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[2]/td[3]/span'
        validate_ids = '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[3]/td/label/button'
        success_ok = '/html/body/div[3]/md-dialog/md-dialog-actions/button'
        escalate_x = '//*[@id="dialogContent_2"]/div[1]/button'
        escalate_escalate = '/html/body/div[3]/md-dialog/md-dialog-actions/button'

        @staticmethod
        def exposure_zone_never_expire_row(row):
            row = int(row)
            row += 1
            return '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[' + str(row) + ']/td[3]/span'

    class Selects:
        document_type = '//form[@id="dataEntryForm"]/div[3]/div[1]/div[7]/div[1]/div/a'
        exempt_reason = '//div[@id="exempt_reason_chosen"]/a'
        location = '//div[@id="location_chosen"]/a'
        filter_state = '//div[@id="filter_state_id_chosen"]/a'
        filter_attribute_group = '//div[@id="filter_group_id_chosen"]/a'
        filter_attribute = '//div[@id="filter_attribute_id_chosen"]/a'
        escalate_reason = '//*[@id="dialogContent_2"]/div[2]/div/div[1]/select'

    class Inputs:
        customers = '//form[@id="dataEntryForm"]/div[3]/div/div[4]/div/span/input[2]'
        created_date = '//form[@id="dataEntryForm"]/div[3]/div/div[8]/div/div/input'
        effective_Date = '//form[@id="dataEntryForm"]/div[3]/div/div[8]/div[2]/div/md-datepicker/div/input'
        single_use_checkbox = '//form[@id="dataEntryForm"]/div[3]/div[1]/div[9]/div[2]/md-content/md-checkbox'
        # exposure_zones = '//div[@id="exposure_zones_chosen"]/ul/li[2]/input'
        exposure_zones = '//*[@id="exposure_zones_chosen"]/ul/li/input'
        invalid_reasons = '//div[@id="invalid_reasons_chosen"]/ul/li/input'
        customer_attributes = '//div[@id="customer_codes_chosen"]/ul/li/input'
        document_attributes = '//div[@id="certificate_codes_chosen"]/ul/li[2]/input'
        escalate_explain = '//*[@id="dialogContent_2"]/div[2]/div/div[2]/textarea'

        @staticmethod
        def exposure_zone_tax_id_row(row):
            row = int(row)
            row += 1
            return '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[' + str(row) + ']/td[2]/input'

        @staticmethod
        def exposure_zone_expire_date_row(row):
            row = int(row)
            row += 1
            return '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[' + str(
                row) + ']/td[3]/md-datepicker/div[1]/input'

        @staticmethod
        def exposure_zone_exempt_percentage_row(row):
            row = int(row)
            row += 1
            return '//*[@id="dataEntryForm"]/div[3]/div[1]/div[13]/div/table/tbody/tr[' + str(row) + ']/td[4]/input'


class MergeDocumentWindow:
    class Buttons:
        submit = '//button[@id="submit_merge"]'
        release_document = '//button[@id="release_anchor"]'
        flip_all_images = '//button[@id="flip_images"]'
        rotate_90_left = '//*[@id="merge_action_158_0"]/span[1]'
        rotate_90_right = '//*[@id="merge_action_158_0"]/span[2]'
        rotate_180 = '//*[@id="merge_action_158_0"]/span[3]'
        darken_contrast = '//*[@id="merge_action_158_0"]/span[4]'
        delete = '//*[@id="merge_action_158_0"]/span[5]'
        successful_merge_x = '//*[@id="success_prompt_next_dialog"]/div/div/div[1]/button'
        successful_merge_close = '//*[@id="success_prompt_close_btn"]'
        successful_merge_next = '//*[@id="success_prompt_next_btn"]'

    class Selects:
        document_type = '//*[@id="DocumentType0"]'
        exposure_zone = '//*[@id="ExposureZone0"]'
        document_category = '//*[@id="TaxCode0"]'
