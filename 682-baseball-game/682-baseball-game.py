class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        
        for op in operations:
            
            if op=="C":
                
                stack.pop()
                
            elif op=="D":
                
                last=stack[-1]
                n=2*last
                stack.append(n)
                
            elif op=="+":
                n=stack[-1]+stack[-2]
                stack.append(n)
                
            else:
                stack.append(int(op))
                
        res=sum(stack)
        return res
            
            