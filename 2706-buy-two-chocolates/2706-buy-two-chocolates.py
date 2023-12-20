class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        
        
            min1=min2=float("inf")

            for price in prices:
                
                
                if price<min1:
                    min2=min1
                    min1=price
                    
                elif price<min2:
                    min2=price

#                 if price<min2:

#                     if price<min1:
#                         min2=min1
#                         min1=price
#                     else:
#                         min2=price
            cost=min1+min2
            left=money-cost
            return left if left>=0 else money
        
        
        
#         prices.sort()
        
#         cost=prices[0]+prices[1]
        
#         if (money-cost)>=0:
#             return money-cost
#         else:
#             return money

          