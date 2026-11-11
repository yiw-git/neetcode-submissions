from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time=0
        self.post=defaultdict(list)
        self.follower=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append((self.time, tweetId))
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed=self.post[userId][:]
        #feed: [(tim1, postaaa),(time3, postbbb)]
        for followee in self.follower[userId]:#find all fans of me
            feed.extend(self.post[followee])
            #feed:[(tim1, postaaa),(time3, postbbb), (time6,post111), (time8,postabc)] last two post comes from fans 
        feed.sort(key=lambda x:-x[0])
        return [tweetId for _, tweetId in feed[:10]]
        #final return is a list of tweetId
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
