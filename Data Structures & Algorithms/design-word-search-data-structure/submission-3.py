class TrieNode(object):

    def __init__(self) -> None:
        self.chars = {}
        self.eos = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.chars:
                curr = curr.chars[char]
            else:
                new_node = TrieNode()
                curr.chars[char] = new_node
                curr = curr.chars[char]
        curr.eos = True
        return None

    def search(self, word: str) -> bool:

        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, idx):

        if idx == len(word) and node.eos == True:
            return True

        if idx == len(word) and node.eos == False:
            return False
                    
        if word[idx] == ".":
            for char in node.chars:
                if self.dfs(node.chars[char], word, idx + 1):
                    return True
            return False
        elif word[idx] in node.chars:
            return self.dfs(node.chars[word[idx]], word, idx + 1)
    
        return False
                

        
