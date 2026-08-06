import operator
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("*", "+", "-", "/")
        stack = deque()

        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                match token:
                    case "+":
                        res = a + b
                    case "-":
                        res = a - b
                    case "*":
                        res = a * b
                    case "/":
                        res = int(a /b)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack.pop()