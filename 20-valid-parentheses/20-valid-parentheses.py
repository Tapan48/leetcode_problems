class Solution:
    def isValid(self, s: str) -> bool:
        
        dictt={"(":")", "{":"}","[":"]"}
        
        stack=[]
        for brac in s:
            
            if brac in dictt:      ## open brackets added in stack if bracket
                                       ## found is open
                stack.append(brac)
                
            
            else:                      ##  check if last open bracket in stack==
                                           ## closed bracket found in string
                
                if stack and brac==dictt[stack[-1]]:
                    stack.pop()
                    
                else:
                    return False
        return True if not stack else False      
                
                
                
                
          
                
                
                
                
              
       
    
        