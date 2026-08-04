from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for idx in range(len(s1)):
            s1_count[ord(s1[idx]) - ord("a")] += 1
            s2_count[ord(s2[idx]) - ord("a")] += 1

        matches = 0
        for idx in range(26):
            if s1_count[idx] == s2_count[idx]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add the letter to the right of the window
            char = s2[r]
            idx = ord(char) - ord("a")
            s2_count[idx] += 1
            if s2_count[idx] == s1_count[idx]:
                matches += 1
            elif s2_count[idx] == s1_count[idx] + 1:
                matches -= 1
            
            char = s2[l]
            idx = ord(char) - ord("a")
            s2_count[idx] -= 1
            if s2_count[idx] == s1_count[idx]:
                matches += 1
            elif s2_count[idx] == s1_count[idx] - 1:
                matches -= 1
            l += 1

        return matches == 26