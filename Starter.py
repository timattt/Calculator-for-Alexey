import Interpretator
import LexicalAnalyzer
import SyntaxAnalyzer

test = str(input())

builder = SyntaxAnalyzer.TreeBuilder(LexicalAnalyzer.tokenize(test))
builder.G()

top = builder.ancestors[0]

value = Interpretator.run(top)
print(value)
