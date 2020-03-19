"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        res = []
        # stack中是当前遍历的层的节点。
        # stack2中是当前层节点的所有左右子树。
        # 遍历完当前层，将下一层stack2 赋给stack，stack2 为空，继续存储再下一层节点
        stack, stack2 = deque(), deque()
        stack.append(root)
        while stack:
            temp = []
            while (stack):
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            stack, stack2 = stack2, stack
            res.append(temp)
        return res