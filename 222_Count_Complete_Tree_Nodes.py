"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    '''
    Solution1:
    遍历所有节点，将所有节点加入数组，最后返回数组长度。
    O(N)
    '''
    count = 0
    def countNodes(self, root: TreeNode) -> int:

        count = 0

        def inorder(root):
            if not root:
                return
            self.count += 1
            inorder(root.left)
            inorder(root.right)

        inorder(root)
        return self.count

    '''
    Solution2:
    O(logN)
    '''

    def countNodes(self, root: TreeNode) -> int:
        lh, rh = 0, 0
        cur = root
        while cur:
            lh += 1
            cur = cur.left
        cur = root
        while cur:
            rh += 1
            cur = cur.right
        return (2 ** lh - 1) if lh == rh else 1 + (self.countNodes(root.left) + self.countNodes(root.right))