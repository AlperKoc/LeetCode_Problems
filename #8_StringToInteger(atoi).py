class Solution:
    def myAtoi(self, str):
        minI = -1 * (2**31)
        maxI = (2**31) - 1
        result = []
        firstChar = True
        
        if len(str) == 0 or str == '+' or str == '-' or firstChar:
            return 0
        
        for i in range(len(str)):
            if(str[i] != ' ' and firstChar): # nonspace and firstChar
                if str[i] == '-' or str[i] == '+' or str[i].isdigit(): # +,- or digit
                    result.append(str[i])
                else: # char
                    return(0)
                    break
                firstChar = False
            elif(not firstChar): # nonspace
                if(str[i].isdigit()): # digit
                    result.append(str[i])
                else: # char
                    break
        
        if len(result) == 1 and (result[0] == '+' or result[0] == '-'):
            return 0
        
        resultInt = int("".join(result))
        
        if resultInt > maxI:
            return maxI
        elif resultInt < minI:
            return minI
        return int(resultInt)
