import LexicalAnalyzer
import SyntaxAnalyzer

def run(head) -> int:
        """ A recursive function that solves the equation """
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
                if len(head.values) == 1:
                        result = head.values[0]
                else:
                        result = run(head.children[0])

        return result
