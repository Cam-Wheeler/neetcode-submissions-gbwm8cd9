class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0:
            return False

        if len(s) == 0:
            return True
    

        head, tail = 0, 0
        while tail < len(t):

            if s[head] == t[tail]:
                head += 1
                tail += 1
                if head == len(s):
                    return True
            else:
                tail += 1
            

        return False

