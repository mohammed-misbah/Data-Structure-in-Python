class bst:
    def __init__(self, key):
        self.key = key
        self.lside = None
        self.rside = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lside:
                self.lside.insert(data)
            else:
                self.lside = bst(data)
        else:
            if self.rside:
                self.rside.insert(data)
            else:
                self.rside = bst(data)

    def search(self, data):
        if self.key == data:
            print("Your data is present")
            return
        if data < self.key:
            if self.lside:
                self.lside.search(data)
            else:
                print("Node is not present at tree")
        else:
            if self.rside:
                self.rside.search(data)
            else:
                print("Node is not present at tree")

    def preorder(self):
        print(self.key, end=",")
        if self.lside:
            self.lside.preorder()
        if self.rside:
            self.rside.preorder()

    def inorder(self):
        if self.lside:
            self.lside.inorder()
        print(self.key, end=",")
        if self.rside:
            self.rside.inorder()

    def postorder(self):
        if self.lside:
            self.lside.postorder()
        if self.rside:
            self.rside.postorder()
        print(self.key, end=",")

    def delete(self, data):
        if self.key is None:
            print("Tree is empty..!")
            return
        if data < self.key:
            if self.lside:
                self.lside = self.lside.delete(data)
            else:
                print("Node is not present")
        elif data > self.key:
            if self.rside:
                self.rside = self.rside.delete(data)
            else:
                print("Node is not present")
        else:
            if self.lside is None:  # while empty leaf node
                temp = self.rside
                self = None
                return temp
            if self.rside is None:   # while one leaf node
                temp = self.lside
                self = None
                return temp
            node = self.rside          # while two leaf node
            while node.lside is None:
                node = self.lside
            self.key = node.key
            self.rside = self.rside.delete(node.key)
        return self
    def min_node(self):
        current = self
        while current.lside:
            current = current.lside
        print("Node with smallest key is:", current.key)
    def max_node(self):
        current = self
        while current.rside:
            current = current.rside
        print("Node with largest key is:", current.key)
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lside)+count(node.rside)


root = bst(10)
list = [8, 23, 12, 6, 68, 39, 71]
for i in list:
    root.insert(i)
print("Count is", count(root))
print("Preorder is:")
root.preorder()
print("\n")
root.min_node()
root.max_node()
print("\nInorder is:")
root.inorder()
print("\nPostorder is:")
root.postorder()
print()
root.delete(71)
print("\n after deleting")
root.preorder()


# class bnrysrchtree:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
#
#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if data < self.key:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = bnrysrchtree(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = bnrysrchtree(data)
#
#     def search(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if data < self.key:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("Node is not present")
#         else:
#             if self.data:
#                 self.lchild.search(data)
#             else:
#                 print("Node is not is present")
#             return
#
#     def preorder(self):
#         print(self.key, end=" ")
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()
#
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.inorder()
#
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key, end=" ")
#
#     def delete(self, data):
#         if self.key is None:
#             print("Key is empty..!")
#             return
#         if data < self.lchild:
#             if self.lchild:
#                 self.lchild.delete(data)
#             else:
#                 print("data is not present")
#         else:
#             if data > self.rchild:
#                 if self.rchild:
#                     self.rchild.delete(data)
#             else:
#                 print("data is not present")
#             if self.lchild is None:
#                 temp = self.rchild
#                 self = None
#                 return temp
#             if self.rchild is None:
#                 temp = self.lchild
#                 self = None
#                 return temp
#             node = self.lchild
#             while self.lchild is None:
#                 node = self.rchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
#         return self
#
#     def min_heap(self):
#         current = self
#         while current.lside:
#             current = current.lchild
#         print("Node with smallest key is:", current.key)
#
#     def max_heap(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("Node with largest key is:", current.key)
#
#
# def counts(node):
#     if node is None:
#         return 0
#     return 1 + counts(node.lchild)+counts(node.rchild)
#
#
# roots = bnrysrchtree(8)
# list1 = [12, 45, 2, 21, 43]
# for i in list1:
#     roots.insert(i)
# print("Count is", counts(roots))
# print("preorder is")
# roots.preorder()


















































#     def delete(self, data, current):
#         if self.key is None:
#             print("Tree is empty..!")
#             return
#         if data < self.key:
#             if self.lside:
#                 self.lside = self.lside.delete(data, current)
#             else:
#                 print("Node is not present")
#         elif data > self.key:
#             if self.rside:
#                 self.rside = self.rside.delete(data, current)
#             else:
#                 print("Node is not present")
#         else:
#             if self.lside is None:  # while empty leaf node
#                 temp = self.rside
#                 if data == current:
#                     self.key = temp.key
#                     self.lside = temp.lside
#                     self.rside = temp.reside
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.rside is None:   # while one leaf node
#                 temp = self.lside
#                 if data == current:
#                     self.key = temp.key
#                     self.lside = temp.lside
#                     self.rside = temp.reside
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             node = self.rside          # while two leaf node
#             while node.lside is None:
#                 node = self.lside
#             self.key = node.key
#             self.rside = self.rside.delete(node.key, current)
#         return self
#
#
# def count(node):
#     if node is None:
#         return 0
#     return 1 + count(node.lside)+count(node.rside)
#
#
# root = bst(10)
# list = [2, 3]
# for i in list:
#     root.insert(i)
# print(count(root))
# if count(root)>1 :
#     root.delete(68)
# else:
#     print("cant delete")
# print("\n after deleting")
# root.preorder()
