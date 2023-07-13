class binarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = binarySearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = binarySearchTree(data)

    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)

        return self
    
    def findMax(self):
        if self.right is None:
            return self.data
        else:
            return self.right.findMax()
        
    def findMin(self):
        if self.left is None:
            return self.data
        else:
            return self.left.findMin()
        
def buildTree(elements):
    root = binarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    numbersTree = buildTree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbersTree.inOrderTraversal())

    numbersTree.delete(20)
    print('After deleting 20:', numbersTree.inOrderTraversal())

    print(numbersTree.search(20))