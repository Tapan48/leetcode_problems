class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        
            n=len(nums)
            target=sum(nums)-x
            if target<0:
                return -1
            
            
            l,r=0,0
            cursum=0
            res=float("inf")
            
            while r<n:
                
                cursum+=nums[r]
                
                while l<=r and cursum>target:
                    
                    cursum-=nums[l]
                    l+=1
                
                if cursum==target:
                    windowlen=r-l+1
                    minoper=n-windowlen
                    res=min(res,minoper)
                    r+=1
                    
                elif cursum<target:
                    r+=1
            return res if res!=float("inf") else -1      
                    
                
                
                
            
            
        