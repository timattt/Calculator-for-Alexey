# Lists for all avalible operators and the list of delimiters
operators = ['(', ')', '*', '/', '+', '-']
delimiters = [' ', '\t', '\n']

def tokenize(text:str) -> list:
        """ This method tokenizes string into operators (as chars) and numbers (as ints) """

        # To ensure that the last number will be taken 
        text += delimiters[0]

        # The result list with tokens and a temporary variable for numbers
        result = []
        raw_number = ""

        for val in text:
                # Conditions for tokens
                isOperator = val in operators
                isDelimiter = val in delimiters
                isNumber = val.isdigit()

                # Push the number and flushes it (if we've reached the last digit of this number)
                if (isOperator or isDelimiter) and len(raw_number) > 0:
                        result.append(int(raw_number))
                        raw_number = ""	
                
                # Operator case
                if isOperator:
                        result.append(val)
                
                # Number case
                if isNumber:
                        raw_number += val

        return result
