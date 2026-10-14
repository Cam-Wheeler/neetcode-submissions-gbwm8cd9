class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: len(t) > len(s)
        if len(t) > len(s):
            return ""

        want = Counter(t) # dict of counts
        have = defaultdict(int)
        current_shortest = float("inf")
        result = None
        l = 0

        def count_matches():
            matches = 0
            for char, count in want.items():
                if have[char] >= count:
                    matches += 1
            return matches

        for r in range(len(s)):
            have[s[r]] += 1
            matches = count_matches()
            # If we have a substring that contains everything we want
            # We will now shrink
            while matches == len(want):
                if (r - l) + 1 < current_shortest:
                    current_shortest = (r - l) + 1
                    result = (l, r)
                have[s[l]] -= 1
                l += 1
                matches = count_matches()

        return "" if result == None else s[result[0]:result[1] + 1]

            
                




