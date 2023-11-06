​
​
think and solve again
​
​
​
dp={1:1}
​
​
​
​
def dfs(num):                   ####  solved in notebook
​
if num==1:
return 1
​
if num in dp:
return dp[num]
​
dp[num]=0 if num==n else num
​
​
for i in range(1,num):
​
val=dfs(i)*dfs(num-i)
​
dp[num]=max(dp[num],val)
​
return dp[num]
​
return dfs(n)
​
​
​
​
​