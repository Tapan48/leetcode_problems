class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]                                 ## + -  main case
        for num in asteroids:                     ##  + + 
                                                   ## - -
                                               ## - +
                
            while stack and stack[-1]>0 and num<0:
                
                diff=stack[-1]+num
                
                if diff<0:
                    stack.pop()
                    
                elif diff>0:
                    num=0
                
                else:
                    stack.pop()
                    num=0
                    
            if num:
                stack.append(num)
                
        return stack    
                    
           
        
                
            
                
               
                            
                        
                        
                        
                        
                        
                        
                        
                        
            
                        
                        
                        
                    
                

                    
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        