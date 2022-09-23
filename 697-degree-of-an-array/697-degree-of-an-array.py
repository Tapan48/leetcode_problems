class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        
        freq={}
        firstseen={}
        
        degree=0
        minlen=0
        for i,ele in enumerate(nums):
            
            if ele not in firstseen:
                firstseen[ele]=i
                
            freq[ele]=freq.get(ele,0)+1
            
            if freq[ele]>degree:
                degree=freq[ele]
                minlen=i-firstseen[ele]+1
                
            elif freq[ele]==degree:
                
                minlen=min(minlen,i-firstseen[ele]+1)
                
                
        return minlen        
                
                
                
                
                
                
        
        
        
        
        