class TreeNode:
    def __init__(self, data):
        self.data = data
        self.fc = None
        self.sc = None
        self.tc = None

class TertiaryTree:
    def __init__(self):
        self.root = None

    def is_max_heap(self, node):
        if node is None:
            return True

        if node.fc is not None and node.data < node.fc.data:
            return False

        if node.sc is not None and node.data < node.sc.data:
            return False

        if node.tc is not None and node.data < node.tc.data:
            return False

        return self.is_max_heap(node.fc) and self.is_max_heap(node.sc) and self.is_max_heap(node.tc)

# Example usage
tree = TertiaryTree()
tree.root = TreeNode('X')
tree.root.fc = TreeNode('P')
tree.root.fc.fc = TreeNode('A')
tree.root.fc.sc = TreeNode('B')
tree.root.fc.tc = TreeNode('C')

tree.root.sc = TreeNode('Q')
tree.root.sc.fc = TreeNode('D')
tree.root.sc.sc = TreeNode('E')
tree.root.sc.tc = TreeNode('F')

tree.root.tc = TreeNode('R')

if tree.is_max_heap(tree.root):
    print("is Max heap")
else:
    print("is Not a max heap")
