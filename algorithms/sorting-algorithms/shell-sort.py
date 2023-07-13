def shellSort(lst):
    gap = len(lst) // 2

    while gap > 0:
        for i in range(gap, len(lst)):
            anchor = lst[i]
            j = i

            while j >= 0 and lst[j - gap] > anchor:
                lst[j] = lst[j - gap]
                j -= gap

            lst[j] = anchor
        gap //= 2

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    shellSort(lst)

    print(lst)