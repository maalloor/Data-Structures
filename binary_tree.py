from deque import Deque

class _TreeNode:
    """Binary tree node: a value and two references, left and right."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary search tree (BST) implemented purely with linked nodes
    (no lists/tuples/dicts).

    `insert` is included so the tree can be built easily, along with
    several ways of printing it.
    """

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        """Inserts a value following BST order
        (smaller to the left, greater or equal to the right)."""
        if self.root is None:
            self.root = _TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = _TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = _TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    # ---------- Traversals that build a string (no lists) ----------

    def _inorder_str(self, node):
        if node is None:
            return ""
        left = self._inorder_str(node.left)
        right = self._inorder_str(node.right)
        text = str(node.value)
        if left:
            text = left + " " + text
        if right:
            text = text + " " + right
        return text

    def _preorder_str(self, node):
        if node is None:
            return ""
        text = str(node.value)
        left = self._preorder_str(node.left)
        right = self._preorder_str(node.right)
        if left:
            text = text + " " + left
        if right:
            text = text + " " + right
        return text

    def _postorder_str(self, node):
        if node is None:
            return ""
        left = self._postorder_str(node.left)
        right = self._postorder_str(node.right)
        # Postorder: left, right, root (the root goes last)
        text = str(node.value)
        if right:
            text = right + " " + text
        if left:
            text = left + " " + text
        return text

    def print_structure(self):
        """
        Prints the tree in three ways:
          - Inorder (left, root, right)
          - Preorder (root, left, right)
          - Postorder (left, right, root)
        plus a level-by-level view using our own Deque (not a list)
        as the auxiliary queue for the BFS traversal.
        """
        if self.is_empty():
            print("Binary tree: (empty)")
            return

        print("Binary tree")
        print("  Inorder  : " + self._inorder_str(self.root))
        print("  Preorder : " + self._preorder_str(self.root))
        print("  Postorder: " + self._postorder_str(self.root))
        print("  Level by level:")
        self._print_by_levels()

    def _print_by_levels(self):
        """BFS (level-order) traversal using our own Deque as the
        auxiliary queue instead of a Python list."""
        queue = Deque()
        queue.push_right(self.root)
        current_level = 0
        while not queue.is_empty():
            nodes_in_level = len(queue)
            level_text = ""
            counter = 0
            while counter < nodes_in_level:
                node = queue.pop_left()
                level_text += str(node.value) + " "
                if node.left is not None:
                    queue.push_right(node.left)
                if node.right is not None:
                    queue.push_right(node.right)
                counter += 1
            print("    Level " + str(current_level) + ": " + level_text.strip())
            current_level += 1
