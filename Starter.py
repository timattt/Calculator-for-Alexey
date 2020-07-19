import Interpretator
import LexicalAnalyzer
import SyntaxAnalyzer

print("===================================")
print("\tPyCalculator v.0.1")
print("===================================")

print("Enter the statement to solve (avalible operations: '+', '-', '*', '/', round brackets): ")
test = str(input())

builder = SyntaxAnalyzer.TreeBuilder(LexicalAnalyzer.tokenize(test))
builder.G()

top = builder.ancestors[0]

value = Interpretator.run(top)
print(value)
