import LexicalAnalyzer

class Node:
	
	def __init__(self, name:str) -> None:
		self.name = name
		self.children = []
		self.values = []
		
		
	def addChild(self, child) -> None:
		self.children.append(child)
		
	
	def addValue(self, val) -> None:
		self.values.append(val)

class TreeBuilder:
	"""
	Example for: 10 + 2 * (5 + 6)
	There will be this tree:
	HEAD
|
P{+}
|\
| \
|  \
|   \
T    \
|     \
|      \
E{10}	\
	 \	
	  \	
	   \
	   T{*}
	  /\
	 /  \	
	/    \
       /     \
      E{2}    \ 
	       \
		E{(, )}
		|
		|
		|
		P{+}
		/\     
	       / \
	      /   \
	     /     \
	    /       \
	   /         \
	   T	     T
	   |         | 
	   |         |
	   |         |
	   E{5}      E{6}	    
	"""
	def hasMoreTokens(self) -> bool:
		return self.currentIndex < len(self.currentString)
	
	def __init__(self, val) -> None:
		self.currentString = val
		self.currentIndex = 0
		self.ancestors = []
		
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
		new_node = Node(name)
		old_node = self.currentNode()
		
		old_node.addChild(new_node)
		self.ancestors.append(new_node)
		
		
	def climbUp(self) -> None:
		self.ancestors.pop()
			
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


