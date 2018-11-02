class Solution:
    def isPalindrome(self, x):
        x = str(x)
        first = 0
        last = len(x)-1
        palyndrome = True
        for i in range(len(x)//2):
            if x[first] != x[last]:
                palyndrome = False
                break
            first+=1
            last-=1
        if palyndrome:
            return True
        else:
            return False
                
        
        
