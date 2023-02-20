# Insertion Sort

def insertion_sort(list):
    for i in range(1, len(list)):
        current = element[i]
        j = i-1
        while j >= 0 and current < element[j]:
            element[j + 1] = element[j]
            j = j - 1
        element[j + 1] = current
            # temp = element[j]
            # element[j] = element[j + 1]
            # element[j + 1] = temp
            # j = j - 1
    return element


if __name__ == '__main__':
    element = [323, 46, 11, 45, 6, 89, 32, 43, 54]
    print(insertion_sort(element))

