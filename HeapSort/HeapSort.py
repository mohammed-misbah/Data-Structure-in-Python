# Min-Heap
# def heapify(arr, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     if left < n and arr[i] > arr[left]:
#         smallest = left
#     if right < n and arr[i] > arr[right]:
#         smallest = right
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         heapify(arr, n, smallest)


# def insert(array, newnum):
#     size = len(array)
#     if size == 0:
#         array.append(newnum)
#     else:
#         array.append(newnum)
#         for i in range((size // 2) - 1, -1, -1):
#             heapify(arr, size, i)


# def deletenode(array, num):
#     size = len(array)
#     for i in range(0, size):
#         if num == array[i]:
#             break
#     array[i], array[size - 1] = array[size - 1], array[i]
#     array.remove(num)
#     for i in range((size // 2) - 1, -1, -1):
#         heapify(array, len(array), i)

# arr = []
# insert(arr, 4)
# insert(arr, 5)
# insert(arr, 10)
# insert(arr, 15)
# insert(arr, 2)
# insert(arr, 23)
# insert(arr, 3)
# insert(arr, 19)
# print("Min-Heap array: ", str(arr))

# deletenode(arr, 15)
# print("\n\nAfter deletion: ", str(arr))


# Max-Heap
def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[i] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)


def insert(array, newnode):
    size = len(array)
    if size == 0:
        array.append(newnode)
    else:
        array.append(newnode)
        for i in range((size // 2)-1, -1, -1):
            heapify(arr, size, i)


def delete(array, num):
    size = len(array)
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(num)
    for i in range((size // 2)-1, -1, -1):
        heapify(array, len(array), i)


arr = []
insert(arr, 1)
insert(arr, 3)
insert(arr, 36)
insert(arr, 73)
insert(arr, 21)
insert(arr, 12)
insert(arr, 43)
insert(arr, 25)

print("Min Heap      :", str(arr))

delete(arr, 12)
print("\nAfter deletion:", str(arr))

# Heap Sort


def heapify(arr, size, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 1

    if left < size and arr[left] > arr[smallest]:
        smallest = left
    if right < size and arr[left] > arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, size, smallest)


def heapsort(arr, size):
    for i in range((size // 2)-1, -1, -1):
        heapify(arr, size, i)
    for i in range(size-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def printarray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


arr = [4, 5, 8, 12, 9]
n = len(arr)
heapsort(arr, n)
print("The sorted array is:")
printarray(arr, n)



