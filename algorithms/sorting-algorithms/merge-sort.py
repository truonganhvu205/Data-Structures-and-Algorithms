def mergeTwoSort(lstOne, lstTwo, lstThree):
    i = j = k = 0

    while i < len(lstOne) and j < len(lstTwo):
        if lstOne[i] <= lstTwo[j]:
            lstThree[k] = lstOne[i]
            i += 1
        else:
            lstThree[k] = lstTwo[j]
            j += 1

        k += 1

    while i < len(lstOne):
        lstThree[k] = lstOne[i]
        i += 1
        k += 1

    while j < len(lstTwo):
        lstThree[k] = lstTwo[j]
        j += 1
        k += 1

def mergeSort(lst):
    if len(lst) <= 1:
        return
    
    mid = len(lst) // 2
    start = lst[:mid]
    end = lst[mid:]

    mergeSort(start)
    mergeSort(end)

    mergeTwoSort(start, end, lst)

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    mergeSort(lst)

    print(lst)