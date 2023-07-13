def linearSearch(numberList, numberToFind):
    for index, element in enumerate(numberList):
        if element == numberToFind:
            return index
        
    return -1

if __name__ == '__main__':
    numberList = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    numberToFind = 9

    print(linearSearch(numberList, numberToFind))