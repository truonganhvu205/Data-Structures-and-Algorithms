# Hoare Partition

def swap(lst, a, b):
    if a != b:
        lst[a], lst[b] = lst[b], lst[a]

def partition(lst, start, end):
    pivotIndex = start
    pivot = lst[pivotIndex]

    while start <= end:
        while start < len(lst) and lst[start] <= pivot:
            start += 1
        while lst[end] > pivot:
            end -= 1

        if start < end:
            swap(lst, start, end)

    swap(lst, pivotIndex, end)
    return end

def quickSort(lst, start, end):
    if start < end:
        p = partition(lst, start, end)
        quickSort(lst, start, p - 1)
        quickSort(lst, p + 1, end)

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    quickSort(lst, 0, len(lst) - 1)

    print(lst)