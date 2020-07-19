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
        if head.name == "M":
                if head.values:
                        result = run(head.children[0])
                        for i in range(1, len(head.children)):
                                result -= run(head.children[i])
                else:
                        result = run(head.children[0])
                        
        if head.name == "T":
                result = 1
                for child in head.children:
                        result *= run(child)
        if head.name == "K":
                if head.values:
                        result = run(head.children[0])
                        for i in range(1, len(head.children)):
                                result /= run(head.children[i])
                else:
                        result = run(head.children[0])
        if head.name == "E":
                if len(head.values) == 1:
                        result = head.values[0]
                else:
                        result = run(head.children[0])
        # Debug print
        #print("Name:", head.name, "\tValue:", head.values, "\tResult:", result)
        return result
