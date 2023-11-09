cursum,l=0,0
res=0
for r in range(len(arr)):
cursum+=arr[r]
if (r-l+1)>k:
cursum-=arr[l]
l+=1
if (r-l+1)==k and (cursum/(r-l+1))>=threshold:
res+=1
return res