class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        
        """
        l,r=len(nums)-2,len(nums)-1
        
        
        i=l        
        
        while l>=0:                ## r index denotes the goalpost
                                      ## we have to check if from l index we can reach r                                          ## index
            
            if i+nums[l]>=r:
                
                r=l
                l-=1
                i=l
            else:
                
                l-=1
                i=l
                
        if r==0:
            return True
        
        else:
                return False
                
            """
        goal=len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            
            if i+nums[i]>=goal:
                
                goal=i
                
                
        return (goal==0)    