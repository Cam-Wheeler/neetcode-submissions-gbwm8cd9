from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for char1, char2 in zip_longest(word1, word2):
            if char1:
                res.append(char1)
            if char2:
                res.append(char2)
        
        return "".join(res)