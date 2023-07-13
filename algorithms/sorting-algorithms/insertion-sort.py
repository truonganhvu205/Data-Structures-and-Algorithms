def insertionSort(lst):
    for i in range(1, len(lst)):
        anchor = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > anchor:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = anchor

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    insertionSort(lst)

    print(lst)