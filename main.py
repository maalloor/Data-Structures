from stack import Stack
from deque import Deque
from binary_tree import BinaryTree

def demo_stack():
    print("=== Stack Demo ===")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_structure()   # Stack (top -> bottom): 3 -> 2 -> 1
    print("pop():", stack.pop())
    stack.print_structure()

def demo_deque():
    print("\n=== Deque Demo ===")
    deque = Deque()
    deque.push_right(2)
    deque.push_right(3)
    deque.push_left(1)
    deque.push_right(4)
    deque.print_structure()   # Deque (left -> right): 1 <-> 2 <-> 3 <-> 4
    print("pop_left():", deque.pop_left())
    print("pop_right():", deque.pop_right())
    deque.print_structure()

def demo_binary_tree():
    print("\n=== Binary Tree Demo ===")
    tree = BinaryTree()
    for value in (5, 3, 8, 1, 4, 7, 9):
        tree.insert(value)
    tree.print_structure()

if __name__ == "__main__":
    demo_stack()
    demo_deque()
    demo_binary_tree()
