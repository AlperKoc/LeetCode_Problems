class Solution:
    def twoSum(self, nums, target):
        
        numsOriginal = nums.copy()
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    i1 = numsOriginal.index(nums[i])
                    numsOriginal[i1] = numsOriginal[i1] + 1 # test case [3,3]
                    i2 = numsOriginal.index(nums[j])
                    return [i1,i2]
                elif nums[i] + nums[j] > target:
                    break
            
        
