# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result=[]
        queue=[root]
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                TreeNode=queue.pop(0)
                level.append(TreeNode.val)
                if TreeNode.left:
                    queue.append(TreeNode.left)
                if TreeNode.right:
                    queue.append(TreeNode.right)
            result.append(level)
        return result
