from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # letters in word: [word]
        res = []

        base = ord("a")
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - base] += 1
            groups[tuple(key)].append(word)

        for anagram_group in groups.values(): 
            res.append(anagram_group)

        return res