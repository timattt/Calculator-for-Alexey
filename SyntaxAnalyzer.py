import LexicalAnalyzer

class Node:
	children = []
	values = []
	name = ""
	
	def __init__(self, name:str) -> None:
		self.name = name
		
	def addChild(self, child) -> None:
		self.children.append(child)
		
	def addValue(self, val) -> None:
		print(val)
		self.values.append(val)

class TreeBuilder:
	currentString = []
	currentIndex = 0
	ancestors = []
	
	def hasMoreTokens(self) -> bool:
		return self.currentIndex < len(self.currentString)
	
	def __init__(self, val) -> None:
		self.currentString = val
		self.currentIndex = 0
		
	def currentToken(self) -> int or str:
		return self.currentString[self.currentIndex]	
	
	def currentNode(self) -> Node:
		return self.ancestors[-1]
	
	def currentIsOperator(self, tp:str):
		return self.hasMoreTokens() and self.currentToken() in LexicalAnalyzer.operators and self.currentToken() == tp
		
	def currentIsNumber(self):
		return self.hasMoreTokens() and not self.currentToken() in LexicalAnalyzer.operators
	
	def error(self, message:str) -> None:
		print("Compilation failed!")
		print(message)
		exit(0)
	
	def collectOperator(self, tp) -> None:
		if not self.currentIsOperator(tp):
			self.error("Expected operator " + tp)
		else:
			self.currentNode().addValue(tp)
			self.currentIndex += 1
		
	def tryOperator(self, tp) -> bool:
		if self.currentIsOperator(tp):
			self.collectOperator(tp)
			return True
		else:
			return False
			
	def collectNumber(self) -> None:
		if not self.currentIsNumber():
			self.error("Number is expected!")
		else:
			self.currentNode().addValue(self.currentToken())
			self.currentIndex += 1
		
	def tryNumber(self) -> bool:
		if self.currentIsNumber():
			self.collectNumber()
			return True
		else:
			return False
			
	def makeHead(self) -> None:
		self.ancestors.append(Node("HEAD"))
	
	def climbDown(self, name:str) -> None:
		print("Climbing down into " + name)
		new_node = Node(name)
		self.currentNode().addChild(new_node)
		self.ancestors.append(new_node)
		
	def climbUp(self) -> None:
		self.ancestors.pop()
		print("climbingUp")
			
	def G(self):
		self.makeHead()
		self.P()
		
	def P(self):
		self.climbDown("P")
		self.T()
		while self.tryOperator("+"):
			self.T()
		self.climbUp()
		
	def T(self):
		self.climbDown("T")
		self.E()
		while self.tryOperator("*"):
			self.E()
		self.climbUp()
		
		
	def E(self):
		self.climbDown("E")
		if not self.tryNumber():
			self.collectOperator("(")
			self.P()
			self.collectOperator(")")
		self.climbUp()
		
			
builder = TreeBuilder(LexicalAnalyzer.tokenize("10 + 3"))
builder.G()

