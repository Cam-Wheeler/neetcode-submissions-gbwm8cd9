from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = deque()
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped != brackets[bracket]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

