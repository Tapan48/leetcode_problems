class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        
        heapq.heapify(nums)          ## tc of line  =  o(n)
        
        
        while len(nums)>k:           ##  tc o (n-k)log n
                                               
                                               ## total tc : o(nlogn)
            
            
            heapq.heappop(nums)              ## heappop takes log n
                                             ## keep popping from min heap until length of 
                                              nums == k and we get k largest elements
            
        res=nums[0]    
        return res
        """
        nums.sort()
        
        return nums[len(nums)-k]
     
        
       
        
        
        
        
        
        
        
        
        
        