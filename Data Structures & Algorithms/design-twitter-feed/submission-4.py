from collections import defaultdict
from heapq import heappush_max, heappop_max

class Twitter:

    def __init__(self):
        self.tweet_heap = []
        self.tweet_time = 0
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        node = (self.tweet_time, tweetId, userId)
        self.tweet_time += 1
        heappush_max(self.tweet_heap, node)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        working_heap = self.tweet_heap.copy()
        feed = []
        while working_heap and len(feed) < 10:
            node = heappop_max(working_heap)
            if node[2] in self.users[userId] or node[2] == userId:
                feed.append(node[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
