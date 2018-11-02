class Solution:
    def jump(self, nums):
        memo = [len(nums)] * len(nums)
        print(len(nums))
        memo[0] = 0
        solutionFound = False
        
        for i in range(len(nums)):
            if i >= 1 and nums[i] + 1 == nums[i-1]:
                continue
            for j in range(1,nums[i]+1):
                if i+j >= len(nums):
                    break
                else:
                    if memo[i+j] > (memo[i]+1):
                        memo[i+j] = memo[i]+1
                        if i+j == len(nums) - 1:
                            solutionFound = True
                            break
            if solutionFound:
                break
                
        return memo[-1]
    
    
