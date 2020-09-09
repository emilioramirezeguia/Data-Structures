"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        # check if current node has a prev pointer
        if self.prev is not None:
            self.prev.next = self.next
        # check if current node has a next pointer
        if self.next is not None:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # grab passed in value and create a new node
        new_head = ListNode(value)
        # check whether the list is empty
        # if it is, assign the new node as the list's head and tail
        if self.head is None and self.tail is None:
            self.head = new_head
            self.tail = new_head
            # increment list length by 1
            self.length += 1
        else:
            # set the new node's next pointer to the current head
            new_head.next = self.head
            # update the current head's previous pointer to the new node
            self.head.prev = new_head
            # make the new node the head of the list
            self.head = new_head
            # increment list length by 1
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # grab passed in value and create a new node
        new_tail = ListNode(value)
        # check whether the list is empty
        # if it is, assign the new node as the list's head and tail
        if self.head is None and self.tail is None:
            self.head = new_tail
            self.tail = new_tail
            # increment list length by 1
            self.length += 1
        else:
            # set the new node's previous pointer to the current tail
            new_tail.prev = self.tail
            # update the current tail's next pointer to the new node
            self.tail.next = new_tail
            # make the new node the tail of the list
            self.tail = new_tail
            # increment list length by 1
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # if there is no nodes
        if self.head is None and self.tail is None:
            return None

        # shrink list length by 1 no matter what
        self.length -= 1

        # if there is only 1 node in the list, reset everything
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # else if node_to_remove is equal to the list head, update the head of the list to the current head's next pointer
        elif node == self.head:
            # set the current head's next pointer as the head of the list
            self.head = node.next
            node.delete()
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass


test_DLL = DoublyLinkedList(ListNode("Emilio"))
# Test the __len__ method.
print(len(test_DLL))
# Check the current node's value
print(test_DLL.head.value)
# test a new node is added to head correctly
test_DLL.add_to_head(ListNode("Emilio2"))
print("List length: ", len(test_DLL))  # should return 2
print("Head's prev: ", test_DLL.head.prev)  # should return None
print("Head's next: ", test_DLL.head.next.value)  # should return "Emilio"?
print("Head's value: ", test_DLL.head.value.value)  # should return "Emilio2"
