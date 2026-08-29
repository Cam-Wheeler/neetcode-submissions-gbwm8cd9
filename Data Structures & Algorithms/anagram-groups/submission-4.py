from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1
            groups[tuple(key)].append(word)

        res = []
        for key, group in groups.items():
            res.append(group)

        return res