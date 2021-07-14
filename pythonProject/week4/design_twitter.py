class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 把每个人关注的人 建一个哈希表
        self.HashMap = {}
        # 把每个人发过的推 建一个哈希表
        self.posted = {}
        # 用一个self.t维护时间 每次有人发推特后 self.t - 1
        # python 最小堆 时间越新 self。t 越小 在堆顶
        self.t = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # 维护发推的哈希表
        if userId in self.posted:
            self.posted[userId].append([self.t,tweetId])
        else:
            self.posted[userId] = [[self.t,tweetId]]
        self.t -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # 先建最小堆 分别把这个人的推 和这个人关注的人的推特 放到堆里
        # 取前10个 或者不到10个的推
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        all = []
        if userId in self.posted:
            all += self.posted[userId][:]

        if userId in self.HashMap:
            for id in self.HashMap[userId]:
                if id in self.posted:
                    all += self.posted[id][:]
        heapq.heapify(all)
        i = 0
        ans = []

        while all and i <= 9:
            ans.append(heapq.heappop(all)[1])
            i += 1
        return ans



    def follow(self, followerId: int, followeeId: int) -> None:
        # 维护关注的人哈希表
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.HashMap:
            if followeeId not in self.HashMap[followerId]:
                self.HashMap[followerId].append(followeeId)
        else:
            self.HashMap[followerId] = [followeeId]


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.HashMap:
            self.HashMap[followerId].remove(followeeId)