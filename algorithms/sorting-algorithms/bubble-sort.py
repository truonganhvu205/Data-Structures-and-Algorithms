def bubbleSort(lst):
    for i in range(len(lst) - 1):
        swapped = False

        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    bubbleSort(lst)

    print(lst)