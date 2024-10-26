# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return current
        while current.next:
            if current.val != current.next.val:
                current = current.next
            else:
                current.next = current.next.next

        return head