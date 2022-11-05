class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        
        nums = [eval(i) for i in nums]
        heapq.heapify(nums)
        
        while len(nums)!=k:
            
            heapq.heappop(nums)
            
        res=heapq.heappop(nums)
        
        return str(res)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        