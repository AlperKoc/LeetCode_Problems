class Solution:
    def countAndSay(self, n):
        
        numList = list("1")
        resultList = []
        temp = []
        
        for i in range(n-1):
            resultList.clear()
            current = numList[0]
            temp.append(current)
            
            for i in range(1,len(numList)):
                if current == numList[i]:
                    temp.append(numList[i])
                else:
                    resultList.append(str(len(temp)))
                    resultList.append(current)
                    temp.clear()
                    current = numList[i]
                    temp.append(numList[i])
                    
            resultList.append(str(len(temp)))
            resultList.append(current)
            temp.clear()
            numList = resultList.copy()
            
        return "".join(map(str,numList))
