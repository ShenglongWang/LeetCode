"""
@version:01.00.00
@Author:Shenglong
"""

'''
解题思路跟105一样
把后序数列翻转，即可得到遍历顺序为中右左的数列。
构造顺序相应的先构造右子树，再构造左子树。
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder.reverse()
        print(postorder)

        def rebuildTree(poststart, instart, inend, postOrder, inOrder):
            if poststart > len(postOrder) - 1 or instart > inend:
                return None
            index = 0
            root = TreeNode(postOrder[poststart])

            for i in range(instart, inend + 1):
                if inOrder[i] == root.val:
                    index = i
                    break
            root.right = rebuildTree(poststart + 1, index + 1, inend, postOrder, inOrder)
            root.left = rebuildTree(poststart + inend - index + 1, instart, index - 1, postOrder, inOrder)

            return root

        return rebuildTree(0, 0, len(postorder) - 1, postorder, inorder)
