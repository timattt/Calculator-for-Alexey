import Interpretator
import LexicalAnalyzer
import SyntaxAnalyzer

print("Input statement to solve (use only +, *, (, ) and digits, other is comming soon) :)")
test = str(input())

builder = SyntaxAnalyzer.TreeBuilder(LexicalAnalyzer.tokenize(test))
builder.G()

top = builder.ancestors[0]

value = Interpretator.run(top)
print(value)
