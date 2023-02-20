# Binary Search
position = -1
def binary_search(list, x):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2
        if list[mid] == x:
            globals()['position'] = mid
            return x
        else:
            if list[mid] < x:    # If x is greater, ignore left half
                low = mid + 1
            elif list[mid] > x:  # If x is smaller, ignore right half
                high = mid - 1
            else:    # x is present at mid
                return mid     # If we reach here, then the element was not present
    return -1


list = [2, 3, 4, 10, 40]
x = 10
if binary_search(list, x):
    print("Element is present at position:", position)
else:
    print("Element is not present in array")
