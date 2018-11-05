class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif i>0 and nums[i-1]< target and nums[i] > target:
                return i
            elif i<len(nums)-1 and nums[i+1]> target and nums[i] < target:
                return i+1
            elif nums[-1] < target:
                return len(nums)
            elif nums[0] > target:
                return 0

            
        
