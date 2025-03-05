import re

class Interpreter:
    def __init__(self, expression):
        # Remove spaces from the input expression
        self.expression = re.sub(r'\s+', '', expression)
        self.position = 0
        self.current_token = None

    def get_next_token(self):
        # Check if we've reached the end of the expression
        if self.position >= len(self.expression):
            return None
        
        current_char = self.expression[self.position]
        
        # If it's a number, extract the full number
        if current_char.isdigit():
            number = ''
            while self.position < len(self.expression) and self.expression[self.position].isdigit():
                number += self.expression[self.position]
                self.position += 1
            return ('NUMBER', int(number))
        
        # If it's an operator, return it
        if current_char in '+-':
            self.position += 1
            return ('OPERATOR', current_char)
        
        return None

    def evaluate_expression(self):
        # Get the first number
        self.current_token = self.get_next_token()
        
        if self.current_token and self.current_token[0] == 'NUMBER':
            result = self.current_token[1]
            self.current_token = self.get_next_token()
        else:
            raise ValueError("Invalid expression: Expected a number at the beginning")
        
        while self.current_token is not None:
            if self.current_token[0] == 'OPERATOR':
                operator = self.current_token[1]
                self.current_token = self.get_next_token()
                
                if self.current_token and self.current_token[0] == 'NUMBER':
                    if operator == '+':
                        result += self.current_token[1]
                    elif operator == '-':
                        result -= self.current_token[1]
                    
                    self.current_token = self.get_next_token()
                else:
                    raise ValueError("Invalid expression: Expected a number after the operator")
            else:
                raise ValueError("Invalid expression: Unexpected token encountered")
        
        return result

# Test cases
test_expressions = [
    "1 + 2 - 1",
    "10 - 5 - 2",
    "8 + 1 + 7",
    "6 - 5 + 1",
    "1 + 2 + 3 - 4 - 1"
]

for expression in test_expressions:
    interpreter = Interpreter(expression)
    print(f"{expression} = {interpreter.evaluate_expression()}")
