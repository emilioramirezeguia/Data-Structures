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
        # no matter what, increment list length by 1
        self.length += 1
        # check whether the list is empty
        # if it is, assign the new node as the list's head and tail
        if self.head is None and self.tail is None:
            self.head = new_head
            self.tail = new_head
        else:
            # set the new node's next pointer to the current head
            new_head.next = self.head
            # update the current head's previous pointer to the new node
            self.head.prev = new_head
            # make the new node the head of the list
            self.head = new_head

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
        # check if the node is currently the head
        if node == self.head:
            return None

        # grab the passed in node's value
        value = node.value

        # if node is currently at tail
        if node == self.tail:
            self.remove_from_tail()
        # else if node is in the middle
        else:
            node.delete()
            self.length -= 1

        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # check to see if node is equal to the list tail
        if node == self.tail:
            return None

        # grab the value of the node
        value = node.value

        # if node is equal to head, call remove_from_head
        if node == self.head:
            self.remove_from_head()
        # else if node is in the middle
        else:
            node.delete()
            self.length -= 1

        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # check to see if list is empty
        if self.head is None and self.tail is None:
            return None

        # shrink list length by 1 no matter what
        self.length -= 1

        # if there is only 1 node in the list, reset everything
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # else if node is equal to the current head, update head to the current head's next pointer
        elif node == self.head:
            # set the current head's next pointer as the head of the list
            self.head = node.next
            node.delete()
        # else if node is equal to the current tail, update tail to the current tail's prev pointer
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        # else if node is between head and tail, simply delete the node
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # check to see if list is empty
        if self.head is None and self.tail is None:
            return None

        # keep a record of the max value, starting with the first
        max_value = self.head.value
        # grab a hold of the current node
        current_node = self.head

        while current_node is not None:
            # compara the current node's value to the current max value
            if current_node.value > max_value:
                max_value = current_node.value
            # then update the current value to keep traversing through list
            current_node = current_node.next
        # when there are no longer any nodes left, return max value
        return max_value
