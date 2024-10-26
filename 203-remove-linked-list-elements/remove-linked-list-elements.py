# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        initial = ListNode()
        initial.next = head
        prev = initial

        current = head
        while current:
            if current.val == val:
                prev.next = current.next
                current = prev.next
            else:
                current = current.next
                prev = prev.next

        return initial.next

                