class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char_s in s:
            if char_s == "#":
                if stack_s:
                    stack_s.pop()

            else:
                stack_s.append(char_s)

        for  char_t in t:
            if char_t == "#":
                if stack_t:
                    stack_t.pop()

            else:
                stack_t.append(char_t)

        return stack_s == stack_t
