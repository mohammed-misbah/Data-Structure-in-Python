# This means a created the node data->[10]ref OR adrss->[None]
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None
        self.ref = None

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    # Add at Beginning
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_between(self, data, X):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n is not None:
            if X == n.data:
                break
            n = self.ref
            if n is None:
                print("Node is Empty")
            else:
                new_node.ref = n.ref
                n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty so we can't delete nodes")
        else:
            self.head = self.head.ref

    def delete_by_value(self, x):
        # if self.head is None:
        #     print("Cant delete Linked List is Empty")
        #     return
        if x == self.head.data:  # data of the first node
            self.head = self.head.ref  # ref of the 2nd has to store 1st head
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is empty")
        else:
            n.ref = n.ref.ref


ll = linkedlist()
ll.add_begin(30)
ll.add_begin(40)
ll.add_end(50)
ll.add_between(30 ,100)
ll.delete_by_value(30)
ll.delete_begin()
ll.print_LL()
