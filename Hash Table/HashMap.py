# # Hash Map Example
# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.arr = [[] for i in range(self.Max)]
#     def gethash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.Max
#     def setitem(self, key, value):
#         h = self.gethash(key)
#         self.arr[h] = value
#     def getitem(self, key):
#         h = self.gethash(key)
#         return self.arr[h]
#     def delitem(self, key):
#         h = self.gethash(key)
#         self.arr[h] = None
# ht = HashTable()
# ht.setitem('name', 'mizbah')
# print(ht.getitem('name'))


# Hash Table Collision Example

# class HashTable:
#     def __init__(self):
#         self.size = 100
#         self.arr = [[] for _ in range(self.size)]
#
#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.size
#
#     def getitem(self, key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
#
#     def setitem(self, key, value):
#         h = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key, value)
#                 found = True
#                 break
#         if not found:
#             self.arr[h].append((key, value))
#
#     def delitem(self, key):
#         h = self.get_hash(key)
#         for idx, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h]
#
#
# HT = HashTable()
# HT.setitem('nike', 7000)
# HT.setitem('adidas', 4000)
# HT.setitem('puma', 3000)
# HT.setitem('woodland', 5000)
# print(HT.getitem('nike'))
# print(HT.getitem('woodland'))
# print(HT.delitem('nike'))


# Hash Table


# class hashtable:
#     def __init__(self):
#         self.size = 100
#         self.bucket = [None for i in range(self.size)]

#     def get_hashtable(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self.get_hashtable(key)
#         self.bucket[index].append((key, value))

#     def find(self, key):
#         index = self.get_hashtable(key)
#         bucket = self.bucket[index]
#
#         for idx, elmnt in bucket:
#             if idx == key:
#                 return elmnt

#         return None


# ht = hashtable()
# ht.insert('march', 122)
# print(ht.find('march'))

class hashtable:
    def __init__(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = ord(char)
        return h % self.size

    def getitem(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def setitem(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[idx][h] = (key, value)
            found = True
            break
        if not found:
            self.arr[h].append((key, value))


ht = hashtable()
ht.setitem('misbah', '20')
print((ht.getitem('misbah')))


