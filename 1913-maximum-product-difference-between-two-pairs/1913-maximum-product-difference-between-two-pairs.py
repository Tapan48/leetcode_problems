class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        
#         nums.sort()
#         n=len(nums)-1
#         ans=(nums[n]*nums[n-1])-(nums[1]*nums[0])
#         return ans

          
            heapq.heapify(nums)

            s1=heapq.heappop(nums)
            s2=heapq.heappop(nums)
            
            
            negated_nums = [-num for num in nums]


            heapq.heapify(negated_nums)
            
            l2=abs(heapq.heappop(negated_nums))
            l1=abs(heapq.heappop(negated_nums))    
            
            ans=(l2*l1)-(s1*s2)
            return ans