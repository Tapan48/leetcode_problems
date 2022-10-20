class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
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
                        