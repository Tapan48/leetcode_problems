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
        
        """
        l,r=0,1
        maxprofit=0
        
        while r<len(prices):                          ## tc o(n)  sc o(1)
            
            
            if prices[l]>prices[r]:                      ## profit=sp -cp
                l=r                                      ##  for maxprofit , sp high
                r+=1                                            ## cp low
                 
            else:
                
                profit=prices[r]-prices[l]
                
                maxprofit=max(profit,maxprofit)
                r+=1
                
        return maxprofit       
           """
        
        
        
        
        
        res=[0]*len(prices)
        
        maxright=0
        for i in range(len(prices)-1,-1,-1):
            
            if prices[i]>maxright:
                maxright=max(maxright,prices[i])
                
                res[i]=prices[i]
                
            else:
                res[i]=maxright
                
        maxprofit=0        
        for i in range(len(prices)):
            
            
            profit=res[i]-prices[i]
            
            maxprofit=max(profit,maxprofit)
                
        return maxprofit        
                
                
                
            
        
                
        
        
                