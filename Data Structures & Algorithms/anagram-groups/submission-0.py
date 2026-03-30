from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        base = ord("a")

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - base] += 1
            anagrams[tuple(key)].append(word)

        output = []
        for word_list in anagrams.values():
            output.append(word_list)
        return output

        