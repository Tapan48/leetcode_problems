class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        n=len(num)-1
        
        
        
        for r in range(n,-1,-1):
            
            singledig=int(num[r])
            if singledig%2:
                return num[:r+1]
        return ""    
            
            
            
        