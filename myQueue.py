class Node:
    def __init__(self, value, next_node=None):
        """
        Constructor
        :param value: any datatype
        :param next_node: pointer to next node
        """
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        """
        pointer to given node
        :param next_node: node after our current node
        :return: /
        """
        self.next_node = next_node

    def get_next_node(self):
        """
        gives the next node back
        :return: nextnode
        """
        return self.next_node

    def get_value(self):
        """
        gives the stored datatype in a node
        :return: any datatype
        """
        return self.value


class Queue:
    def __init__(self, max_size=None):
        """
        Constructor
        :param max_size: spaces for our waiting row
        """
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    # Add your enqueue method below:
    def enqueue(self, value):
        """
        Adds a new node at the tail
        :param value: any datatype
        :return: /
        """
        if self.has_space(): # checking if it has space
            item_to_add = Node(value)
            print("Adding"+str(item_to_add.get_value())+" to the queue!")

            if self.is_empty(): # check if queue is empty
                self.head = item_to_add
                self.tail = item_to_add
            else: # if there are items
                self.tail.next_node = item_to_add
                self.tail = item_to_add
                self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        """
        Removes the first Node of our Queue
        :return: any dataype
        """
        if self.is_empty(): #check if the queue is empty
            print("This queue is empty")
        else:
            item_to_remove = self.head #remove starts from the head
            print("Removing"+str(item_to_remove.get_value)+"from the queue!")
            if self.size == 1: # if there is only one node
                self.head = None
                self.tail = None
            else: # if there are multiples of nodes
                self.head = self.head.get_next_node
            self.size -= 1
            return item_to_remove.get_value()

    def peek(self): # get value of the top
        """
        returns the value of the top node
        :return: any datatype
        """
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def get_size(self):
        """
        Return the size
        :return: integer
        """
        return self.size

    def has_space(self):
        """
        Checks if there are sill spaces in our queue
        :return: bool
        """
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        """
        Give true if empty
        :return: bool
        """
        return self.size == 0

#testcode
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #