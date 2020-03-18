"""
@version:01.00.00
@Author:Shenglong
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode, length=1) -> int:
        if root == None:
            return 0
        from collections import deque

        depth = 1
        # 理解stack为某一层需要遍历的节点，stack2为下一层需要比那里的节点
        stack, stack2 = deque(), deque()
        stack.append(root)
        while (len(stack) > 0):
            while (len(stack) > 0):
                tree = stack.pop()
                if tree.left == None and tree.right == None:
                    return depth
                if tree.left != None:
                    stack2.append(tree.left)
                if tree.right != None:
                    stack2.append(tree.right)
            # 此层节点stack遍历结束，准备遍历下层节点（stack2）
            stack, stack2 = stack2, stack
            depth += 1
