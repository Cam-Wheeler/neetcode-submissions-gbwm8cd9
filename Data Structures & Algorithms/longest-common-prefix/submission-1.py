class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_word = strs[0]

        for word in strs:
            if len(word) < len(shortest_word):
                shortest_word = word
        
        prefix = ""
        for idx in range(len(shortest_word)):
            char = shortest_word[idx]
            for word in strs:
                if word[idx] != char:
                    return prefix
            prefix += char

        return prefix
