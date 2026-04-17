class TrieNode(object):

    def __init__(self):
        self.eos = False
        self.chars = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for idx in range(len(word)):
            if word[idx] not in current.chars:
                current.chars[word[idx]] = TrieNode()
            if idx == len(word) - 1:
                current.eos = True
                return
            current = current.chars[word[idx]]
        return 

    def search(self, word: str) -> bool:
        current = self.root
        for idx in range(len(word)):
            if word[idx] not in current.chars:
                return False
            else:
                if idx == len(word) - 1 and current.eos == True:
                    return True
                elif idx == len(word) - 1 and current.eos == False:
                    return False
                else:
                    current = current.chars[word[idx]]
        return False # Not sure this is needed. 
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for idx in range(len(prefix)):
            if prefix[idx] in current.chars:
                current = current.chars[prefix[idx]]
            else:
                return False
        return True
        
        