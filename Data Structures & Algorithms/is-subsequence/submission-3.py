class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_char = 0

        for t_char in t:
            if s_char == len(s):
                break
            if t_char == s[s_char]:
                s_char += 1
        
        if s_char == len(s):
            return True
        return False

