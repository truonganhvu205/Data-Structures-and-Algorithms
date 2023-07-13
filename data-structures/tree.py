class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level
    
    def printTree(self):
        space = ' ' * self.getLevel() * 4
        prefix = space + '|__' if self.parent else ''

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.printTree()

def buildTree():
    root = Tree('Electronics')

    laptop = Tree('Laptop')
    laptop.addChild(Tree('Dell'))
    laptop.addChild(Tree('Lenovo'))
    laptop.addChild(Tree('Macbook'))

    cellphone = Tree('Cellphone')
    cellphone.addChild(Tree('Samsung'))
    cellphone.addChild(Tree('iPhone'))
    cellphone.addChild(Tree('Xiaomi'))

    root.addChild(laptop)
    root.addChild(cellphone)

    root.printTree()

if __name__ == '__main__':
    buildTree()