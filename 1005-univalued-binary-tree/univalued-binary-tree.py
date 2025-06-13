# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # # BFS
        # queue = deque([root])
        # is_univalued = True
        # init_value = root.val

        # while queue:
        #     node = queue.popleft()

        #     if node.val != init_value:
        #         is_univalued = False
        #         break

        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # return is_univalued

        # DFS
        init_value = root.val
        def dfs(node):
            nonlocal init_value

            if node.val != init_value:
                return False

            if node.left:
                if not dfs(node.left):
                    return False
            if node.right:
                if not dfs(node.right):
                    return False

            return True

        return dfs(root)
        