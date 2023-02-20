# Doubly Linked List Examples
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class doublelinkedlist:
    def __init__(self):
        self.head = None
        self.nref = None
        self.pref = None

    # Traversing the Node:

    def print_dl_forward(self):
        if self.head is None:
            print("The given double linked list is Empty..!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def print_dl_reverse(self):
        print()
        if self.head is None:
            print("The given double linked list is Empty..!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref

    # Adding at Empty Node

    # def insert_empty(self, data):
    #     if self.head is None:
    #         new_node = Node(data)
    #         self.head = new_node
    #     else:
    #         print("The given node is empty..!")

    # Add at beginning of a linked list

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Add at end of the linked list

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, X):
        if self.head is None:
            print("The given Node is Empty..!")
        else:
            n = self.head
            while n is not None:
                if X == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in double linked list..!")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("The given list is empty..!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present in linked list..!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.nref
                if n.pref is not None:
                    n.pref.nref = new_node
                # else:
                #     self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("The given linked list is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("The given linked list id  empty..!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the node")
        else:
            n = self.head
            while n is not None:  # n will reached end position
                n = n.nref
            n.pref.nref = None


ll = doublelinkedlist()
# ll.insert_empty(23)
ll.add_begin(30)
ll.add_begin(50)
ll.add_begin(45)
ll.add_begin(34)
ll.add_end(50)
# ll.print_dl_reverse()
# ll.add_after(100, 30)
# ll.add_before(200, 30)
# ll.print_dl_forward()
# ll.print_dl_reverse()

# def del_by_value(self, x):
#     if self.head is None:
#         print("The given linked list id  empty..!")
#     else:
#         n = self.nref
#         while x is not None:
#             if x == n.data:
#                 break
#             n = n.nref
#         if n is not None:
#             print("The give ddl is Empty..!")

