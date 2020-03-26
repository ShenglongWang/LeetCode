"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:


    '''
    解题思路：
    每次递归返回当前节点，当前节点+左子树和，当前节点+右子树和，子树和+当前节点中的最大值
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxValue = float('-inf')

        def maxValuePath(root):
            if not root:
                return 0
            left = maxValuePath(root.left)
            right = maxValuePath(root.right)
            temp = max(left, right)
            if temp < 0:
                self.maxValue = max(root.val, self.maxValue)
            self.maxValue = max(self.maxValue, left + root.val, right + root.val, left + right + root.val)
            return max(root.val, root.val + left, root.val + right)

        maxValuePath(root)
        return self.maxValue