class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        
        dummyarr=sorted(score)
        dummyarr.reverse()
        dictt={}
        
        
        cnt=1
        for num in dummyarr:
            
            if cnt==1:
                dictt[num]="Gold Medal"
                
            elif cnt==2:
                dictt[num]="Silver Medal"
                
            elif cnt==3:
                dictt[num]="Bronze Medal"
                
                
            else:
                dictt[num]=str(cnt)
                
            cnt+=1    
        for i,num in enumerate(score):
            
            dummyarr[i]=dictt[num]
        return dummyarr     
            
        
        
        