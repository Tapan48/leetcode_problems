
from collections import deque


class MyStack:

    def __init__(self):
        q=[]
        self.queue=q
        

    def push(self, x: int) -> None:
        
        
        
        self.queue.append(x)
        
        
        

    def pop(self) -> int:
        
        
        val=self.queue.pop()
        return val
    
    def top(self) -> int:
        
        val=self.queue[-1]
        return val

    def empty(self) -> bool:
        
        if len(self.queue)==0:
            
            return True
        
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()