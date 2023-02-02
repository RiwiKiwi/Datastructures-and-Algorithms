
class Node:
    def __init__(self, value, next_node=None):
        """
        constructor
        :param value: any datatype
        :param next_node:
        """
        self.value = value # Node with a value
        self.next_node = next_node # where it is linked to

    def get_value(self):
        """
        Gives value of our node
        :return: any datatype
        """
        return self.value

    def get_next_node(self):
        """
        Gives the node after our constructed node
        :return: memorylocation
        """
        return self.next_node

    def set_next_node(self, next_node):
        """
        Sets a pointer to another where it needs to be pointed
        :param next_node: node where it needs to be pointed
        :return: /
        """
        self.next_node = next_node


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        """
        Constructor
        :param value: any datatype
        """
        self.head_node = Node(value)

    def get_head_node(self):
        """
        gives the first node of our linked list
        :return: headnode
        """
        return self.head_node

    def insert_beginning(self, new_value):
        """
        Inserts at the position of our headnode
        :param new_value: any datatype
        :return: /
        """
        new_node = Node(new_value) # making a new node to insert
        new_node.set_next_node(self.head_node) # pointer to existing headnode
        self.head_node = new_node # existing headnode will be the new_node

    def stringify_list(self):
        """
        prints our Linked list out
        :return: our linkedlist
        """
        string_list = ""
        current_node = self.get_head_node() # pointer to head
        while current_node:
            if current_node.get_value() != None: # till it hasn't reached the end of the linkedlist
                string_list += str(current_node.get_value()) + "\n" # everyvalue will be printed
            current_node = current_node.get_next_node() #pointer = pointer + 1
        return string_list

    def remove_node(self, value_to_remove):
        """
        removes the value from our linked list
        :param value_to_remove: any datatype
        :return: /
        """
        current_node = self.get_head_node() # pointer to head
        if current_node.get_value() == value_to_remove: # checking if the value is in the head
            self.head_node = current_node.get_next_node() # new head_node will be the second_node after the deleted head_node
        else:
            while current_node:
                next_node = current_node.get_next_node() # pointer = pointer + 1
                if next_node.get_value() == value_to_remove: # check if you got the value
                    current_node.set_next_node(next_node.get_next_node()) # curr will point to the next_node after your deleting node
                    current_node = None # change it back to nullptr
                else:
                    current_node = next_node # else keep going i guess...

# These are optional functions

    def swap_nodes(self, val1, val2):
        """
        Swaps positions between 2 nodes
        :param val1: value of first node
        :param val2:  value of second node
        :return: /
        """
        print(f'Swapping {val1} with {val2}')

        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

    def nth_last_node(self, n):
        """
        Function to return n-th last element with 2 pointers
        :param n: steps to delay currentpointer
        :return: any datatype of nth last pointer
        """
        current = None
        tail_seeker = self.head_node
        count = 1
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= n + 1:
                if current is None:
                    current = self.head_node
                else:
                    current = current.get_next_node()
        return current

    def find_middle(self):
        """
        Returns the middle of the list using 2 pointers
        :return: any datatype
        """
        fast_pointer = self.head_node
        slow_pointer = self.head_node

        while fast_pointer is not None:
            fast_pointer = fast_pointer.get_next_node()
            if fast_pointer:
                fast_pointer = fast_pointer.get_next_node()
                slow_pointer = slow_pointer.get_next_node()
        return slow_pointer

############################################### TEST CODE ##############################################################
ll = LinkedList()
ll.insert_beginning(1)
ll.insert_beginning(2)
ll.insert_beginning(3)
print(ll.stringify_list())
print(ll.get_head_node().get_value())
print(ll.get_head_node().get_next_node().get_value())






