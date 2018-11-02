class Solution:
    def addTwoNumbers(self, l1, l2):
        sum1 = 0
        sum2 = 0
        
        mult = 1
        while(l1 != None):
            sum1 += l1.val * mult
            l1 = l1.next
            mult *= 10
        
        mult = 1
        while(l2 != None):
            sum2 += l2.val * mult
            l2 = l2.next
            mult *= 10
        
        total = sum1 + sum2 
        
     
        if total == 0:
            node = ListNode(0)
            return node
        else:
            strVal = str(total)
            strList = list(strVal)
            revList = list(reversed(strList))
            head = ListNode(revList[0])
            
            linkedList = []
            linkedList.append(head)
            
            for i in range(1,len(revList)):
                node = ListNode(revList[i])
                linkedList.append(node)
            
            for i in range(len(linkedList)-1):
                linkedList[i].next = linkedList[i+1]
            return head
            
                
        
        
