class TreeNode(object):

    def __init__(self):
        self.chars = {}
        self.eof = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char in current.chars:
                current = current.chars[char]
            else:
                current.chars[char] = TreeNode()
                current = current.chars[char]
        current.eof = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.chars:
                current = current.chars[char]
            else:
                return False
        return current.eof

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char in current.chars:
                current = current.chars[char]
            else:
                return False
        return True
        