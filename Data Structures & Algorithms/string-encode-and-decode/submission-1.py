class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""

        encoded = ""
        for sub_string in strs:
            str_len = len(sub_string)
            string_w_len = f"{str_len}#{sub_string}"
            encoded += string_w_len
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        output = []
        i = 0
        decode_len = ""

        while i < len(s):
            # Stack the ints into a string to get the total length.
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                decode_len += s[i]

            # We have hit the end of the len prefix. We need to decode.
            elif s[i] == "#":
                str_len = int(decode_len)
                single_str = s[i+1: i+1+str_len]
                output.append(single_str)
                # Cleanup
                decode_len = ""
                i = i + str_len  # skip past the decoded string

            i += 1

        return output