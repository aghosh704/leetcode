"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    from typing import Optional
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_map = {}
        while headA:
            ptr_map[headA] = 1
            headA = headA.next
        while headB:
            if headB:
                if headB in ptr_map:
                    return headB
            headB = headB.next
        return None

