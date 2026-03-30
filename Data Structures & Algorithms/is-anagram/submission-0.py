class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lens are not the same, no match. 
        if len(s) != len(t):
            return False

        s_char_dict = {}
        for i in s:
            if i in s_char_dict.keys():
                s_char_dict[i] += 1
            else:
                s_char_dict[i] = 1
        
        t_char_dict = {}
        for i in t:
            if i in t_char_dict.keys():
                t_char_dict[i] += 1
            else:
                t_char_dict[i] = 1
        
        if s_char_dict == t_char_dict:
            return True
        else:
            return False