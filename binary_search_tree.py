class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self.bst_insert(self.root, value)

    def bst_insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self.bst_insert(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif value > current_node.value:
            if current_node.right:
                self.bst_insert(current_node.right, value)
            else:
                current_node.left = Node(value)


    def search(self, query):
        return self.bst_search(self.root, query)

    def bst_search(self, node, query):
        if node.value == query:
            return True
        elif node.value < query and node.left:
            return self.bst_search(node.left, query)
        elif node.value > query and node.right:
            return self.bst_serach(node.right, query)
        else:
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, current, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if current:
            traversal += (str(current.value) + "-")
            traversal = self.preorder_print(current.left, traversal)
            traversal = self.preorder_print(current.right, traversal)
        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_tree()

# Check search
# Should be True
print tree.search(4) == True
# Should be False
print tree.search(6) == False