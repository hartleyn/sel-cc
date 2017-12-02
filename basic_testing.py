addr = ['124', 'Conch', 'Street', 'Bikini', 'Bottom', 'CA', 'US', '27716']
output = ''
for x in range(0, len(addr)):
	output += addr[x]
	
	if x != len(addr) - 1:
		output += ' '
print(output)