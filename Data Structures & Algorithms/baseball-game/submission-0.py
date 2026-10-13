class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = deque()

        for element in operations:

            if element == "+":
                stack.append(stack[-2] + stack[-1])
            elif element == "D":
                stack.append(stack[-1] * 2)
            elif element == "C":
                stack.pop()
            else:
                stack.append(int(element))
        
        res = 0
        for element in stack:
            res += element

        return res