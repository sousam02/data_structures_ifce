
class Stack_array:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return
        return self.stack.pop()
        
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

    def get_values_by_indexs_B(self, indexs):
        count = 0
        aux = self
        array_of_values = []

        while aux.data:
            if count in indexs:
                array_of_values.append(aux.data)
            aux = aux.next
            count += 1

        return array_of_values
        

    def get_values_by_slice_A(self, start, end):
        array_of_values = []
        count = 0
        aux_stack = Pilha()

        while self.data:
            if count == start:
                while count <= end:
                    array_of_values.append(self.data)
                    aux_stack.push(self.pop())
                    count += 1
            aux_stack.push(self.pop())
            count += 1

        self.esvazia_auxiliar(aux_stack)

        return array_of_values
    
    def get_values_by_slice_B(self, start, end):
        count = 0
        aux = self
        array_of_values = []

        while aux:
            if count == start:
                while count <= end:
                    array_of_values.append(aux.data)
                    aux = aux.next
                    count += 1

            aux = aux.next
            count += 1
        return array_of_values
        
    def remove_all_A(self):
        while self.next:
            self.pop()
       
    def remove_all_B(self):
        while self.data != None:
            self.data = self.next.data
            self.next = self.next.next

    def remove_by_index_A(self, index):
        aux_stack = Pilha()
        count = 0

        while index > count:
            aux_stack.push(self.pop())
            count += 1

        self.pop()

        self.esvazia_auxiliar(aux_stack)
    
    def remove_by_index_B(self, index):
        count = 0
        aux_stack = Pilha()
        #encontra o elemento de acordo com o index
        while index > count:
            p1 = Pilha(aux_stack.data, aux_stack.next)
                
            aux_stack.data = self.data
            aux_stack.next = p1
            self.data = self.next.data
            self.next = self.next.next
            count += 1
        self.data = self.next.data
        self.next = self.next.next

        #volta os elementos para a stack original
        while aux_stack.data:
            p1 = Pilha(self.data, self.next)

            self.data = aux_stack.data
            self.next = p1
            aux_stack.data = aux_stack.next.data
            aux_stack.next = aux_stack.next.next

    def remove_by_value_A(self, value):
        aux_stack = Pilha()
        
        while self.data != value:
            aux_stack.push(self.pop())
        self.pop()

        self.esvazia_auxiliar(aux_stack)

    def remove_by_value_B(self, value):

        aux_stack = Pilha()

        while self.data != value:
            p1 = Pilha(aux_stack.data, aux_stack.next)
                
            aux_stack.data = self.data
            aux_stack.next = p1
            self.data = self.next.data
            self.next = self.next.next
        self.data = self.next.data
        self.next = self.next.next

        while aux_stack.data:
            p1 = Pilha(self.data, self.next)

            self.data = aux_stack.data
            self.next = p1
            aux_stack.data = aux_stack.next.data
            aux_stack.next = aux_stack.next.next

    def remove_all_by_value_A(self, value):
        aux_stack = Pilha()

        while self.data != None:
            if self.data == value:
                self.pop()
            aux_stack.push(self.pop())
        
        self.esvazia_auxiliar(aux_stack)

    def remove_all_by_value_B(self, value):

        aux_stack = Pilha()

        while self.data != None:
            if self.data == value:
                self.data = self.next.data
                self.next = self.next.next

            p1 = Pilha(aux_stack.data, aux_stack.next)             
            aux_stack.data = self.data
            aux_stack.next = p1
            self.data = self.next.data
            self.next = self.next.next     

        while aux_stack.data != None:
            p1 = Pilha(self.data, self.next)

            self.data = aux_stack.data
            self.next = p1
            aux_stack.data = aux_stack.next.data
            aux_stack.next = aux_stack.next.next

    
    def remove_all_by_indexes_A(self, indexes):
        aux_stack = Pilha()
        count = 0
        while self.data != None:
            aux_stack.push(self.pop())
            if count in indexes:
                aux_stack.pop()
            
            count += 1

        self.esvazia_auxiliar(aux_stack)

    def remove_all_by_indexes_B(self, indexes):
        aux_stack = Pilha()
        count = 0

        while self.data != None:
            p1 = Pilha(aux_stack.data, aux_stack.next)             
            aux_stack.data = self.data
            aux_stack.next = p1
            self.data = self.next.data
            self.next = self.next.next
            if count in indexes:
                aux_stack.data = aux_stack.next.data
                aux_stack.next = aux_stack.next.next
            count += 1
        
        while aux_stack.data != None:
            p1 = Pilha(self.data, self.next)

            self.data = aux_stack.data
            self.next = p1
            aux_stack.data = aux_stack.next.data
            aux_stack.next = aux_stack.next.next
            
    def remove_all_by_slice_A(self, inicio, final):
        aux_stack = Pilha()
        count = 0
        while self.data != None:
            if count == inicio:
                while final >= count:
                    self.pop()
                    count += 1
            aux_stack.push(self.pop())
            count += 1

        self.esvazia_auxiliar(aux_stack)

    def remove_all_by_slice_B(self, inicio, final):
        aux_stack = Pilha()
        count = 0

        while self.data != None:
            if count == inicio:
                while final >= count:
                    self.data = self.next.data
                    self.next = self.next.next
                    count += 1
            p1 = Pilha(aux_stack.data, aux_stack.next)
                
            aux_stack.data = self.data
            aux_stack.next = p1
            self.data = self.next.data
            self.next = self.next.next
            count += 1
        
        while aux_stack.data != None:
            p1 = Pilha(self.data, self.next)

            self.data = aux_stack.data
            self.next = p1
            aux_stack.data = aux_stack.next.data
            aux_stack.next = aux_stack.next.next

        

            
            


def popular_pilha(stack):
    for i in range(8):
        stack.push(i)



stack = Pilha()
popular_pilha(stack)

print(stack.display())
print('PEEK')
print(stack.peek_A())
print(stack.peek_B())

#---------------------------------------------------------
print('\nis_empty')
print(stack.is_empty_A())
print(stack.is_empty_B())

#---------------------------------------------------------
print('\nLen')
print(stack.len_A())
print(stack.len_B())

#---------------------------------------------------------
print('\nLast')
print(stack.last_A())
print(stack.last_B())

print(stack.display())

#---------------------------------------------------------
print('\nget_value_by_index')
print(stack.get_value_by_index_A(3))
print(stack.get_value_by_index_B(3))

print(stack.display())
#---------------------------------------------------------
print('\nget_index_by_value')
print(stack.get_index_by_value_A(5))
print(stack.get_index_by_value_A(5))

#------------------------------------------------------
print('\nget_all_indexs_by_value')
stack.push(2)
print(stack.display())
print(stack.get_all_indexs_by_value_A(2))
print(stack.get_all_indexs_by_value_B(2))
#------------------------------------------------------
print('\nget_values_by_indexs')
indexs = [2,4,5,7]
print(stack.get_values_by_indexs_A(indexs))
print(stack.get_values_by_indexs_B(indexs))

print(stack.display())
#------------------------------------------------------
print('\nget_values_by_slice')
print(stack.get_values_by_slice_A(2, 5))
print(stack.get_values_by_slice_B(2, 5))

print(stack.display())
#------------------------------------------------------
print('\nremove_all')
stack.remove_all_A()
print(stack.display())

popular_pilha(stack)
print(stack.display())

stack.remove_all_B()
print(stack.display())
#------------------------------------------------------
print('\nremove_by_index')
popular_pilha(stack)
print(stack.display())
stack.remove_by_index_A(3)
print(stack.display())
stack.remove_by_index_B(3)

print(stack.display())
#------------------------------------------------------
print('\nremove_by_value')
stack.remove_by_value_A(6)
print(stack.display())

stack.remove_by_value_B(1)
print(stack.display())
#----------------------------------------------------
popular_pilha(stack)
print(stack.display())
#------------------------------------------------------
print('\nremove_all_by_value')
stack.remove_all_by_value_A(7)
stack.remove_all_by_value_B(5)
print(stack.display())

#---------------------------------------------------
print('\nremove_all_by_indexes')
array_of_indexes = [1, 2, 4]
stack.remove_all_by_indexes_A(array_of_indexes)
print(stack.display())

array_of_indexes = [1, 2, 4]
stack.remove_all_by_indexes_B(array_of_indexes)
print(stack.display())
#--------------------------------------------------
popular_pilha(stack)
print(stack.display())
#------------------------------------------------------
print('\nremove_all_by_slice')
stack.remove_all_by_slice_A(3,6)
print(stack.display())
#--------------------------------------------------
popular_pilha(stack)
print(stack.display())
#------------------------------------------------------
stack.remove_all_by_slice_B(3,6)
print(stack.display())
#--------------------------------------------------






