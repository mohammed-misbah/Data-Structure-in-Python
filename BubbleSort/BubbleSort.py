# Bubble Sort Example 1

# def bubble_sort(list):
#     size = len(list)
#
#     for i in range(size-1):
#         for j in range(size-1):
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#
#
# if __name__ == '__main__':
#     element = [2, 54, 23, 1, 56, 3, 78, 34]
#     # list = ['misbah', 'rena', 'zaid', 'ajmal', 'yasin', 'badar']
#     bubble_sort(element)
#     print(element)

# Bubble Sort Example 2


# def bubble_sort(element, key=None):
#     size = len(element)
#
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1):
#             if element[j][key] > element[j+1][key]:
#                 temp = element[j]
#                 element[j] = element[j+1]
#                 element[j+1] = temp
#                 swapped = True
#         if not swapped:
#             break
#
#
# if __name__ == '__main__':
#     list = [{'name': 'roy', 'amount': '100000', 'device': 'IphoneXS'},
#             {'name': 'john', 'amount': '40000', 'device': 'OnePlus'},
#             {'name': 'arun', 'amount': '85000', 'device': 'Samsung S20 Ultra'}
#             ]
#     bubble_sort(list, key='name')
#     print(list)

# Bubble sort using Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.nref:
            last_node = last_node.nref
        last_node.nref = new_node

    def bubble_sort(self):
        if self.head is None:
            return
        while True:
            current = self.head
            swapped = False
            while current.nref:
                if current.data > current.nref.data:
                    current.data, current.nref.data = current.nref.data, current.data

                    swapped = True
                current = current.nref
            if not swapped:
                break

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nref


BS = Linkedlist()
BS.append(34)
BS.append(56)
BS.append(45)
BS.append(23)
BS.append(67)
BS.bubble_sort()
BS.print_list()



