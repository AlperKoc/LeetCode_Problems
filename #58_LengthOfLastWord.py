class Solution:
    def lengthOfLastWord(self, s):
        count = 0
        
        if s.count(' ') == len(s):
            return 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and count != 0:
                break
            elif s[i] !=  ' ':
                count += 1

        return count
        
