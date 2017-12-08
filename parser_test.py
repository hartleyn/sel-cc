from html.parser import HTMLParser
from urllib import parse



class ParserTest(HTMLParser):
	href_arr = []
	title_arr = []
	count = 0
	
	def handle_starttag(self, tag, attrs,):
		
		if tag == 'a':
			print('LINK FOUND')
			self.count += 1
			for attr in attrs:
				if (str(attr)[0:8] == "('title'" or str(attr)[0:7] == "('href'") and str(attr)[10:19] != '/messages':
					print('	attr:', attr)
	
	def report_count(self):
		print(self.count, 'links found.')
'''
				if attribute == 'href':
					self.href_arr.append(value)
					
				if attribute == 'title':
					if value is not None:
						self.title_arr.append(value)
					else:
						self.title_arr.append('NO LINK TITLE')


	def print_links_info(self):
		print(self.href_arr)
		print(self.title_arr)
		#assert len(self.href_arr) == len(self.title_arr)
		
		length = len(self.href_arr)
		
		for x in range(0, length):
			if self.href_arr[x][0:9] != '/messages':
				print(' href: ', self.href_arr[x])
'''