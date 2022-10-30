class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        
        self.arr=nums
        self.size=k
        heapq.heapify(self.arr)
        
        while len(self.arr)>k:
            heapq.heappop(self.arr)
        
        
    def add(self, val: int) -> int:
        
        heapq.heappush(self.arr,val)
        
        while len(self.arr)>self.size:
            heapq.heappop(self.arr)
        
        return self.arr[0]
        
        
        """
        self.arr.append(val)
        
        self.arr.sort()
        
        n=len(self.arr)-self.size
        res=self.arr[n]
        
        return res
        """


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)