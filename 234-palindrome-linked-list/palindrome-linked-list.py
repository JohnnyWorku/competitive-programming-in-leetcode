# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # stack = []
        # length = 1
        # current = head
        
        # while current.next:
        #     current = current.next
        #     length += 1

        # # if length == 1:
        # #     return False

        # current = head
           
        # if length % 2 == 0:    # reassigning current as head
        #     for i in range(length // 2):
        #         stack.append(current.val)
        #         current = current.next

        # else:
        #     for i in range(length // 2):
        #         stack.append(current.val)
        #         current.val
            
        #     current = current.next   # To not to consider the middle element

        # while stack and current:
        #     top = stack.pop()
        #     if current.val == top:
        #         current =current.next
        #     else:
        #         return False

        # return True


        nums = []
        current = head

        while current:
            nums.append(current.val)
            current = current.next

        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

