def selectionSort(lst):
    for i in range(len(lst) - 1):
        minIndex = i

        for j in range(minIndex + 1, len(lst)):
            if lst[minIndex] > lst[j]:
                minIndex = j

        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    selectionSort(lst)

    print(lst)