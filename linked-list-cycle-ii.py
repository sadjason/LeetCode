# encoding: utf-8

__author__ = 'zhangwei'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        
        hasCycle = False    # 链表是否存在环标志位

        while fast is not None and slow is not None:
            if fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                hasCycle = True
                break
        
        if hasCycle is False:
            return None
        
        slow = head
        while slow is not None:
            if slow is fast:
                return slow
            slow = slow.next
            fast = fast.next