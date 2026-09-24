class _DequeNode:
    """Doubly linked node: knows both its previous and next node."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    """
    Double ended queue implemented as a manual doubly linked list
    (nodes with .prev and .next).

    Keeps references to the head (left end) and the tail (right end)
    so all 4 operations are O(1).
    """
    def __init__(self):
        self.head = None  # left end
        self.tail = None  # right end
        self._count = 0

    def is_empty(self):
        return self.head is None

    def push_left(self, value):
        """Adds a node to the beginning (left) of the deque."""
        new_node = _DequeNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._count += 1

    def push_right(self, value):
        """Adds a node to the end (right) of the deque."""
        new_node = _DequeNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def pop_left(self):
        """Removes and returns the value of the node at the beginning (left)."""
        if self.is_empty():
            raise IndexError("pop_left from an empty deque")
        node = self.head
        self.head = node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None  # the deque is now empty
        self._count -= 1
        return node.value

    def pop_right(self):
        """Removes and returns the value of the node at the end (right)."""
        if self.is_empty():
            raise IndexError("pop_right from an empty deque")
        node = self.tail
        self.tail = node.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None  # the deque is now empty
        self._count -= 1
        return node.value

    def __len__(self):
        return self._count

    def print_structure(self):
        """Prints the deque from left to right."""
        current = self.head
        parts = ""
        while current is not None:
            parts += str(current.value)
            if current.next is not None:
                parts += " <-> "
            current = current.next
        print("Deque (left -> right): " + parts if parts else "Deque: (empty)")
