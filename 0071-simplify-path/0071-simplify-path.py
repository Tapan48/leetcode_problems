class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        
        
        
#         stac  mnvk=[]
#         string=""
        
#         for char in path:
            
            
            
            
                
#                 if stack and stack[-1]=="/" and char=="/":
                    
#                     continue
                    
#                 else:
#                     if char!=".":
                        
#                         string+=char            ## wrong solution
#                     stack.append(char)
                    
#         return string[0:len(string)-1]           
                     
            string=""
            stack=[]
            for char in path+"/":
                
                
                if char=="/":
                    if string=="..":
                        if stack: stack.pop()
                    
                        
                    
                    elif string!="" and string!=".":
                        stack.append(string)
                     
                    string=""
                else:
                    string+=char
                    
            return "/" + "/".join(stack)       
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                        
                    
                
                    
                    
              
                    
            
            
            
            
            
            
            
                
                
                
            
            
            
            
                
                
                
                
                
               
        
        

            
        
        
        
        
        
        
        
        
        
        
        
        