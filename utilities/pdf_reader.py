import os
import glob
import PyPDF2 as reader
from test_base import debug, slash, download_path

__author__ = 'Nick Hartley'
# 3/18/2018


def get_request_link_from_request_pdf():
    full_path = '{}{}*.pdf'.format(download_path, slash)
    # full_path = test_base.download_path + test_base.slash + '*.pdf'
    list_of_files = glob.glob(full_path)
    latest_file = max(list_of_files, key=os.path.getctime)

    if debug:
        print(latest_file)

    pdf_file = open(latest_file, 'rb')  # Change to 'with' statement

    pdf_reader = reader.PdfFileReader(pdf_file)

    pdf_file.close()

    if debug:
        print(pdf_reader.numPages)

    page = pdf_reader.getPage(0)
    text = page.extractText()
    text_split = text.split()

    for word in text_split:
        if word[0:5] == 'https' and len(word) > 32:
            if debug:
                print(word)
            return word

    print('No request link found. Ensure that the most recent PDF file in your download directory is a request PDF.')


def get_request_links_from_merged_pdf_file():
    """
    Function for retrieving request codes from a merged PDF campaign request.

    Updated 5/24/2018
    """
    full_path = '{}{}*.pdf'.format(download_path, slash)
    # full_path = test_base.download_path + test_base.slash + '*.pdf'
    list_of_files = glob.glob(full_path)
    latest_file = max(list_of_files, key=os.path.getctime)

    if debug:
        print(latest_file)

    pdf_file = open(latest_file, 'rb')

    pdf_reader = reader.PdfFileReader(pdf_file)

    if debug:
        print(pdf_reader.numPages)

    links = []
    for x in range(pdf_reader.numPages):
        page = pdf_reader.getPage(x)

        text = page.extractText()
        text_split = text.split()

        for word in text_split:
            if word[0:31] == 'https://beta.certexpress.com?r=':
                links.append(word)

    if debug:
        print(links)
    return links
