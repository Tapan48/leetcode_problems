class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        """
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
                    
           """
        
        """
        n=numRows                                    ###   0 1 0      add consecutive elemts
                                                     ##    0 1 1 0    to get next row
        arr=[]                                        ##   0 1 2 1 0   
                                                      ##   0 1 3 3 1 0
        row=1                                        ##     1  4 6 4 1
        while row<=n:
            
            if row==1:
                arr.append([1])
            
            
            else:
                arr1=[]
                l=0
                array= [0]+arr[-1]+[0]
                
                j=row
                while j:
                    summ=array[l]+array[l+1]
                    arr1.append(summ)
                    j-=1
                    l+=1
                arr.append(arr1)
                
            row+=1
            
        return arr    
                """
        
        n=numRows
        arr=[]
        for row in range(1,n+1):
            
            if row==1:
                arr.append([1])
                
                
            else:
                arr1=[]
                l=0
                
                array=[0]+arr[-1]+[0]
                
                for j in range(row):
                    
                    summ=array[l]+array[l+1]
                    arr1.append(summ)
                    l+=1
                arr.append(arr1)    
        return arr           
                    
                    
                    
            
            
            
                    
                
                
                
                
            
            
        
            
            