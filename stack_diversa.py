


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):

        newNode = Node(data, self.head)
        
        self.head = newNode
        

    def pop(self):
        poppedData = self.head

        self.head = self.head.next
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
    def peek_d(self):
        elements = self.head

        while elements.next:
            elements = elements.next
        return elements.data

    def is_empty_diversa(self):
        if self.head == None:
            return 'List is empty'
        else:
            return 'List is not empty'

    def len_d(self):
        count = 0
        elements = self.head

        while elements:
            count += 1
            elements = elements.next
        return count
    
    def last_d(self):

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next
        return currentNode.data

    def get_value_by_index_d(self, index):

        count = 0
        currentNode = self.head

        while count != index:
            
            if currentNode.next == None:
                return currentNode.data

            currentNode = currentNode.next
            count =+ 1
            

        return currentNode.data

    def get_index_by_value_d(self, value):
        count = 0
        currentNode = self.head

        while currentNode:
            if currentNode.data == value:
                return count

            currentNode = currentNode.next
            count += 1
        return 'Valor não encontrado'

    def get_all_index_by_value_d(self, value):
        count = 0
        currentNode = self.head
        arrayOfIndex = []
        
        while currentNode:
            if currentNode.data == value:
                arrayOfIndex.append(count)

            currentNode = currentNode.next
            count += 1

        if arrayOfIndex == []:
            return 'Nenhum índice foi encontrado'
        return arrayOfIndex

    def get_value_by_indexs_d(self, indexes):
        currentNode = self.head
        count = 0
        arrayOfValues = []

        while currentNode:
            if count in indexes:
                arrayOfValues.append(currentNode.data)
            currentNode = currentNode.next

            count += 1
        return arrayOfValues

    def get_values_by_slice_d(self, ii, fi):
        count = 0
        currentNode = self.head
        arrayOfValues = []

        while currentNode:
            if count == ii:
                while fi >= count:
                    arrayOfValues.append(currentNode.data)

                    currentNode = currentNode.next
                    count += 1
            currentNode = currentNode.next
            count += 1
        return arrayOfValues

    def remove_all_d(self):
        self.head = None

    def remove_by_index_d(self, index):

        count = 0
        currentNode = self.head

        while count != (index - 1):
            currentNode = currentNode.next
            count += 1
            
        currentNode.next = currentNode.next.next
        
    def remove_by_value(self, value):
        currentNode = self.head

        while currentNode.data != value:
            currentNode = currentNode.next
            
        

    
    


        

stack = Stack()

stack.display()
stack.push(3)
stack.push(9)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(7)
stack.push(56)
stack.push(92)

stack.display()
print('\nPeek_d: ' + str(stack.peek_d()))
print('Lenght_d: ' + str(stack.len_d()))
print('Last_d: ' + str(stack.last_d()))

print('getValueByIndex: ' + str(stack.get_value_by_index_d(2)))
print('getIndexByValue: ' + str(stack.get_index_by_value_d(3)))
print('getAllIndexByValue: ' + str(stack.get_all_index_by_value_d(3)))
print('getValuesByIndexs' + str(stack.get_value_by_indexs_d([1, 3, 5])))
print('getValuesBySlice: ' + str(stack.get_values_by_slice_d(2, 5)))
print('pop: ' + str(stack.pop()))
stack.remove_all_d()
stack.display()

stack.push(3)
stack.push(9)
stack.push(5)
stack.push(7)
stack.push(4)
stack.push(7)
stack.push(56)
stack.push(92)
stack.display()

stack.remove_by_index_d(2)
stack.remove_by_value(92)
stack.display()





##print('getValueByIndex: ' + str(stack.getValueByIndex(3)))

