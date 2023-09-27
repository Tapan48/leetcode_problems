class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
#         cntodd=0
        
#         for num in range(low,high+1):   ### tle
            
#             if num%2:
#                 cntodd+=1
                
#         return cntodd       

          rannge=high-low+1
    
          if rannge%2:
            
            res=(rannge//2 +1) if low%2 else rannge//2
            return res
            
          
        
          else:
                return rannge//2
        
        
        