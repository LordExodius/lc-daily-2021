# Oscar Yu
# May 20th, 2021

def kthSmallest(self, root: TreeNode, k: int) -> int:
    orderList = []
    def inorder(root):
        if not root is None:
            inorder(root.left)
            orderList.append(root.val)
            inorder(root.right)
    inorder(root)
    print(orderList)
        
    return orderList[k - 1]

# Optimizations:
"""
- can call inorder traversal on left side of tree first, then right side if
not enough elements are found (vai)
"""