class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        if s == "":
            return res
        
        i = 0
        while i < len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            res.append(s[j+1:j+length+1])
            i = j + length + 1
        return res
