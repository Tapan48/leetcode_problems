​
​
stack=[]
i=0
​
​
for n in pushed:              ### tc o(n)
​
stack.append(n)
​
while stack and stack[-1]==popped[i]:
​
stack.pop()
i+=1
return not stack
​