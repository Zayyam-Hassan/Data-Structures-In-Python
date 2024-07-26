class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = TreeNode(val)
            return
        current_node = self.head
        prev_node = None
        while current_node:
            prev_node = current_node
            if current_node.data > val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if prev_node.data > val:
            prev_node.left = TreeNode(val)
        else:
            prev_node.right = TreeNode(val)

    def delete(self, val):
        self.head = self._delete_node(self.head, val)

    def _delete_node(self, node, val):
        if node is None:
            return node
        if val < node.data:
            node.left = self._delete_node(node.left, val)
        elif val > node.data:
            node.right = self._delete_node(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self._min_value_node(node.right).data
            node.right = self._delete_node(node.right, node.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def __inorderhelper(self, current_node):
        if not current_node:
            return
        self.__inorderhelper(current_node.left)
        print(current_node.data, end='  ')
        self.__inorderhelper(current_node.right)

    def inorder_traversal(self):
        self.__inorderhelper(self.head)
