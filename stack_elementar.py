class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack(Node):
    def __init__(self):
        self.head = None

    def push(self, data):

        newNode = Node(data, self.head)
        
        self.head = newNode
        

    def pop(self):
        poppedData = self.next
        currentNode = self.head
        self.head = currentNode.next
        return poppedData.data
            
    def display(self):
        if self.head == None:
            print('List is empty')
            return
        
        elements = self.head

        while elements:

            print(elements.data)
            elements = elements.next
    
        print('------------------')

    def peek_elementar(self):
        peek = self.pop()
        self.push(peek)

        return peek

    def is_empty_elementar(self):
        if self.head == None:
            return 'list is empty'
        else:
            return 'list is not empty'

    def len_elementar(self):
        current_node = self.head
        aux_stack = Stack()
        count = 0

        while current_node:
            if current_node == None:
                count += 1
            else:
                aux_stack.push(self.pop())
                count += 1

        while aux_stack:
            self.push(aux_stack.pop())
        return count

        

        

stack = Stack()
stack.push(3)
stack.push(9)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(7)
stack.push(56)
stack.push(92)
stack.display()


print('peek: ' + str(stack.peek_elementar()))
print('is empty: ' + str(stack.is_empty_elementar()))
print('Len: ' + str(stack.len_elementar()))
print('hello')