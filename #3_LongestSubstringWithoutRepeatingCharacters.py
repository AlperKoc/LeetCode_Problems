class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxCount = 0
        for i in range(n):
            found = set()
            for j in range(i, n):
                if s[j] in found: 
                    break
                found.add(s[j])
            maxCount = max(len(found), maxCount)            
        return maxCount
