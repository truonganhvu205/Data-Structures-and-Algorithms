# NOTE: numberList always be SORTED before using Binary Search

def binarySearch(numberList, numberToFind):
    start = 0
    end = len(numberList) - 1

    while start <= end:
        mid = (start + end) // 2
        midNumber = numberList[mid]

        if midNumber == numberToFind:
            return mid
        elif midNumber < numberToFind:
            start = mid + 1
        else:
            end = mid - 1

    return -1

if __name__ == '__main__':
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numberToFind = 9

    print(binarySearch(numberList, numberToFind))