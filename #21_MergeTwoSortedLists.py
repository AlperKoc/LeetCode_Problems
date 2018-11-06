# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import copy
class Solution:
    def printList(self,l):
        while l != None:
            print(l.val)
            l = l.next
    def mergeTwoLists(self, l1, l2):

        
        mergedList = ListNode(0)
        mergedHead = mergedList
        current = 0
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if (l1 == None) and (l2 == None):
            return l1
        
        if l1.val < l2.val:
            mergedList.val = l1.val
            l1 = l1.next
        else:
            mergedList.val = l2.val
            l2 = l2.next
        
        while True:
            newNode = ListNode(0)
            if l1 == None:
                mergedList.next = l2
                break
            if l2 == None:
                mergedList.next = l1
                break
            if (l1 == None) and (l2 == None):
                print("both none")
                break
            if l1.val < l2.val:
                newNode.val = l1.val
                if l1 == None:
                    print("l1")
                else:
                    l1 = l1.next
            else:
                newNode.val = l2.val
                if l2 == None:
                    print("l2")
                else:
                    l2 = l2.next
            mergedList.next = newNode
            mergedList = mergedList.next
        self.printList(mergedHead)
        return(mergedHead)
    
