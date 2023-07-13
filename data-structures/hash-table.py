class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.getHash(index)
        return self.arr[h]
    
    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.getHash(key)
        self.arr[h] = None

hashTable = HashTable()

# __setitem__
hashTable['march 6'] = 12
hashTable['march 7'] = 23

print(hashTable.arr)

# __getitem__
print(hashTable['march 6'])

# __delitem__
del hashTable['march 7']

print(hashTable.arr)