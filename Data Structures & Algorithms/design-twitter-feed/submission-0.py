class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result, minHeap = list(), list()

        self.following[userId].add(userId)

        if len(self.following[userId]) >= 10:
            maxHeap = list()
            for followeeId in self.following[userId]:
                if followeeId in self.tweets and self.tweets[followeeId]:
                    index = len(self.tweets[followeeId]) - 1
                    time, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(maxHeap, [-time, tweetId, followeeId, index - 1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                time, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [time, tweetId, followeeId, index])
        else:
            for followeeId in self.following[userId]:
                if followeeId in self.tweets:
                    index = len(self.tweets[followeeId]) - 1
                    time, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])

        while minHeap and len(result) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
