# encoding: utf-8

__author__ = 'zhangwei'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast is not None and slow is not None:
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False