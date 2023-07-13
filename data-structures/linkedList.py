class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' => ' if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    def getLength(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count
    
    def insertAtBegin(self, data):
        self.head = Node(data, self.head)

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insertAt(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insertAtBegin(data)
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    def removeAt(self, index):
        if index < 0 or index > self.getLength():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insertValues(self, dataList):
        self.head = None

        for data in dataList:
            self.insertAtEnd(data)
        
linkedList = LinkedList()

linkedList.insertAtBegin(0)
linkedList.insertAtEnd(1)
linkedList.insertAt(1, 0.5)
linkedList.removeAt(2)

lst = [1, 2, 3, 4, 5]
linkedList.insertValues(lst)

linkedList.printLinkedList()

print(linkedList.getLength())