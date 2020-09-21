import re

def noFreeFix(err, history):
	
	with open( err.getFilename(), "r") as f:
		data = f.readlines()
	
	
	problemLine = data[err.getProblemLines()[len(err.getProblemLines())-1] - 1]
	if problemLine.find('(malloc|calloc|realloc)(.+);'):
		var = problemLine[0 : problemLine.find('=')].strip()

		i = 0
		for i in range(len(data)):
			if data[i].find('return 0;') >= 0:
				return_line_num = i

		n = len(data)
		data.append("")
		for i in range(n-1, return_line_num-1, -1):
			data[i + 1] = data[i]
			
		data[return_line_num] = "\tfree(" + var + ");\n"	
		
		
		history.append(problemLine.strip())
		
		with open( err.getFilename(), "w") as f:
			for line in data:
				f.write(line)
