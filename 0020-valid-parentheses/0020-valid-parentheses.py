class Solution:
    def isValid(self, s: str) -> bool:
        
        
        
        hashmap={
            "(":")",
            "[":"]",
            "{":"}"
            
        }
        
        stack=[]
        for brac in s:
            
            if brac in hashmap:
                
                stack.append(brac)
                
            else:
                if stack and hashmap[stack[-1]]==brac:
                    stack.pop()
                else:
                    return False
        return True if not stack else False            