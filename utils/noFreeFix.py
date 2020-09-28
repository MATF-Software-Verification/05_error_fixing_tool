import re

def noFreeFix(err, history):
	
	with open( err.getFilename(), "r") as f:
		data = f.readlines()
	
	
	problemLine = data[err.getProblemLines()[len(err.getProblemLines())-1] - 1]


	if problemLine.find('(malloc|calloc|realloc)(.+);'):
		var = problemLine[0 : problemLine.find('=')].strip()
		
		var = var.split(' ')[-1]
		star = 0
		for i in range(len(var)):
			if (var [i] == '*'):
				star = star + 1
		var = var[star : ]
			
		
		malloc_var = []
		for i in range(len(data)):
			if data[i].find(var + ' = ' + 'malloc')>=0:
				malloc_var.append(i)
			
		for i in range(len(data)):
			if data[i].find('return 0;') >= 0:
				#free_line_num = i
				malloc_var.append(i)

		
		m = len(malloc_var)

		if m == 1:
			k = 0
		else:
			k = 1
		
		for j in range(k, m):
			if m == 1:
				index = 0
			else:
				index = m - j
			n = len(data)
			data.append("")
			for i in range(n - 1, malloc_var[index]-1, -1):
				data[i + 1] = data[i]
		
			fix = "\tfree(" + var + ");\n"	
		
			data[malloc_var[index]] = fix
		
		
			history.append(problemLine.strip())
			err.setBugFix(fix)
			err.setChangedLine(malloc_var[index])
		
		
		with open( err.getFilename(), "w") as f:
			for line in data:
				f.write(line)
