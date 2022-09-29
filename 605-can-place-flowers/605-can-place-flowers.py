class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        """
        for i in range(0,len(flowerbed)):
            
            if len(flowerbed)==1:
                if flowerbed[i]==0:
                    n-=1
                    break
            
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                    
            elif i==(len(flowerbed)-1):
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    n-=1
                    
            else:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                    
        return n<=0            
          """
        
        
        arr=[0]+flowerbed+[0]
        
        for i in range(1,len(arr)-1):
            
            
            if arr[i-1]==0 and arr[i]==0 and arr[i+1]==0:
                arr[i]=1
                n-=1
                
        return n<=0        
        
        
        
        
        
        
        