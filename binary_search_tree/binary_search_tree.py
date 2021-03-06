"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # elif value >= self.value:
        #     if self.right is None:
        #         self.right = BSTNode(value)
        #     else:
        #         self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the root node's value equals the target
        if target == self.value:
            return True
        # check if the root's value is less than the target
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # check if the root's value is greater than the target
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right:
            current_node = current_node.right
        return current_node.value
        # max_value = self.value
        # current_node = self

        # while current_node is not None:
        #     if current_node.value > max_value:
        #         max_value = current_node.value
        #     current_node = current_node.right

        # return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on root node's value first
        fn(self.value)
        # check if there is a left child node
        if self.left is not None:
            # call for_each on the left childe node
            self.left.for_each(fn)
        # check if there is a right child node
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # check if there is a left child node
        if self.left is not None:
            # call for_each on the left child node
            self.left.in_order_print()
        # call function on root node's value last
        print(self.value)
        # check if there is a right child node
        if self.right is not None:
            self.right.in_order_print()

        # # create a stack
        # stack = Stack()
        # # grab highest value node and push it to stack
        # while self.right:
        #     self = self.right
        # current_node = self
        # s.push(current_node)
        # # check whether there are nodes in the stack
        # while len(s):
        #     # if there are no children, push it to stack
        #     # if there is not left child, print lowest value
        #     if current_node.left is None:
        #         if current_node.right is None:
        #             s.pop()
        #             print(current_node.value)
        #         else:

        #     if:
        #         current_node = current_node.left
        #         current_node.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        queue = Queue()

        current_node = self
        queue.enqueue(current_node)

        while len(queue) > 0:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()

        current_node = self
        stack.push(current_node)

        while len(stack):
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # call function on root node's value first
        print(self.value)
        # check if there is a left child node
        if self.left is not None:
            # call for_each on the left childe node
            self.left.pre_order_dft()
        # check if there is a right child node
        if self.right is not None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # check if there is a left child node
        if self.left is not None:
            # call for_each on the left childe node
            self.left.post_order_dft()
        # check if there is a right child node
        if self.right is not None:
            self.right.post_order_dft()
        # call function on root node's value last
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
