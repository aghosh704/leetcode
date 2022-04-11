#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        tmp = []
        while True:
            tmp.append(head.val)
            head = head.next
            if head is None:
                break
        f = 0
        l = len(tmp) - 1
        isPalindrome = True
        while f < l:
            if tmp[f] == tmp[l]:
                pass
            else:
                isPalindrome = False
                break
            f += 1
            l -= 1

        return isPalindrome

l1 = ListNode("a")
l2 = ListNode("b")
l3 = ListNode("b")
l4 = ListNode("a")

l1.next = l2
l2.next = l3
l3.next = l4

print(Solution().isPalindrome(l1))