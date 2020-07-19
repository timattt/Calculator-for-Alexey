import Interpretator
import LexicalAnalyzer
import SyntaxAnalyzer

def welcome_print() -> None:
    """ Just a beatiful welcome sign :) """
    print("=======================================")
    print("\tEasyCalculatorPy v.0.1")
    print("=======================================")

welcome_print()

#Input expression
print("Enter the statement to solve (avalible operations: '+', '-', '*', '/', round brackets): ")
test = str(input())

#Tokenize the string, build a tree
builder = SyntaxAnalyzer.TreeBuilder(LexicalAnalyzer.tokenize(test))
builder.G()

top = builder.ancestors[0]

#Find the value of the expression
value = Interpretator.run(top)
print("Result:", value)
