class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        for row in matrix:
            
            if target<=row[len(row)-1]:
                
                l,r=0,len(row)-1
                
                while l<=r:
                    
                    mid=(l+r)//2
                    
                    if row[mid]==target:
                        return True
                    
                    elif target>row[mid]:
                        l=mid+1
                    
                    else:
                        r=mid-1
                        
        return False        
           """
        
        toprow,bottomrow=0,len(matrix)-1
        
        
        
        while toprow<=bottomrow:
            
            midrow=(toprow+bottomrow)//2
            
            if target>matrix[midrow][-1]:
                toprow=midrow+1
                
            elif target<matrix[midrow][0]:
                bottomrow=midrow-1
                
            else:
                break
        if not(toprow<=bottomrow):
            return False
                
         
        targetrow=matrix[midrow]
        l,r=0,len(targetrow)-1
        
       
        while l<=r:
            
            mid=(l+r)//2
                    
            if targetrow[mid]==target:
                return True
                    
            elif target>targetrow[mid]:
                l=mid+1
                    
            else:
                r=mid-1
                        
        return False        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        