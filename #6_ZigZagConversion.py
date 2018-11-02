class Solution:
    def convert(self, s, numRows):
        col = len(s)
        row = numRows
    
        if row == 1:
            return s

        table = [[' ' for x in range(col)] for y in range(row)]
        
        colIndex = 0
        rowIndex = 0
        direction = False # move down or move to upper right
        for i in s:
            table[rowIndex][colIndex] = i
            if not direction:
                if rowIndex == row - 1:
                    direction = True
                    rowIndex -= 1
                    colIndex += 1                
                else:
                    rowIndex += 1
            elif direction:
                if rowIndex == 0:
                    rowIndex +=1
                    direction = False
                else:
                    rowIndex -= 1
                    colIndex += 1
        result = []
        
        for i in table:
            result.append("".join(i))
            result[-1] = result[-1].replace(" ","")
        return "".join(result)

        
