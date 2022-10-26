class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
        arr=[]
        for i in range(len(temperatures)-1):
            
            for j in range(i+1,len(temperatures)):
                
                
                if temperatures[j]>temperatures[i]:
                    
                    arr.append(j-i)
                    break
                
                if j==(len(temperatures)-1):
                    arr.append(0)
        arr.append(0)            
                
        print(arr)        
        return arr
           """
        
        """
        i=0
        j=1
        
        arr=[]
        while i<(len(temperatures)-1):
            
            if j>=len(temperatures):
                arr.append(0)
                i+=1
                j=i+1
            
            if j<len(temperatures)and temperatures[j]>temperatures[i]:
                arr.append(j-i)
                i+=1
                j=i+1
            
            else:
                j+=1
        arr.append(0)
        
        return arr       
              """
        
        
        stack=[]
        res=[0]*len(temperatures)
        
        
        for i,temp in enumerate(temperatures):
            
            while stack and temp>stack[-1][0]:
                
                stacktemp,stackind=stack.pop()
                res[stackind]=i-stackind
            stack.append([temp,i])
            
        return res     
                
                
                
                
                
                
                
                
            
            
        
        
                     
                    
                    