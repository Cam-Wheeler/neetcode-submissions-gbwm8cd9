from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # If its not present, its 100% not possible
        if endWord not in wordList:
            return 0

        # If its present, its either possible or not (depending on wordlist)
        adj = defaultdict(set)
        n = len(beginWord)
        wordList.append(beginWord)
        for word in wordList:
            for other_word in wordList:
                if word == other_word:
                    continue
                diff = 0
                for idx in range(n):
                    if word[idx] != other_word[idx]:
                        diff += 1
                if diff <= 1:
                    adj[word].add(other_word)
                    adj[other_word].add(word)
        
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




                    



        