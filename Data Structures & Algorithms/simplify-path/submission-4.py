class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        skip = 0
        clean = []
        for idx in range(len(split_path) - 1, 0, -1):

            if split_path[idx] == "" or split_path[idx] == ".":
                continue
            elif split_path[idx] == "..":
                skip += 1
            else:

                if not skip:
                    clean.append(split_path[idx])
                else:
                    skip -= 1
        
        clean.reverse()
        return "/" + "/".join(clean)



