"""
@version:01.00.00
@Author:Shenglong
"""


class Solution:

    '''
    解题思路：

    中序第一个为根节点，然后在前序中找根节点，找到后，根节点左边为所有左子树
    右边为所有右子树。依次类推，在前序中找中序中根节点的左右子树

    前序:[9,3,15,20,7]  inOrder
    中序:[3,9,20,15,7]  preOrder
    prestart 中序开始的index
    instart  前序开始的index
    inend    前序结束的index

    在构建左子树时，左子树根节点为prestart+1，在前序[instart : inend] 中找。
    右子树有点麻烦，需要计算在根节点的左子树有多少个节点，再与prestart相加
    ex:
    根节点为 3
                 [9,3,15,20,7]
                    3
    构建左子树， prestart+1， 即中序中的9。instart 不变， inend 为 index-1（即3的index-1）
    构建右子树， 在根节点3 左侧，有 index - instart 个元素，算上根节点3，prestart 为
    prestart+ index - instart + 1 ， instart 为 index + 1， inend不变


    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def rebuildTree(prestart, instart, inend, preOrder, inOrder):
            if prestart > len(preOrder) - 1 or instart > inend:
                return None
            index = 0
            root = TreeNode(preOrder[prestart])

            for i in range(instart, inend + 1):
                if inOrder[i] == root.val:
                    index = i
                    break
            root.left = rebuildTree(prestart + 1, instart, index - 1, preOrder, inOrder)
            root.right = rebuildTree(prestart + index - instart + 1, index + 1, inend, preOrder, inOrder)

            return root

        return rebuildTree(0, 0, len(inorder) - 1, preorder, inorder)