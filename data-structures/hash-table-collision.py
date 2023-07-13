class HashTableCollision:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def getHash(self, key):
        hash = 0

        for char in key:
            hash += ord(char)

        return hash % self.MAX

    def __getitem__(self, key):
        h = self.getHash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True

        if not found:
            self.arr[h].append((key, value))
            
    def __delitem__(self, key):
        h = self.getHash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print('del', index)
                
                del self.arr[h][index]

hashTableCollision = HashTableCollision()

# getHash()
print(hashTableCollision.getHash('march 6'))
print(hashTableCollision.getHash('march 17'))

# __setitem__
hashTableCollision['march 5'] = 12
hashTableCollision['march 6'] = 23
hashTableCollision['march 17'] = 34
hashTableCollision['march 8'] = 45
hashTableCollision['march 9'] = 56

# __getitem__
print(hashTableCollision.arr)

print(hashTableCollision['march 6'])
print(hashTableCollision['march 17'])

# __delitem__
del hashTableCollision['march 17']
print(hashTableCollision.arr)