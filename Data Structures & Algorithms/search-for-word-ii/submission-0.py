class TrieNode(object):

    def __init__(self) -> None:
        self.chars = {}
        self.eos = False

    def addWord(self, word):

        current = self
        for char in word:
            if char not in current.chars:
                current.chars[char] = TrieNode()
            current = current.chars[char]
        current.eos = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, current_word):

            if (r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or board[r][c] not in node.chars
                ):
                return
            
            visited.add((r, c))
            node = node.chars[board[r][c]]
            current_word += board[r][c]
            if node.eos:
                result.add(current_word)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for cx, cy in directions:
                dfs(r + cx, c + cy, node, current_word)
            visited.remove((r, c))

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)

