"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    n, k = 0, 0
    value = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:

        '''
        Solution1：
        前序遍历所有节点，最后返回相应index值即可
        res = []
        def preorder(root):
            if root:
                preorder(root.left)
                res.append(root.val)
                preorder(root.right)
        preorder(root)
        return res[k-1]
        '''

        '''
        当n<k时执行遍历函数
        从叶子节点n+=1，当n==k时，给value赋值，最后返回value值
        self.n = 0
        self.k = k
        def preorder(root):
            if self.n < self.k:
                if root:
                    if root.left:
                        preorder(root.left)
                    self.n += 1
                    if self.n == self.k:
                        self.value = root.val
                    if root.right:
                        preorder(root.right)
        preorder(root)
        return self.value
        '''
        '''
        从最左边节点开始遍历，当节点没有左子树时，k -= 1.
        当k == 0时，结束循环，相反，遍历右子树
        '''

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right