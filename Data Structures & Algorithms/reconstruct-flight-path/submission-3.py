from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        for src, dest in tickets:
            adj[src].append(dest)
        
        for _, dests in adj.items():
            dests.sort()

        res = ["JFK"]

        def dfs(node, moves):

            if moves == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            tmp = list(adj[node])
            for idx, dest in enumerate(tmp):
                adj[node].pop(idx)
                res.append(dest)
                if dfs(dest, moves + 1):
                    return True
                adj[node].insert(idx, dest)
                res.pop()

            return False
            
        dfs("JFK", 1)
        
        return res




