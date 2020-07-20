import Interpretator
import LexicalAnalyzer
import SyntaxAnalyzer

def welcome_print() -> None:
    """ Just a beatiful welcome sign :) """
    print("=======================================")
    print("\tEasyCalculatorPy v.0.2")
    print("=======================================")

welcome_print()

#Input expression
print("Enter the statement to solve (avalible operations: '+', '-', '*', '/', round brackets): ")
input_expression = str(input())

#Debug print
#print(LexicalAnalyzer.tokenize(test))

#Debug print
#print(LexicalAnalyzer.tokenize(test))

#Tokenize the string, build a tree
builder = SyntaxAnalyzer.TreeBuilder(LexicalAnalyzer.tokenize(input_expression))
builder.G()

top = builder.ancestors[0]

#Find the value of the expression
value = Interpretator.run(top)
print("Result:", value)
