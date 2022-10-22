class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        row=1
        n=numRows
        arr=[]
        
        while row<=n:
            
            arr1=[]
            for i in range(0,row):
                
                if i==0 or i==(row-1):
                    arr1.append(1)
                    
                else:
                    summ=arr[row-2][i]+arr[row-2][i-1]
                    
                    arr1.append(summ)
            
            row+=1
            arr.append(arr1)
            
        return arr     
                    
            
            
            