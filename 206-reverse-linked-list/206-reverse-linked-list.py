# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
    
    # Recursive
    def reverseList(self, head, prev=None):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)