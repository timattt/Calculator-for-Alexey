import LexicalAnalyzer
import SyntaxAnalyzer

def run(head) -> int:
	""" recursevly works on a node and generates a number """
	result = 0
	
	if head.name == "HEAD":
		result = run(head.children[0])
	if head.name == "P":
		for child in head.children:
			result += run(child)
	if head.name == "T":
		result = 1
		for child in head.children:
			result *= run(child)
	if head.name == "E":
		# number
		if len(head.values) == 1:
			result = head.values[0]
		# (...)
		else:
			result = run(head.children[0])
	return result
