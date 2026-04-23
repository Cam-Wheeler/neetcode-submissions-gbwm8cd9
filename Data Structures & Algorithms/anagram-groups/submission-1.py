from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                idx = ord("a") - ord(char)
                key[idx] += 1
            groups[tuple(key)].append(word)
        
        return [group for group in groups.values()]
            