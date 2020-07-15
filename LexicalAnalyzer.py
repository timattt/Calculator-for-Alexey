operators = ['(', ')', '*', '/', '+', '-']
delimiters = [' ', '\t', '\n']

def tokenize(text:str) -> list:
	""" This method tokenizes string into operators (as chars) and numbers (as ints) """

	# to ensure that the last number will be taken 
	text += delimiters[0]
	
	# some nice vars
	result = []
	raw_number = ""
	
	for val in text:
		# conditions
		isOperator = val in operators
		isDelimiter = val in delimiters
		isNumber = val.isdigit()

		# if it is operator
		if isOperator:
			result.append(val)
			
		# if it may be number
		if isNumber:
			raw_number += val
		
		# flush number if it is ending
		if (isOperator or isDelimiter) and len(raw_number) > 0:
			result.append(int(raw_number))
			raw_number = ""
	print("Tokenized successfully! Tokens:")
	print(result)
	return result
