class Pilha:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

        
    #Q2 pushWithClassLinkedList(e)
    def push(self, newData=None):
        if newData is None:
            return

        p1 = Pilha(self.data, self.next)

        self.data = newData
        self.next = p1
    
  
    # Q3 popWithClassLinkedList(e)
    def pop(self):
        if not self:
            return None
        
        poped = self.data
        
        #if not self.next:
        if self.next is None:
            self.data = None
            self.next = None
        else:
            self.data = self.next.data
            #self.next = None
            self.next = self.next.next
        return poped

    def esvazia_auxiliar(self, aux_stack):
        while aux_stack.data != None:
            self.push(aux_stack.pop())

    def display(self):
        aux = self
        elements = []
        while aux.data != None:

            elements.append(aux.data)
            aux = aux.next

        return elements

    def peek_A(self):
        valor = self.pop()
        self.push(valor)
        return valor

    def peek_B(self):
        return self.data
    
    def is_empty_A(self):
        aux = self.pop()

        if aux == None:
            return 'List is empty'
        else:
            self.push(aux)
            return 'List is not empty'


    def is_empty_B(self):
        if self.data == None:
            return 'List is empty'
        else:
            return 'List is not empty'
    
    def len_A(self):
        auxStack = Pilha()
        count = 0

        while self.data != None:
            auxStack.push(self.pop())
            count += 1

        while auxStack.data != None:
            self.push(auxStack.pop())

        return count

    def len_B(self):
        count = 0
        aux = self
        while aux.next != None:
            aux = aux.next
            count += 1
        
        return count

    def last_A(self):
        auxStack = Pilha()

        while self.data != None:
            auxStack.push(self.pop())

        last_element = auxStack.peek_A()

        self.esvazia_auxiliar(auxStack)

        return last_element

    def last_B(self):
        aux = self

        while aux.next.next:
            aux = aux.next
        return aux.data

    def get_value_by_index_A(self, index):
        count = 0
        aux_stack = Pilha()

        while index >= count:
            aux_stack.push(self.pop())
            count += 1

        value = aux_stack.peek_A()

        self.esvazia_auxiliar(aux_stack)
        return value

    def get_value_by_index_B(self, index):
        if index > self.len_B():
            return 'Range out of index'


        aux = self
        count = 0
        while index > count:
            aux = aux.next
            count +=1
        return aux.data

    def get_index_by_value_A(self, value):
        count = 0
        aux_stack = Pilha()

        while self.data != value:
            aux_stack.push(self.pop())
            count += 1

        self.esvazia_auxiliar(aux_stack)

        return count
    
    def get_index_by_value_B(self, value):
        count = 0
        aux = self

        while aux.data != value:
            aux = aux.next
            count += 1

        return aux.data

    def get_all_indexs_by_value_A(self, value):
        count = 0
        aux_stack = Pilha()
        array_of_indexs = []

        while self.data != None:
            if self.data == value:
                array_of_indexs.append(count)

            aux_stack.push(self.pop())
            count += 1

        self.esvazia_auxiliar(aux_stack)

        return array_of_indexs

    def get_all_indexs_by_value_B(self, value):
        count = 0
        aux = self
        array_of_indexs = []

        while aux.data != None:
            if aux.data == value:
                array_of_indexs.append(count)
            aux = aux.next
            count += 1

        return array_of_indexs


    def get_values_by_indexs_A(self, indexs):
        count = 0
        aux_stack = Pilha()
        array_of_values = []


        while self.data:
            if count in indexs:
                array_of_values.append(self.peek_A()) 
            aux_stack.push(self.pop())
            count += 1

        self.esvazia_auxiliar(aux_stack)

        return array_of_values
        



        
        



stack = Pilha()
for i in range(8):
    stack.push(i)

print(stack.display())

print(stack.peek_A())
print(stack.peek_B())

print(stack.is_empty_A())
print(stack.is_empty_B())

print(stack.len_A())
print(stack.len_B())

print(stack.last_A())
print(stack.last_B())

print(stack.display())

print(stack.get_value_by_index_A(3))
print(stack.get_value_by_index_B(3))

print(stack.display())

print(stack.get_index_by_value_A(5))
print(stack.get_index_by_value_A(5))


stack.push(2)
print(stack.display())

print(stack.get_all_indexs_by_value_A(2))
print(stack.get_all_indexs_by_value_B(2))

indexs = [2,4,5,7]
print(stack.get_values_by_indexs_A(indexs))




