class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        if "" in strs:
            return ""
        
        min_str = min(strs)
        output = ""
        for idx, char in enumerate(min_str):
            flag = True
            for substr in strs:
                if substr[idx] != char:
                    flag = False
            if flag:
                output += char
            if not flag:
                return output
        return output
