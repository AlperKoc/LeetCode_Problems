class Solution:
    def intToRoman(self, num):
        romans = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
        numList = list(str(num))
        length = len(str(num))
        c = 10**(length-1)
        roman =[]

        if num in romans:
            return romans[num]
        if num >= 1000:
            roman.append("M"*(num//1000))
            del numList[0]
            num -= 1000 * (num//1000)
            length -= 1
            c /= 10 #100
            
        for i in range(length):
            n = numList[i] 
            if int(n) == 0:
                c /= 10 
                continue
            if int(n) < 5:
                if int(n) <= 3:
                    if int(n) % 3 == 0:
                        roman.append(3*romans[c])
                    else:
                        roman.append((int(n)%3)*romans[c])
                if int(n) % 4 == 0:
                    roman.append(romans[c])
                    roman.append(romans[c*5])
            if int(n) == 5:
                roman.append(romans[c*5])
            if int(n) > 5:
                n = str(int(n) - 5)
                if int(n) <= 3:
                    if int(n) % 3 == 0:
                        roman.append(romans[c*5])
                        roman.append(3*romans[c])
                    else:
                        roman.append(romans[c*5])
                        roman.append((int(n)%3)*romans[c])
                if int(n) % 4 == 0:
                    roman.append(romans[c])
                    roman.append(romans[c*10]) 
            c /= 10 
        return "".join(roman)
        
