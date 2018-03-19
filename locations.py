
'''
	Created by Nick Hartley
	3/14/2018
'''


class Buttons:
	upload = '//button[@id="upload_file"]'
	import_customer_data = '//button[@id="import_data"]'
	success_modal_ok = '//*[@id="success_prompt_dialog"]/div/div/div[3]/button'
	success_modal_close = '//*[@id="success_prompt_dialog"]/div/div/div[1]/button'
	error_modal_ok = '//*[@id="error_dialog"]/div/div/div[3]/button'
	error_modal_close = '//*[@id="error_dialog"]/div/div/div[1]/button'
	
class Inputs:
	choose_file = '//input[@id="importfile"]'