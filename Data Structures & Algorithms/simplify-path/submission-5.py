class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")
        stack = []
        for idx in range(1, len(split_path)):

            if split_path[idx] == "" or split_path[idx] == ".":
                continue

            elif split_path[idx] == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(split_path[idx])

        return "/" + "/".join(stack)
            


            



