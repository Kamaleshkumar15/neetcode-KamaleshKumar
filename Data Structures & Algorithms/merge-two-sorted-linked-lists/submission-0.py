# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while a:
            arr.append(a.val)
            a = a.next

        while b:
            arr.append(b.val)
            b = b.next

        arr.sort()

        d = ListNode(0)
        c = d

        for x in arr:
            c.next = ListNode(x)
            c = c.next

        return d.next
            