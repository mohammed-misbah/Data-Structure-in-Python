# Linear Search
position = -1


def linear_search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['position'] = i
            return True
        i = i + 1
    return False


list = [34, 56, 4, 65, 5, 43, 2, 36, 7, 76]
n = 36
if linear_search(list, n):
    print("item is found at position:", +position)
else:
    print("item is not found..!")

