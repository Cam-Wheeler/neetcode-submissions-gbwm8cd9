class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            s = s
        
        head = 0
        tail = len(s) - 1

        while head <= tail:
            tmp = s[head]
            s[head] = s[tail]
            s[tail] = tmp
            head += 1
            tail -= 1
        