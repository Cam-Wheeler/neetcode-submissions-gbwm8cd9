class TrieNode:
    def __init__(self):
        self.eos = False
        self.chars = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.chars:
                current.chars[char] = TrieNode()
            current = current.chars[char]
        
        # Mark the actual last character's node as the end
        current.eos = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, node) -> bool:
            # Base Case: We've matched all characters. 
            # Is this node marked as an end of a word?
            if idx == len(word):
                return node.eos
            
            char = word[idx]
            
            if char == ".":
                # Wildcard: Try every possible path from this node
                for child_node in node.chars.values():
                    if dfs(idx + 1, child_node):
                        return True
                return False
                
            else:
                # Normal character: Move to the child if it exists
                if char not in node.chars:
                    return False
                return dfs(idx + 1, node.chars[char])

        return dfs(0, self.root)