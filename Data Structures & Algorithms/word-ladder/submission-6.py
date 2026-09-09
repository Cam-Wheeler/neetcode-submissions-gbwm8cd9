from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, res = set(wordList), 1
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in range(97, 123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
            res += 1
        return 0




                    



        