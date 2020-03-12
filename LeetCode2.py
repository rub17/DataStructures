# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        outNode = ListNode(0)
        curr = outNode
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                carry = carry + l1.val 
                l1 = l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            while curr.next != None:
                curr = curr.next
            curr.next = ListNode(carry%10)
            carry = int(carry / 10)
            
        return outNode.next
