# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dimater=0
        def height(TreeNode):
            nonlocal dimater
            if TreeNode is None:
                return 0
            left_height=height(TreeNode.left)
            right_height=height(TreeNode.right)
            dimater=max(dimater,left_height+right_height)
            return max(left_height,right_height)+1
        height(root)
        return dimater