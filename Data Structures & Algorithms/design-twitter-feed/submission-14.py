import heapq

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_n = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_n, tweetId))
        self.tweet_n += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.follows[userId]
        followers.add(userId) # include themselves for their feed, idempotent add.

        feed_heap = [] # tweet_n, idx of tweet, user_id, tweet_id
        for user in followers:
            tweets = self.tweets[user]
            if tweets:
                most_recent = tweets[-1]
                heapq.heappush_max(feed_heap, (most_recent[0], len(tweets) - 1, user, most_recent[1]))

        feed = []
        while feed_heap: # while there are tweets to give.
            tweet_n, idx_of_tweet, user_id, tweet_id = heapq.heappop_max(feed_heap) # take from the top of the heap (most recent tweet)
            feed.append(tweet_id)
            if idx_of_tweet > 0: # if there are more tweets from this user to add.
                next_tweet_idx = idx_of_tweet - 1
                next_user_tweet = self.tweets[user_id][next_tweet_idx]
                new_node = (next_user_tweet[0], next_tweet_idx, user_id, next_user_tweet[1])
                heapq.heappush_max(feed_heap, new_node) # add the next tweet to the heap.
            if len(feed) == 10: # we have enough tweets
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: # users cannot follow themselves
            return
        self.follows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: # check they are following them in the first place.
            self.follows[followerId].remove(followeeId)
