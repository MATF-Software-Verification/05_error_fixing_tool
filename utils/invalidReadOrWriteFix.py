import re

def invalidReadOrWriteFix(err, history):

	f = open( err.getFilename(), "r")
	data = f.readlines()
	f.close()
	
	elemSize = ''
	bytesAfter = ''
	addition = ''

	# left
	bytesBefore = ''
	changeLeft = ''
	

	for elem in err.getProblemLines():
		if re.findall('[malloc|calloc|realloc].+;', data[elem-1]):
			lineToChange = data[elem-1]
			err.setChangedLine(elem)
			elemSize = int(re.findall('\d+', err.getErrorType())[0])
			break


	lineToChange = data[err.getProblemLines()[0]-1]
	err.setChangedLine(err.getProblemLines()[0])
	elemSize = int(re.findall('\d+', err.getErrorType())[0])

	for line in err.getErrorReason():
		if re.findall('Address [0-9a-zA-Z]+ is \d+ bytes after a block of size \d+ alloc\'d', line):
			bytesAfter = int(re.findall('\d+', line.split('is')[1])[0])
			break
		# left
		if re.findall('Address [0-9a-zA-Z]+ is \d+ bytes before a block of size \d+ alloc\'d', line):
			bytesBefore = int(re.findall('\d+', line.split('is')[1])[0])
			break
	#left
	if elemSize and (bytesAfter or bytesBefore):
		start = lineToChange.find('*')
		end = lineToChange.find('=')
		varType = lineToChange[0:start].strip()

		#if zbog levog
		if bytesAfter:
			addition = lineToChange[:lineToChange.rfind(')')] + ' + ' + 'sizeof(' + varType + ')*' \
				+ str((bytesAfter+elemSize)/elemSize) + ' );\n'

		#left
		elif bytesBefore:
			addition = lineToChange[:lineToChange.rfind(')')] + ' + ' + 'sizeof(' + varType + ')*' \
				+ str(1) + ' );\n'
			

		m = re.search('(malloc|calloc|realloc)(.+);', addition)
		if m:
			expressionData = m.group(2).replace('(', '', 1)[::-1].replace(')', '', 1)[::-1].strip()
			expressionData = re.sub('sizeof[ ]*\([ ]*(int|double|char|float)[ ]*\)', '1' , expressionData)
			addition = addition[:addition.find('(')+1] + ' sizeof(' + varType + ')*' + str(eval(expressionData)) + ' );\n'

		if addition not in history:
			err.setBug(lineToChange)
			err.setBugFix(addition)	
			history.append(addition)


		#left
		if bytesBefore:
			problemLine = data[err.getProblemLines()[1]-1]
			changeLeft = problemLine[:problemLine.find('[') + 1] + str(eval(expressionData)) + problemLine[problemLine.find(']'):]
			if changeLeft not in history:
				err.setBug(problemLine)
				err.setBugFix(changeLeft)
				history.append(changeLeft)


