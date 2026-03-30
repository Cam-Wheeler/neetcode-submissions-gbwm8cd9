class Solution:

    def __init__(self):
        self.tracker = {}

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            self.tracker[i] = len(strs[i])
            encoded = encoded + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        slicing_str = s
        for idx, length in self.tracker.items():
            decoded.append(slicing_str[:length])
            slicing_str = slicing_str[length:]
        return decoded