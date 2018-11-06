class Solution:
    def plusOne(self, digits):
        
        #number = int("".join(map(str,digits)))
        #incremented = number + 1
        #strNum = str(incremented)
        #return list(map(int,list(strNum)))
        
        return list(map(int,list(str((int("".join(map(str,digits)))) + 1))))
