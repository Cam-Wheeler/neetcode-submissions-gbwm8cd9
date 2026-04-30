from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.tweets = defaultdict(list)
        self.tweet_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.users[userId].copy()
        follows.append(userId)
        heap = []
        for user in follows:
            for tweet in self.tweets[user]:
                heapq.heappush_max(heap, tweet)
        
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop_max(heap)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users[followerId] and followerId != followeeId:
            self.users[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


