class Twitter:

    def __init__(self):
        self.followmap=defaultdict(set)    #### userid (followers)---> followed(id)
        self.tweetmap=defaultdict(list)      ### userid---> list([count,tweetid])
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        
        minheap=[]
        res=[]
        self.followmap[userId].add(userId)
        for followed in self.followmap[userId]:
            
            if followed in self.tweetmap:
                index=len(self.tweetmap[followed])-1
                count,tweetid=self.tweetmap[followed][index]
                heapq.heappush(minheap,[count,tweetid,index-1,followed])
                
        while minheap and len(res)<10:
            
            count,tweetid,index,followed=heapq.heappop(minheap)
            res.append(tweetid)
            
            if index>=0:
                    count,tweetid=self.tweetmap[followed][index]
                    heapq.heappush(minheap,[count,tweetid,index-1,followed])
        return res            
                    
                    
                
                
                
                
                
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.followmap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)