# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Dummy node to handle edge cases where `left` is the first node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Traverse to the node before the `left` node
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist from `left` to `right`
        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next



        