class StockSpanner:

    def __init__(self):
        
        self.stack=[]
        

    def next(self, price: int) -> int:
        
        if not(self.stack):
            self.stack.append((price,1))
            return 1
        
        
        
        else:
            
            cnt=1
            
            if self.stack[-1][0]>price:
                
                self.stack.append((price,1))
                
                
                return 1
            
            else:
                
                while self.stack and self.stack[-1][0]<=price:
                    
                    prevprice,prevspan=self.stack.pop()
                    cnt+=prevspan
                    
                self.stack.append((price,cnt))  
                return cnt
                
                    
                    
    
            
            
            
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)




















