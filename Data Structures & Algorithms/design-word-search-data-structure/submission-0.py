class TrieNode(object):
    def __init__(self):
        self.eos = False
        self.chars = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        prev = None
        current = self.root
        for char in word:
            if char not in current.chars:
                current.chars[char] = TrieNode()
            prev = current
            current = current.chars[char]
        prev.eos = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, node) -> bool:
            if idx == len(word):
                return False
                
            if idx == len(word) - 1 and (word[idx] in node.chars or word[idx] == ".") and node.eos:
                return True

            if word[idx] != "." and word[idx] not in node.chars:
                return False

            if word[idx] == ".":
                for char in node.chars:
                    if dfs(idx + 1, node.chars[char]):
                        return True
                return False

            return dfs(idx + 1, node.chars[word[idx]])

        return dfs(0, self.root)
            





