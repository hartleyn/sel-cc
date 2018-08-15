

__author__ = 'Nick Hartley'
# 5/19/2018


class Buttons:
    upload = '//button[@id="upload_file"]'
    delete_customer_data = '//button[@id="import_data"]'
    confirm_modal_ok = '//*[@id="prompt_dialog"]/div/div/div[3]/button[1]'
    confirm_modal_cancel = '//*[@id="prompt_dialog"]/div/div/div[3]/button[2]'
    confirm_modal_close = '//*[@id="prompt_dialog"]/div/div/div[1]/button'
    success_modal_ok = '//div[@id="success_prompt_dialog"]/div/div/div[3]/button'
    success_modal_close = '//*[@id="success_prompt_dialog"]/div/div/div[1]/button'
    error_modal_ok = '//*[@id="error_dialog"]/div/div/div[3]/button'
    error_modal_close = '//*[@id="error_dialog"]/div/div/div[1]/button'


class Inputs:
    choose_file = '//input[@id="importfile"]'
