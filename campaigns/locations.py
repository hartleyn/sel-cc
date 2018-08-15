
__author__ = 'Nick Hartley'
# 4/19/2018


class SetUpCampaign:
    class Inputs:
        campaign_title = '//input[@id="MailOutTitle"]'
        include_customers = '//input[@id="MailOutCampaignCustomersInclude"]'
        omit_customers = '//input[@id="MailOutCampaignCustomersIgnore"]'
        missing_exemption = '//input[@id="MailOutForMissing"]'
        invalid_exemption = '//input[@id="MailOutForInvalid"]'
        expired_certificate = '//input[@id="MailOutForExpired"]'
        include_soon_to_expire = '//input[@id="MailOutExpireFuture"]'
        include_soon_to_expire_days = '//input[@id="MailOutExpireDaysOut"]'
        taxable_exposures = '//input[@id="MailOutForTaxable"]'
        override = '//input[@id="MailOutForGood"]'
        billing_customers = '//input[@id="MailOutSendBill"]'
        shipping_customers = '//input[@id="MailOutSendShip"]'
        exclude_same_as = '//input[@id="MailOutExcludeSameas"]'
        expand_bill_to_ship = '//input[@id="MailOutExpandAddress"]'
        exempt_reasons = '//div[@id="MailOutCertificateTemplateId_chosen"]/ul/li/input'

    class Links:
        select_all = '//a[@id="assign_all"]'
        deselect_all = '//a[@id="assign_none"]'

    class Selects:
        document_type = '//select[@id="campaign-document-type"]'

    class Buttons:
        prepare_campaign = '//button[@id="prepare_mailing"]'


class EditCampaign:
    class Inputs:
        send_date = '//input[@id="MailOutSendDate0"]'
        requested_return_date = '//input[@id="MailOutReturnDate0"]'
        generate_date = '//input[@id="MailOutReadyForReviewDate0"]'
        include_most_recent = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[3]/label[1]/input'
        cover_letter_only = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[3]/label[2]/input'
        include_certexpress_access = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[3]/label[3]/input'
        automatically_send_round = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[4]/label/input'
        notes = '//textarea[@id="MailOutNotes"]'
        merged_file = '//*[@id="print_tab"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/label/input'
        zip_individual = '//*[@id="print_tab"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/label/input'
        zip_merged = '//*[@id="print_tab"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/label/input'

    class Selects:
        method = '//select[@id="MailOutMethod"]'
        email_template_cover_letter = '//select[@id="MailOutCoverLetterId"]'
        page_selector = '//td[@id="pager_center"]/table/tbody/tr/td[3]/div/a'

    class Links:
        overview = '//a[@id="tabs-home-head"]'
        add_round = '//a[@id="add_round"]'
        scheduling_and_delivery = '//table[@id="tabs_table"]/tbody/tr/td[1]/div/ul/li[1]/a'
        select_customers = '//table[@id="tabs_table"]/tbody/tr/td[1]/div/ul/li[2]/a'
        preview = '//table[@id="tabs_table"]/tbody/tr/td[1]/div/ul/li[3]/a'
        print = '//table[@id="tabs_table"]/tbody/tr/td[1]/div/ul/li[4]/a'
        send_emails = '//table[@id="tabs_table"]/tbody/tr/td[1]/div/ul/li[5]/a'
        clone_round = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[4]/ul/li[1]/a'
        delete_round = '//table[@id="tabs_table"]/tbody/tr/td[2]/div[1]/div[4]/ul/li[2]/a'
        customer_number_header = '//div[@id="jqgh_completion_table_customer_number"]'
        name_header = '//div[@id="jqgh_completion_table_name"]'

        # Tried something new - it stuck :)
        @staticmethod
        def round(number):
            xpath = '//a[@id="tabs-' + str(number) + '-head"]'
            return xpath

    class Buttons:
        delete_campaign = '//a[@id="delete_campaign"]'
        save_campaign_changes = '//a[@id="save_campaign_updates_top"]'
        export_overview_data = '//button[@id="export_overview_btn"]'
        send_compliance_document_requests = '//*[@id="email_tab"]/table/tbody/tr[2]/td/a'
        first = '//td[@id="first_pager"]/span'
        prev = '//td[@id="prev_pager"]/span'
        next = '//td[@id="next_pager"]/span'
        last = '//td[@id="last_pager"]/span'
        create_printable_file = '//*[@id="print_tab"]/table/tbody/tr[2]/td/a'
