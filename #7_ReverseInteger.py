class Solution:
    def reverse(self, x):
        reverse = list(reversed(str(x)))
        result = []
        
        for i in range(len(reverse)-1):
            if reverse[0] == '0':
                del reverse[0]
        
        if reverse[-1] == '-' or reverse[-1] == '+':
            result = reverse[-1] + "".join(reverse[:-1])       
        else:
            result = "".join(reverse)
        
        intResult = int(result)
        if intResult <= 2**31 - 1 and intResult >= -1* 2**31:
            return int(result)
        else:
            return 0

       
        
        
        
