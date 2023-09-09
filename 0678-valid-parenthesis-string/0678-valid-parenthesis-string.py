class Solution:
    def checkValidString(self, s: str) -> bool:

###  openmax and openmin variables used to solve this question


        
            dp = {}

            def dfs(i, num_open):
                if (i, num_open) in dp:
                    return dp[(i, num_open)]

                if num_open < 0:
                    dp[(i, num_open)] = False
                elif i == len(s):
                    dp[(i, num_open)] = num_open == 0
                elif s[i] == '(':
                    dp[(i, num_open)] = dfs(i + 1, num_open + 1)
                elif s[i] == ')':
                    dp[(i, num_open)] = dfs(i + 1, num_open - 1)
                elif s[i] == '*':
                    dp[(i, num_open)] = (
                        dfs(i + 1, num_open + 1) or
                        dfs(i + 1, num_open - 1) or
                        dfs(i + 1, num_open)
                    )

                return dp[(i, num_open)]

            return dfs(0, 0)

            

        
#         def dfs(i, num_open):   ### not working
            
#             if i == len(s) and num_open == 0:
#                 return True
#             if i == len(s) and num_open < 0:
#                 return False
#             elif  s[i] == "*":
#                 return dfs(i + 1, num_open + 1) or dfs(i + 1, num_open) or dfs(i + 1, num_open - 1)
#             elif  s[i] == "(":
#                 return dfs(i + 1, num_open + 1)
#             elif  s[i] == ")":
#                 return dfs(i + 1, num_open - 1)

#         return dfs(0, 0)






        








        




        


        




        