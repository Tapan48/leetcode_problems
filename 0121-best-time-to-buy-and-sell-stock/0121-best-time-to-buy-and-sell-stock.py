class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        """  
        maxprofit=float("-inf")
        for i in range(0,len(prices)-1):
            for j in range(i,len(prices)):
                
                
                profit=prices[j]-prices[i]
                
                maxprofit=max(maxprofit,profit)
                
        if maxprofit<=0:
            return 0
        
        else:
            return maxprofit
                """
        
        
        l,r=0,1
        maxprofit=0
        
        while r<len(prices):
            
            
            if prices[l]>prices[r]:
                l=r
                r+=1
                
            else:
                
                profit=prices[r]-prices[l]
                
                maxprofit=max(profit,maxprofit)
                r+=1
                
        return maxprofit       
                
                
        
        
                