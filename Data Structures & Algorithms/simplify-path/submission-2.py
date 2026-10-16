class Solution:
    def simplifyPath(self, path: str) -> str:
        ptr = len(path) - 1
        result = []
        skip = 0
        rev_current_section = []
        while ptr >= 0:
            # We have hit a "/"
            if path[ptr] == "/" and rev_current_section:
                rev_current_section.reverse()
                current_section = "".join(rev_current_section)
                if current_section == ".":
                    rev_current_section = []
                    ptr -= 1
                    continue
                elif skip and current_section != "..":
                    skip -= 1
                elif current_section == "..":
                    skip += 1
                else:
                    result.append(current_section)
                rev_current_section = []
                ptr -= 1
            elif path[ptr] == "/" and not rev_current_section:
                ptr -= 1
            else:
                rev_current_section.append(path[ptr])
                ptr -= 1
        
        result.reverse()
        return "/" + "/".join(result)



