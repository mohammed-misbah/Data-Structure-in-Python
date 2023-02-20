# Selection Sort Example 1
def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        if i != min_index:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
            # array[i], array[minimum_index] = array[minimum_index], array[i]


if __name__ == '__main__':
    elements = [23, 2, 4, 56, 26, 65, 12, 45]
    selection_sort(elements)
    print(elements)

# Selection Sort Example 2


def selection_sort(arr, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for i in range(len(arr)):
            min_index = i
            for j in range(i, len(arr)):
                if arr[j][sort_by] < arr[min_index][sort_by]:
                    min_index = j
            if i != min_index:
                temp = arr[i]
                arr[i] = arr[min_index]
                arr[min_index] = temp


if __name__ == '__main__':
    elements = [
        {'first_name': 'mohammed', 'last_name': 'misbah'},
        {'first_name': 'arman',    'last_name': 'malik'},
    ]
    selection_sort(elements, ['first_name', 'last_name'])
    print(*elements, sep='\n')


