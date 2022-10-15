class Solution:
    def hammingWeight(self, n: int) -> int:
        
        cnt=0
        
        
        while n:                    ## used right shift operator
                                     ## 1101>>1  (means right shift every bit by 1 step )
                                     ## 0110>>1
                                     ## 0011>>1
                                     ## 0001>>1 
                                     ## 0000     
            
            cnt+=n%2                ## if last digit is 1 then n%2 =1 
                                    ## if last digit is 0 then n%2=0
            
            n=n>>1
            
        return cnt     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        