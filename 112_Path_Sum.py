"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # solution1:
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right

        # solution2:
        '''
        if root == None:
            return False
        stack = [(root.val,root),]
        while stack:
            s, root = stack.pop()
            if not root.left and not root.right and s == sum:
                return True
            child = [root.left, root.right]
            for node in child:
                if node:
                    stack.append((s + node.val, node))
        return False
        '''