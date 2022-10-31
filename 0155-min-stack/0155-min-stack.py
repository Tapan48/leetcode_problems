class MinStack:

    def __init__(self):
        
        self.stack=[]
        self.minstack=[]
        
        
        
    def push(self, val: int) -> None:
        """
        if not(self.stack):           ## if stack empty,push element
            
            self.minstack.append(val)      
            self.stack.append(val)           
            
        else:                        
            
                                
        
            minval=min(val,self.minstack[-1])
            self.minstack.append(minval)
            self.stack.append(val)
        """
        self.stack.append(val)
        
        minval=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)
        

    def pop(self) -> None:
        
        
        
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.minstack[-1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()