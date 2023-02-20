# Binary Search
position = -1


def binary_search(list, x):

    lower = 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == x:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < x:
                mid + 1
            elif list[mid] > x:
                mid - 1


list[3, 53, 62, 75, 87, 90]
x = 87
if binary_search(list, x):
    print("Given number found at", position)
else:
    print("item is not found in a list..!")
