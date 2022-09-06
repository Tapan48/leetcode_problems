class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        
        
        rescnt=0
        for i in range(len(arr1)):
            cnt=0
            for j in range(len(arr2)):
                
                if abs(arr1[i]-arr2[j])>d:
                    
                    cnt+=1
                    
            if cnt==len(arr2):
                rescnt+=1
                
                    
        
                    
        return rescnt            
                    
            
        
        
        
        
        
        
        
        
        
        

        
        
        