class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode
        return

    def display(self):
        if self.head == None:
            print('list is empty')
        
        contents = self.head

        while contents:
            print(contents.data)
            contents = contents.next
        print('---------------')

        


linkedList = LinkedList()

linkedList.display()
linkedList.append(3)
linkedList.append(5)
linkedList.append(7)
linkedList.display()
