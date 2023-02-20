# Merge Sort
def merge_sort(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


if __name__ == '__main__':
    x = [15, 4, 12, 23, 9, 10]
    y = [5, 67, 28, 10, 32, 31]
    print(merge_sort(x, y))

#  Sorting a Single array


def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)
    return merge_sort(left, right)


def merge_sort(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


if __name__ == '__main__':
    elements = [15, 4, 12, 23, 9, 10]
    print(merge(elements))


# Merge Sort with a key elements


# def merge_sort(elements, key, descending):
#     size = len(elements)
#
#     if size == 1:
#         return elements
#
#     left_list = merge_sort(elements[0:size // 2], key, descending)
#     right_list = merge_sort(elements[size // 2:], key, descending)
#     sorted_list = merge(left_list, right_list,    key, descending)
#
#     return sorted_list
#
#
# def merge(left_list, right_list, key, descending=False):
#     merged = []
#     if descending:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] >= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))
#     else:
#         while len(left_list) > 0 and len(right_list) > 0:
#             if left_list[0][key] <= right_list[0][key]:
#                 merged.append(left_list.pop(0))
#             else:
#                 merged.append(right_list.pop(0))
#
#     merged.extend(left_list)
#     merged.extend(right_list)
#     return merged
#
#
# if __name__ == '__main__':
#     elements = [
#         {'name': 'ram....',  'age': '28', 'time_hours': '5'},
#         {'name': 'maya...', 'age': '23', 'time_hours': '8'},
#         {'name': 'priya..', 'age': '20', 'time_hours': '12'},
#         {'name': 'abinav.', 'age': '25', 'time_hours': '8'},
#     ]
#     print(merge_sort(elements, key='name', descending=False))
#







