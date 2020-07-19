import LexicalAnalyzer

# Class "Node" consists of the name, list of children and the list of values
class Node:
        def __init__(self, name : str) -> None:
                self.name = name
                self.children = []
                self.values = []
                
        def addChild(self, child) -> None:
                self.children.append(child)
                

        def addValue(self, val) -> None:
                self.values.append(val)

class TreeBuilder:
        def hasMoreTokens(self) -> bool:
                """ Returns true if there are some tokens left """
                return self.currentIndex < len(self.currentString)

        def __init__(self, val) -> None:
                self.currentString = val
                self.currentIndex = 0
                self.ancestors = []

        def currentToken(self) -> int or str:
                """ Returns the current token """
                return self.currentString[self.currentIndex]	

        def currentNode(self) -> Node:
                """ Returns the current node """
                return self.ancestors[-1]

        def currentIsOperator(self, tp : str) -> bool:
                """ Returns true if this token is a valid operator """
                return self.hasMoreTokens() and self.currentToken() in LexicalAnalyzer.operators and self.currentToken() == tp

        def currentIsNumber(self):
                """ Returns true if this token is a number, false if not """
                return self.hasMoreTokens() and not self.currentToken() in LexicalAnalyzer.operators

        def error(self, message : str) -> None:
                """ Prints the given error message and aborts the program """
                print("Compilation failed!")
                print(message)
                exit(0)

        def collectOperator(self, tp) -> None:
                """ Collects the operator (if it is not an operator, sends an error message) into the tree """
                if not self.currentIsOperator(tp):
                        self.error("Expected operator " + tp)
                else:
                        self.currentNode().addValue(tp)
                        self.currentIndex += 1

        def tryOperator(self, tp : str) -> bool:
                """ Collects a token if it is an operator and returns true, otherwise returns false """
                if self.currentIsOperator(tp):
                        self.collectOperator(tp)
                        return True
                else:
                        return False

        def collectNumber(self) -> None:
                """ Collects the number (see collectOperator() method) """
                if not self.currentIsNumber():
                        self.error("Number is expected!")
                else:
                        self.currentNode().addValue(self.currentToken())
                        self.currentIndex += 1

        def tryNumber(self) -> bool:
                """ Collects the number token (see tryOperator() method) """
                if self.currentIsNumber():
                        self.collectNumber()
                        return True
                else:
                        return False

        def makeHead(self) -> None:
                """ Creates the head of the tree """
                self.ancestors.append(Node("HEAD"))
                
        def climbDown(self, name : str) -> None:
                """ Climbs down the tree - creates a new node """
                new_node = Node(name)
                old_node = self.currentNode()

                old_node.addChild(new_node)
                self.ancestors.append(new_node)
                
        def climbUp(self) -> None:
                """ Climbs up - deletes the ancestor """
                self.ancestors.pop()

        # Thease are the rules for the recursive descent. The grammar is given in the "readme.md"
        def G(self):
                self.makeHead()
                self.P()
                
        def P(self):
                self.climbDown("P")
                self.M()
                while self.tryOperator("+"):
                        self.M()
                self.climbUp()

        def M(self):
                self.climbDown("M")
                self.T()
                while self.tryOperator("-"):
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


