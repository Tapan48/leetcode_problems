class Solution:
    def isValid(self, s: str) -> bool:
        
        dictt={")":"(", "}":"{","]":"["}
        
        stack=[]
        for brac in s:
            
            if brac not in dictt:      ## open brackets added in stack if bracket
                                       ## found is open
                stack.append(brac)
                
            
            else:                      ##  check if last open bracket in stack==
                                           ## closed bracket found in string
                
                if stack and stack[-1]==dictt[brac]:
                    stack.pop()
                    
                else:
                    return False
        return True if not stack else False      
                
                
                
                
          
                
                
                
                
              
       
    
        