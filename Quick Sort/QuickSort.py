# Quick Sort Example
# def swap(x, y, array):
#     if x != y:
#         temp = array[x]
#         array[x] = array[y]
#         array[y] = temp
#
#
# def partition(element, start, end):
#     pivot_index = start           # pivot index = 0
#     pivot = element[pivot_index]  # pivot = 11
#     while start < end:
#         if start < len(element) and element[start] <= pivot:
#             start += 1
#
#         if element[end] > pivot:
#             end -= 1
#
#         if start < end:
#             swap(start, end, element)
#
#     swap(pivot_index, end, element)
#     return end
#
#
# def quick_sort(element, start, end):
#     if start < end:
#         pi = partition(element, start, end)
#         quick_sort(element, start, pi-1)  # left partition
#         quick_sort(element, end, pi+1)   # right partition
#
#
# if __name__ == '__main__':
#     elements = [11, 4, 5, 45, 24, 36]
#     quick_sort(elements, 0, len(elements)-1)
#     print(elements)


# Quick Sort Using Linkedlist


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None
#
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         new_node.nref = self.head
#         self.head = new_node
#
#     def quick_sort_helper(self, start, end):
#         if start == end:
#             return
#         left = start
#         right = start.nref
#         pivot = start.data
#
#         while right != left:
#             if right.nref < pivot:
#                 left = left.nref
#                 temp = right.data
#                 right.data = left.data
#                 left.data = temp
#             right = right.nref
#
#         self.quick_sort_helper(start, left)
#         self.quick_sort_helper(left.nref, end)
#
#     def quick_sort(self):
#         self.quick_sort_helper(self.head, None)
#
#
# qs = Linkedlist()
# qs.append(23)
# qs.append(45)
# qs.append(34)
# qs.append(78)
# qs.append(39)
#
# qs.quick_sort()
#
#
#
#
#
#
def swap(a, b, array):
    if a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp


def quicksort(element, start, end):
    pivot_index = start
    pivot = element[pivot_index]
    while start < end:
        if start < len(element) and element[start] <= pivot:
            start += 1
        if element[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, element)

    swap(pivot_index, end, element)
    return end


def quick(element, start, end):
    if start < end:
        pi = quicksort(element, start, end)
        quicksort(element, start, pi - 1)
        quicksort(element, end, pi+1)


if __name__ == '__main__':
    list = [12, 45, 32, 21, 5, 2]
    quick(list, 0, len(list)-1)
    print(list)





