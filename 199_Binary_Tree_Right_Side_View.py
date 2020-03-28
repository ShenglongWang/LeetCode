"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:


        '''
        Solution1:
        '''
        if not root:
            return []
        res = []
        stack,stack1 = [], []
        stack.append(root)
        while stack:
            while stack:
                node = stack.pop(0)
                if not stack:
                    res.append(node.val)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            stack, stack1 = stack1, stack
        return res


        '''
        Solution2:
        '''
        res = []
        def preorder(root,level):
            if root:
                if len(res) == level:
                    res.append(root.val)
                preorder(root.right,level+1)
                preorder(root.left,level+1)
        preorder(root,0)

        return res

        '''
        Solution3:
        '''
        depth_to_val = {}
        max_depth = -1
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node:
                depth_to_val[depth] = node.val
                max_depth = max_depth if max_depth > depth else depth

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [depth_to_val[depth] for depth in range(max_depth + 1)]