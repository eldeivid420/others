from Node import Node


class LinkedList:

    def __init__(self):
        self.first = None
        self.size = 0

    def append_value(self, new_value):
        node = Node(new_value)
        if self.size == 0:
            self.first = node
        else:
            current = self.first
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node

        self.size += 1
        return node

    def delete_value(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            while current.next_node.value is not value:
                if current.next_node is None:
                    return False
                else:
                    current = current.next_node

        deleted_node = current.next_node
        current.next_node = deleted_node.next

        self.size += 1
        return value

    def __len__(self):
        return self.size

    def __str__(self):
        string = "["
        current = self.first
        while current is not None:
            string += str(current)
            string += str(",")
            current = current.next_node
        string = string[:-1]
        string += "]"
        return string
