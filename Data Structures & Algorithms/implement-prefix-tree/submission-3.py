class TrieNode(object):

    def __init__(self) -> None:
        self.chars = {}
        self.eos = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for idx in range(len(word)):
            if word[idx] in curr.chars:
                curr = curr.chars[word[idx]]
            else:
                new_node = TrieNode()
                curr.chars[word[idx]] = new_node
                curr = new_node
        
        curr.eos = True

        return None

    def search(self, word: str) -> bool:
        curr = self.root
        for idx in range(len(word)):
            if word[idx] not in curr.chars:
                return False
            else:
                curr = curr.chars[word[idx]]

        return True if curr.eos else False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for idx in range(len(prefix)):
            if prefix[idx] in curr.chars:
                curr = curr.chars[prefix[idx]]
            else:
                return False
        return True
        
        