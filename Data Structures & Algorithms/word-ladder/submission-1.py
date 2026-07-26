from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for other_word in wordList:
                diff = 0
                for idx in range(len(word)):
                    if word[idx] != other_word[idx]:
                        diff += 1
                if diff == 1:
                    adj[word].append(other_word)



        queue = deque()
        queue.append(beginWord)
        path = 1
        seen = set()
        seen.add(beginWord)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return path
                for neigh in adj[node]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append(neigh)
            path += 1
        return 0


