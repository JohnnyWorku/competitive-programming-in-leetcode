# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Adding a dummy node to handle edge cases
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead to maintain a gap
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first reaches the end
        while first:
            first = first.next
            second = second.next

    # Skip the nth node from the end
        second.next = second.next.next

        return dummy.next