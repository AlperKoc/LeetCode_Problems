import sys
class Solution:
    def maxSubArray(self, nums):
        
        sum = 0
        maxSum = float('-inf')
        
        if len(nums) == 0:
            return None
        else:
            sum = nums[0]
            maxSum = nums[0]
            
        for i in range(1,len(nums)):
            if nums[i] <= sum:
                sum = max(nums[i] + sum, nums[i])
            else:
                
                sum = max(nums[i] + sum, nums[i])
            maxSum = max(maxSum,sum)
            
        return maxSum
