# NOTE: numberList always be SORTED before using Binary Search

def binarySearchRecursive(numberList, numberToFind, start, end):
    if end < start:
        return -1
    
    mid = (start + end) // 2

    if mid >= len(numberList) or mid < 0:
        return -1
    
    midNumber = numberList[mid]

    if midNumber == numberToFind:
        return mid
    elif midNumber < numberToFind:
        start = mid + 1
    else:
        end = mid - 1

    return binarySearchRecursive(numberList, numberToFind, start, end)

if __name__ == '__main__':
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numberToFind = 9

    print(binarySearchRecursive(numberList, numberToFind, 0, len(numberList) - 1))