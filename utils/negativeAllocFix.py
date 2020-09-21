import re

def negativeAllocFix(err, history):
	
	with open( err.getFilename(), "r") as f:
		data = f.readlines()
		
	problemLineNum = err.getProblemLines()[len(err.getProblemLines())-1] - 1
	problemLine = data[problemLineNum]

	if problemLine.find('malloc') >= 0:
		expStart = problemLine.find('malloc(') + 7
		
	elif problemLine.find('realloc') >= 0:
		expStart = problemLine.rfind(',') + 1
		
	expEnd = problemLine.rfind(')') 
		
	exp = problemLine[expStart : expEnd]
	exp = 'abs(' + exp + ')'
		
	fixLine = problemLine[0:expStart] + exp + ');\n'
		
	data[problemLineNum] = fixLine
	
	
	history.append(problemLine.strip())
		
	with open( err.getFilename(), "w") as f:
			for line in data:
				f.write(line)
