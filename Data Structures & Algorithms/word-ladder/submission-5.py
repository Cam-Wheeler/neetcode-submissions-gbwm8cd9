from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # If its not present, its 100% not possible
        if endWord not in wordList:
            return 0

        # If its present, its either possible or not (depending on wordlist)
        adj = defaultdict(list)
        n = len(beginWord)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                diff = 0
                for idx in range(n):
                    if wordList[i][idx] != wordList[j][idx]:
                        diff += 1
                if diff == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        iterations = 1

        while q:
            
            for _ in range(len(q)):
                node = q.popleft()

                # We have found endword.
                if node == endWord:
                    return iterations

                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            iterations += 1
        
        # We tried but could not make it to endword.
        return 0




                    



        