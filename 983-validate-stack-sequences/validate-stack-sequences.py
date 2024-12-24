class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []

        for num in pushed:
            stack.append(num)
            while stack and i < len(popped) and popped[i] == stack[-1]:
                stack.pop()
                i += 1

        return not stack    #If the stack is empty it returns true