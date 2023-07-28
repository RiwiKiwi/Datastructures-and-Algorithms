class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        """
        Constructor
        :param value: integervalue
        :param next_node: nextnode after our Node(value)
        :param prev_node: previousnode before our Node(value)
        """
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        """
        initializer for node after Node(value)
        :param next_node: Node(anothervalue)
        :return: /
        """
        self.next_node = next_node

    def get_next_node(self):
        """
        getter for node after Node(value)
        :return: Node(anothervalue)
        """
        return self.next_node

    def set_prev_node(self, prev_node):
        """
        initializer for node before Node(value)
        :param prev_node: Node(anothervalue)
        :return:
        """
        self.prev_node = prev_node

    def get_prev_node(self):
        """
        getter for node before Node(value)
        :return: Node(anothervalue)
        """
        return self.prev_node

    def get_value(self):
        """
        gives value of a certain node
        :return: integer
        """
        return self.value


class DoublyLinkedList:
    def __init__(self):
        """
        Constructor
        """
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        """
        Makes a new node and then adds at the beginning
        :param new_value: any datatype
        :return: /
        """
        new_head = Node(new_value)  # Making a node to insert with a given value
        current_head = self.head_node  # pointer to head

        if current_head != None:  # er is al een headnode aanwezig
            current_head.set_prev_node(new_head)  # set prevptr to newhead
            new_head.set_next_node(current_head)  # set newhead's nextptr to currenthead

        self.head_node = new_head  # if it's empty => our made node will be our new head

        if self.tail_node == None:  # if tail == No value
            self.tail_node = new_head  # that samenode will also be the tail

    def add_to_tail(self, new_value):
        """
        Makes a new node and then adds at the end
        :param new_value: any datatype
        :return: /
        """
        new_tail = Node(new_value)  # Making a node to insert with a given value
        current_tail = self.tail_node  # pointer to tail

        if current_tail != None:  # er is een tailnode aanwezig
            current_tail.set_next_node(new_tail)  # curr_tail nextptr will be newtail
            new_tail.set_prev_node(current_tail)  # new_tail prev will be current_tail

        self.tail_node = new_tail  # if there isn't tail ....

        if self.head_node == None:  # if there isn't head
            self.head_node = new_tail

    def remove_head(self):
        """
        Removes the head
        :return: value
        """
        removed_head = self.head_node  # ptr to headnode

        if removed_head == None:  # if head is already empty
            return None  # there is no value

        self.head_node = removed_head.get_next_node()  # if head isn't empty, the next_node after the deleting head will be the new head

        if self.head_node != None:  # if this new headnode isn't empty
            self.head_node.set_prev_node(None)  # the previous has to be empty

        if removed_head == self.tail_node:  # if it's in case the tail
            self.remove_tail()

        return removed_head.get_value()  # the value that gets removed

    def remove_tail(self):
        """
        Removes the tail
        :return: value
        """
        removed_tail = self.tail_node  # pointer to tail

        if removed_tail == None:  # checking if tail is empty
            return None  # there is no value

        self.tail_node = removed_tail.get_prev_node()  # the tail node will be then the previous one after the None valued (node)

        if self.tail_node != None:  # checking if that new pointed tailnode isn't empty
            self.tail_node.set_next_node(None)  # if yes, the next_node has to be None

        if removed_tail == self.head_node:  # if it's in casse the head
            self.remove_head()

        return removed_tail.get_value()  # the value that gets removed

    def remove_by_value(self, value_to_remove):
        """
        Give a certain value to remove
        :param value_to_remove: any datatype
        :return: value
        """
        node_to_remove = None  # We don't know yet
        current_node = self.head_node  # ptr to head

        ###################################  FIND THE DELETING NODE ##########################################################
        while current_node != None:  # go through whole list
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node  # initialize the var, FOUNDED THE NODE
                break  # STOP
            current_node = current_node.get_next_node()  # else, keep on going

        if node_to_remove == None:  # if there is no node with a value
            return None
        ################################## CHECK THE PLACE OF THE NODE #######################################################
        if node_to_remove == self.head_node:  # if it's the headnode
            self.remove_head()
        elif node_to_remove == self.tail_node:  # if it's the tailnode
            self.remove_tail()
        else:  # it's in the middle

            # setting the pointers of it

            next_node = node_to_remove.get_next_node()  # initialize
            prev_node = node_to_remove.get_prev_node()  # idem
            next_node.set_prev_node(prev_node)  # initialize the pointer
            prev_node.set_next_node(next_node)  # idem

        return node_to_remove

    def stringify_list(self):
        """
        Prints our Doubly linked list
        :return: string
        """
        string_list = ""
        current_node = self.head_node  # ptr to head
        while current_node:
            if current_node.get_value() != None:  # keep going till end of the list
                string_list += str(current_node.get_value()) + "\n"  # print the whole linkedlist
            current_node = current_node.get_next_node()  # update the pointer
        return string_list  # print the list




#################################### TEST CODE : MAKING A SUBWAY ######################################################
subway = DoublyLinkedList()

subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

print(subway.stringify_list())

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()
print(subway.stringify_list())

subway.remove_by_value("Times Square")
print(subway.stringify_list())
