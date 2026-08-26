class TrieNode(object):

    def __init__(self) -> None:
        self.chars = {}
        self.eos = False

class Trie(object):

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char in curr.chars:
                curr = curr.chars[char]
            else:
                new_node = TrieNode()
                curr.chars[char] = new_node
                curr = new_node
        curr.eos = True
        return None
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.chars:
                return False
            else:
                curr = curr.chars[char]
        return curr.eos

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Setup the trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Setup the dfs
        res = set()
        path = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, current_word):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or board[r][c] not in node.chars):
                return
            path.add((r, c))
            node = node.chars[board[r][c]]
            current_word = current_word + board[r][c]
            if node.eos:
                res.add(current_word)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, node, current_word)
            path.remove((r, c))
            return

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie.root, "")
        return list(res)