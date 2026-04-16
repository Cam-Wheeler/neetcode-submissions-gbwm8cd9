from collections import defaultdict
from heapq import heappush_max, heappop_max

class Twitter:
    def __init__(self):
        self.tweet_time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []
        
        relevant_users = self.follows[userId]
        relevant_users.add(userId)
        for user in relevant_users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                tweet_time, tweet_id = self.tweets[user][index]
                heappush_max(max_heap, (tweet_time, tweet_id, user, index - 1))

        while max_heap and len(result) < 10:
            tweet_time, tweet_id, user, index = heappop_max(max_heap)
            result.append(tweet_id)
            if index >= 0:
                next_time, next_tweet_id = self.tweets[user][index]
                heappush_max(max_heap, (next_time, next_tweet_id, user, index - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)