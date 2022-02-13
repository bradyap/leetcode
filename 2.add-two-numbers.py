#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        
        carry = 0
        
        while l1 is not None or l2 is not None:
            s = carry
            
            if l1 is not None:
                s += l1.val
                l1 = l1.next
                
            if l2 is not None:
                s += l2.val
                l2 = l2.next
                
            new = ListNode(s % 10)
            carry = s // 10
            
            if temp is None:
                head = new
                temp = head
            else: 
                temp.next = new
                temp = temp.next
                
        if carry > 0:
            temp.next = ListNode(carry)
        
        return head
# @lc code=end

