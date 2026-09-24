class _StackNode:
    """Simple node: holds a value and a reference to the node below it."""

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Stack (LIFO - Last In, First Out) implemented with linked nodes.

    The "top" of the stack is self.top. Inserting and removing always
    happens at the top, so push/pop are O(1).
    """

    def __init__(self):
        self.top = None
        self._count = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        """Adds a new node to the top of the stack."""
        new_node = _StackNode(value)
        new_node.next = self.top
        self.top = new_node
        self._count += 1

    def pop(self):
        """Removes and returns the value of the node at the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        node = self.top
        self.top = node.next
        self._count -= 1
        return node.value

    def peek(self):
        """Returns the value at the top without removing it (extra utility)."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.top.value

    def __len__(self):
        return self._count

    def print_structure(self):
        """Prints the stack from the top to the bottom."""
        current = self.top
        parts = ""
        while current is not None:
            parts += str(current.value)
            if current.next is not None:
                parts += " -> "
            current = current.next
        print("Stack (top -> bottom): " + parts if parts else "Stack: (empty)")
