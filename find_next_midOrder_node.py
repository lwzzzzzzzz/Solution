#               -------------------------
# 树节点结构是  |left|value|right|parent|     parent即代码的next
#               -------------------------
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        pNext = None
        if pNode.right != None: # 找右子树的最左节点
            pNext = pNode.right
            while pNext.left != None:
                pNext = pNext.left
        elif pNode.next != None: # 如无右子树，case1：当前节点是其父节点的左子树，则下一个就是父节点
                                 #             case2：当前节点是其父节点的右子树，则在往上找父节点
            pNext, pCur = pNode.next, pNode
            while pNext != None and pNext.right == pCur:
                pCur = pNext
                pNext = pCur.next
        return pNext
