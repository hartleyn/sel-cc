from bs4 import BeautifulSoup

'''
	Created by Nick Hartley
	12/11/2017
'''

def run(tag, driver, client, filename, sheetname):
	source = driver.page_source

	soup = BeautifulSoup(source, "html.parser")

	sheet = client.open(filename).worksheet(sheetname)

	sheet.update_cell(1, 1, "Element Text")
	sheet.update_cell(1, 2, "Variable Name")
	sheet.update_cell(1, 3, "ID/XPath")
	
	if tag == 'a':
		sheet.update_cell(1, 4, "Href")


	x = 2
	for link in soup.find_all(tag):
		finished = False

		if str(link.get('href'))[0:9] != '/messages':
			
			sheet.update_cell(x, 1, link.get_text())
			var_name = str(link.get_text()).lower()
			var_name = var_name.split( )
			name = ''
			for n in range(0, len(var_name)):
				name += var_name[n]
				
				if n != len(var_name) - 1:
					name += '_'
			sheet.update_cell(x, 2, name)
			
			string = ''
			for parent in link.parents:
				if finished == False:
					siblings = len(parent.find_previous_siblings(parent.name))
					siblings += 1
					if siblings > 0:
						try:
							string = '//' + str(parent.name) + '[@id="' + parent['id'] + '"]' + string + '/' + str(link.name)
							finished = True	
						except KeyError:
							siblings = len(parent.find_previous_siblings(parent.name))
							if siblings > 0:
								siblings += 1
								string = '/' + str(parent.name) + '[' + str(siblings) + ']' + string
							else:
								string = '/' + str(parent.name) + string
			if finished == False:
				string = '/' + string + '/' + str(link.name)
				string = string[0:2] + string[13:len(string)+1]
			
			siblings = len(link.find_previous_siblings(link.name))
			if siblings > 0:
				siblings += 1
				string += '[' + str(siblings) + ']'
			print(string)
			sheet.update_cell(x, 3, string)
			
			if tag == 'a':			
				sheet.update_cell(x, 4, link.get('href'))
			x += 1
			
			
def grab_input_locations(tag, driver, client, filename, sheetname):
	source = driver.page_source

	soup = BeautifulSoup(source, "html.parser")

	sheet = client.open(filename).worksheet(sheetname)
	
	if tag == 'input':
		sheet.update_cell(1, 1, 'Placeholder')
	sheet.update_cell(1, 2, 'ID')
	sheet.update_cell(1, 3, 'XPath')
	
	x = 2
	for input in soup.find_all(tag):
		finished = False
		
		try:
			var_name = str(input['name'])
			sheet.update_cell(x, 2, var_name)
		except KeyError:
			print('Input name not found.')
	
		try:
			if tag == 'input':
				placeholder = input['placeholder']
				sheet.update_cell(x, 1, placeholder)
		except KeyError:
			print('No placeholder found.')
		finally:		
			string = ''
			for parent in input.parents:
				if finished == False:
					siblings = len(parent.find_previous_siblings(parent.name))
					siblings += 1
					if siblings > 0:
						try:
							string = '//' + str(parent.name) + '[@id="' + parent['id'] + '"]' + string + '/' + str(input.name)
							finished = True	
						except KeyError:
							siblings = len(parent.find_previous_siblings(parent.name))
							if siblings > 0:
								siblings += 1
								string = '/' + str(parent.name) + '[' + str(siblings) + ']' + string
							else:
								string = '/' + str(parent.name) + string
			if finished == False:
				string = '/' + string + '/' + str(input.name)
				string = string[0:2] + string[13:len(string)+1]
				
			siblings = len(input.find_previous_siblings(input.name))
			if siblings > 0:
				siblings += 1
				string += '[' + str(siblings) + ']'
			print('XPath:', string)
			sheet.update_cell(x, 3, string)
			x += 1
			
			
			
			