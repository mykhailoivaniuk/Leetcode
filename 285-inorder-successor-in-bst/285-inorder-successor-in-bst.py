# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev = None
        stack = deque()
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return None
            root = stack.pop()
            if p == prev:
                return root
            prev = root
            root = root.right