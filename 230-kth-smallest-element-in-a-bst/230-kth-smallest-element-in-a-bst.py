# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = deque()
        self.inOrderTraverse(root, nodes)
        return nodes[k-1]
    
    def inOrderTraverse(self, root, nodes):
        if root is None:
            return
        if root.left is not None:
            self.inOrderTraverse(root.left, nodes)
        nodes.append(root.val)
        if root.right is not None:
            self.inOrderTraverse(root.right, nodes)
        
        
        