class Node:
    def __init__(self,value,link_node = None):
        """
        Constructor for our Node
        :param value: Containing worth
        :param link_node: pointer
        """
        self.value = value
        self.link_node = link_node

    def get_value(self):
        """
        Gives value for newly created Node
        :return: integer
        """
        return self.value

    def get_link_node(self):
        """
        Gives the linked node of our constructed node
        :return: node, where our setlink is pointed
        """
        return self.link_node

    def set_link_node(self,link_node):
        """
        creates a pointer , pointing to another node
        :param link_node: node where it needs to be pointed at
        """
        self.link_node = link_node

########################################### TEST CODE #################################################################
node1 = Node("Mijn")
node2 = Node("naam")
node3 = Node("is")
node4 = Node("Riwaaz")
node5 = Node("Ranabhat")

doublefirst = node1.set_link_node(node2)
doublesecond = node2.set_link_node(node3)
doublethird = node3.set_link_node(node4)
doublefourth = node4.set_link_node(node5)

print(node4.get_link_node().get_value())