class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        
        nums.sort()
        n=len(nums)-1
        ans=(nums[n]*nums[n-1])-(nums[1]*nums[0])
        return ans