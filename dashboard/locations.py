
__author__ = 'Nick Hartley'
# 5/18/2018


class Buttons:
    add_widget = '//*[@id="manage_dashboard_link"]'


class MessageCenter:
    class Buttons:
        minimize = '//*[@id="widget_8"]/i[2]'
        maximize = '//*[@id="widget_8"]/i[3]'
        close = '//*[@id="widget_8"]/i[1]'
        prev = '//*[@id="message_center_page_center"]/table/tbody/tr/td[2]'
        next = '//*[@id="message_center_page_center"]/table/tbody/tr/td[6]'

    class Links:
        date_header = '//*[@id="jqgh_message_center_table_created"]'
        refresh = '//*[@id="message_center_widget"]/div[2]/a'
        full_report = '//*[@id="message_center_widget"]/div[2]/a[2]'

        # xpath builder for message link, as determined by the message row
        # 'row' argument is incremented to account for invisible first <tr> element
        @staticmethod
        def message_link_row(row):
            row = int(row)
            row += 1
            xpath = '//*[@id="message_center_table"]/tbody/tr[{}]/td[3]/a'.format(str(row))

            return xpath


class DownloadCenter:
    class Buttons:
        minimize = '//*[@id="widget_9"]/i[2]'
        maximize = '//*[@id="widget_9"]/i[3]'
        close = '//*[@id="widget_9"]/i[1]'
        prev = '//*[@id="download_center_page_center"]/table/tbody/tr/td[2]'
        next = '//*[@id="download_center_page_center"]/table/tbody/tr/td[6]'

    class Links:
        created_header = '//*[@id="jqgh_download_center_table_created"]'
        refresh = '//*[@id="download_center_widget"]/div[2]/a'
        full_report = '//*[@id="download_center_widget"]/div[2]/a[2]'

        @staticmethod
        def download_link_row(row):
            row = int(row)
            row += 1
            xpath = '//*[@id="download_center_table"]/tbody/tr[{}]/td[6]/span/a'.format(str(row))

            return xpath
