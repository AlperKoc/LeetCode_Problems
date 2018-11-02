class Solution:
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        minLen = min(map(len, strs))
        pref = []
        finish = False
        
        for j in range(minLen):
            count = 0
            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i+1][j]:
                    finish = True
                    break
                else:
                    count += 1
                if count == len(strs) - 1:
                    pref.append(strs[i][j])
            if finish:
                break
        return "".join(pref)
