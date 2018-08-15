
__author__ = 'Nick Hartley'
# 5/7/2018


def data_entry_set_name(row):
    row = int(row)
    row += 1
    return '//*[@id="data_entry_sets"]/tbody/tr[' + str(row) + ']/td[2]'


class Buttons:
    add_data_entry_set = '//*[@id="add_set_btn"]'


class Links:
    name_header = '//*[@id="jqgh_data_entry_sets_tag"]'

    @staticmethod
    def data_entry_set_edit(row):
        row = int(row)
        row += 1
        return '//*[@id="data_entry_sets"]/tbody/tr[' + str(row) + ']/td[2]/a'

    @staticmethod
    def data_entry_set_delete(row):
        row = int(row)
        row += 1
        return '//*[@id="data_entry_sets"]/tbody/tr[' + str(row) + ']/td[2]/a[2]'


class AddDataEntrySetModal:
    @staticmethod
    def exposure_zone_label(row, col):
        return '//*[@id="data_entry_sets_table"]/tbody/tr[' + str(row) + ']/td[' + str(col) + ']/span'

    class Buttons:
        add = '//*[@id="insert_set_btn"]'
        cancel = '//*[@id="div_add"]/button[2]'
        close = '//*[@id="add_data_entry_sets_modal"]/div/div/div[1]/button'

    class Inputs:
        name = '//*[@id="name"]'

        @staticmethod
        def exposure_zone_checkbox(row, col):
            return '//*[@id="data_entry_sets_table"]/tbody/tr[' + str(row) + ']/td[' + str(col) + ']/input'


class EditDataEntrySetModal:
    @staticmethod
    def exposure_zone_label(row, col):
        return '//*[@id="data_entry_sets_table"]/tbody/tr[' + str(row) + ']/td[' + str(col) + ']/span'

    class Buttons:
        update = '//*[@id="update_set_btn"]'
        cancel = '//*[@id="div_update"]/button[3]'
        close = '//*[@id="add_data_entry_sets_modal"]/div/div/div[1]/button'

    class Inputs:
        name = '//*[@id="name"]'

        @staticmethod
        def exposure_zone_checkbox(row, col):
            return '//*[@id="data_entry_sets_table"]/tbody/tr[' + str(row) + ']/td[' + str(col) + ']/input'


class DeleteModal:
    class Buttons:
        ok = '//*[@id="prompt_dialog"]/div/div/div[3]/button[1]'
        cancel = '//*[@id="prompt_dialog"]/div/div/div[3]/button[2]'
        close = '//*[@id="prompt_dialog"]/div/div/div[1]/button'
