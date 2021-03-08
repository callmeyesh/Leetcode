# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        current, output = root, []

        while current:
            if not current.left:
                output.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    output.append(current.val)
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        return output


    def inorderTraversal(self, root:TreeNode) -> List[int]:
        current, output = root, []

        while current:
            if not current.left:
                output.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    output.append(current.val)
                    current = current.right
        return output
