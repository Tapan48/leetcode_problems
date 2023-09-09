class Solution:
    def checkValidString(self, s: str) -> bool:

###  netopenmax and netopenmin variables used to solve this question


            netopenmin,netopenmax=0,0


            for i in range(len(s)):
            
                if s[i]=="(":
                    netopenmin,netopenmax=netopenmin+1,netopenmax+1
                    
                elif s[i]==")": 
                    netopenmin,netopenmax=netopenmin-1,netopenmax-1
                    
                else:
                    netopenmin,netopenmax=netopenmin-1,netopenmax+1
                    
                if netopenmax<0:
                    return False
                
                elif netopenmin<0:
                    netopenmin=0
                    
            return netopenmin==0       
                    
        
        
        




#             dp={}
#             def dfs(i,netopen):        ### tc without memoization o(3^n)  sc o(n^2)
#                                        ### tc with memoization   o(n^3)  sc  o(n^2)
        
#                 if i==len(s):
#                    return netopen==0
                
#                 if (i,netopen)in dp:
#                     return dp[(i,netopen)]
                
#                 if netopen<0:
#                     return False
        
                    
#                 if s[i]=="(":
                    
                    
#                      dp[(i,netopen)]= dfs(i+1,netopen+1)
                    
#                 elif s[i]==")":
#                         dp[(i,netopen)]= dfs(i+1,netopen-1)
#                 elif s[i]=="*":
#                     dp[(i,netopen)]= dfs(i+1,netopen+1)or dfs(i+1,netopen-1)or dfs(i+1,netopen)
                    
#                 return dp[(i,netopen)]    
#             return   dfs(0,0)  
                 
                
                
                
                
                    
                    


        
#             dp = {}

#             def dfs(i, num_open):
#                 if (i, num_open) in dp:
#                     return dp[(i, num_open)]

#                 if num_open < 0:
#                     dp[(i, num_open)] = False
#                 elif i == len(s):
#                     dp[(i, num_open)] = num_open == 0
#                 elif s[i] == '(':
#                     dp[(i, num_open)] = dfs(i + 1, num_open + 1)
#                 elif s[i] == ')':
#                     dp[(i, num_open)] = dfs(i + 1, num_open - 1)
#                 elif s[i] == '*':
#                     dp[(i, num_open)] = (
#                         dfs(i + 1, num_open + 1) or
#                         dfs(i + 1, num_open - 1) or
#                         dfs(i + 1, num_open)
#                     )

#                 return dp[(i, num_open)]

#             return dfs(0, 0)

               
                    
                    
                   
                   
                    
               
               

            

        
    






        








        




        


        




        