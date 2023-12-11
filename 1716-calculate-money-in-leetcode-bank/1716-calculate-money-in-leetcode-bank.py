class Solution:
    def totalMoney(self, n: int) -> int:
#         a = n // 7
#         nt = n % 7

#         ans1 = (nt * ((2 * (a + 1)) + (nt - 1))) // 2
#         ans2 = a * (2 * 28 + 7 * (a - 1)) // 2  

#         return ans1 + ans2  
          
          res=0
          day=1
          deposit=1
        
          while day<=n:
                
                
                res+=deposit
                deposit+=1
                
                
                if day%7==0:
                    
                    deposit=day//7+1
                day+=1    
          return res          
                
                
                
                
                
                
                
       