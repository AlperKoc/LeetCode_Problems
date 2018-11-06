class Solution:
    def romanToInt(self, s):
        romans = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        intList = []
        totalSum = 0
        
        for i in range(len(s)):
            intList.append(romans[s[i]])
            
        for i in range(len(intList)):
            if i<len(intList)-1 and intList[i+1] > intList[i]:
                totalSum -= intList[i]
            else:
                totalSum += intList[i]
                
        return totalSum
