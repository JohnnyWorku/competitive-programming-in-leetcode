class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for p in path + "/":  # "/" is used to handle the last case
            if p == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""

            else:
                cur += p

        return "/" + "/".join(stack)