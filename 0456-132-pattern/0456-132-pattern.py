class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        
        stack=[]          ###  (nums[i],minleft)
        minimum=nums[0]
        
        for k in range(len(nums)):
            
            if k==0 or k==1:
                
                stack.append((nums[k],minimum))
                minimum=min(minimum,nums[k])
            else:
                
                while stack and stack[-1][0]<= nums[k]:
                    
                    stack.pop()
                   
                    
                if stack and stack[-1][1]<nums[k] :
                    
                        return True
                else:
                    stack.append((nums[k],minimum))
                    minimum=min(minimum,nums[k])
        return False           
                
                
        