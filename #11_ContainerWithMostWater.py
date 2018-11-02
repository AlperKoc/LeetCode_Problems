class Solution:
    def maxArea(self, height):
        maxArea = 0

        if len(height) == 2:
            return min(height[0],height[1])
        
        i = 0
        j = len(height) - 1
        maxArea = max(maxArea, (j-i) * min(height[i],height[j]))
        
        while i != j:
            if height[i] < height[j]:
                i += 1
            else:
                j-=1
            maxArea = max(maxArea, (j-i) * min(height[i],height[j]))
            
        return maxArea
            
