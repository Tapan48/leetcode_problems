class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictt={}
        for i,num in enumerate(nums):
            
            dictt[num]=dictt.get(num,0)+1
            
        
        sorteddictt=sorted(dictt.items(),key=lambda x:x[1],reverse=True)
        
        resdict=dict(sorteddictt)
        
        
        res=list(resdict.keys())[0:k]
        
        return res
        
        
        