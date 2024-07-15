class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        if not descriptions:
            return None
        
        node_map = {}
        children = set()
        
        # Constructing the tree
        for parent, child, isLeft in descriptions:
            children.add(child)
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if isLeft == 1:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
        
        # Finding the root node
        root_value = None
        for parent, _, _ in descriptions:
            if parent not in children:
                root_value = parent
                break
        
        # Return the root node
        return node_map.get(root_value, None)

