import os
import glob
import test_base
import PyPDF2 as reader

'''
	Created by Nick Hartley
	3/18/2018
'''

def get_request_link_from_request_pdf():
	full_path = test_base.download_path + '\\*.pdf'
	list_of_files = glob.glob(full_path)
	latest_file = max(list_of_files, key=os.path.getctime)
	print(latest_file)

	pdf_file = open(latest_file, 'rb')

	pdf_reader = reader.PdfFileReader(pdf_file)
	print(pdf_reader.numPages)
	page = pdf_reader.getPage(0)
	text = page.extractText()
	text_split = text.split( )

	for word in text_split:
		if word[0:5] == 'https' and len(word) > 32:
			print(word)
			return word
			
	print('No request link found. Ensure that the most recent PDF file in your download directory is a request PDF.')