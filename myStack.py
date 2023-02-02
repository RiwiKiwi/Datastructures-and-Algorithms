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
        sets a pointer to next-node
        :param next_node: node after our working node
        :return: /
        """
        self.next_node = next_node

    def get_next_node(self):
        """
        get the node after our working node
        :return: next node
        """
        return self.next_node

    def get_value(self):
        """
        gives the stored value of a node
        :return: any datatype
        """
        return self.value

class Stack:
    def __init__(self,limit = 1000):
        """
        Constructor
        :param limit: max space
        """
        self.top_item = None
        self.limit = limit
        self.size = 0

    def is_empty(self):
        """
        Checks if the stack is empty
        :return: bool
        """
        if(self.size == 0):
            return True
        else:
            return False


    def push(self,value):
        """
        insert a new node at the top of the stack
        :param value: any datatype
        :return: /
        """
        if (self.has_space()):
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")


    def pop(self):
        """
        deletes the top item of the stack
        :return: any datatype
        """
        if (self.size > 0):
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty")


    def peek(self):
        """
        Gives value back of the top
        :return: any datatype
        """
        if (self.size > 0):
            return self.top_item.get_value()
        else:
            print("Stack is empty")

    def has_space(self):
        """
        Checks if there is space < 1000
        :return:  bool
        """
        if(self.limit > self.size):
            return True
        else:
            return False


###################### TEST CODE

# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()




