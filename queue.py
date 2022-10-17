import numpy as np
class Queue:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def insert(self, new_data):
        if new_data is None:
            return

        f = Queue(new_data, None)

        if self.data == None:
            self.data = new_data
            return
        
        filaAux = self #copia
        while filaAux.next is not None:
            filaAux = filaAux.next

        filaAux.next = f

    def remove(self):
        removed_data = self.data
        if self.next == None:
            self.data = None
            return removed_data
        self.data = self.next.data
        self.next = self.next.next

        return removed_data
    
    def rebuild_queue(self, array):
        self.remove_all_d()

        if self.data == None:
            self.data = array[0]
        for i in range(1, len(array)):
            f = Queue(array[i], None)

            aux_queue = self

            while aux_queue.next != None:
                aux_queue = aux_queue.next
            
            aux_queue.next = f

    def self_to_aux(self, aux_queue):
        while self.data != None:
            aux_queue.insert(self.remove())

    #put the values back to self queue
    def aux_to_self(self, aux_queue):
        while aux_queue.data != None:
            self.insert(aux_queue.remove())
    def array_conversion(self):
        fila = []
        fila_aux = self #copia
        while fila_aux is not None:
            fila.append(fila_aux.data)
            fila_aux = fila_aux.next
        return fila

    def first_c(self):
        aux_queue = Queue()
        aux_queue.insert(self.remove())
        first_element = aux_queue.data

        while self.data != None:
            aux_queue.insert(self.remove())
        while aux_queue.data != None:
            self.insert(aux_queue.remove())
        
        return first_element

    def first_d(self):
        return self.data


    def is_empty_c(self):
        aux_queue = Queue()
        aux_queue.insert(self.remove())
        verify_empty = aux_queue.data

        if verify_empty == None:
            return 'Queue is empty'
        else:
            while self.data != None:
                aux_queue.insert(self.remove())
            while aux_queue.data != None:
                self.insert(aux_queue.remove())
            return 'Queue is not empty'
            
    
    def is_empty_d(self):
        if self.data == None:
            return 'Queue is empty'
        else:
            return 'Queue is not empty'


    def len_c(self):
        count = 0
        aux_queue = Queue()

        while self.data != None:
            count += 1

            aux_queue.insert(self.remove())

        while aux_queue.data != None:
            self.insert(aux_queue.remove())

        return count

    def len_d(self):
        count = 0
        aux = self

        while aux != None:
            aux = aux.next
            count += 1

        return count

    def last_c(self):
        aux_queue = Queue()

        while self.data != None:
            last_element = self.remove()
            aux_queue.insert(last_element)

        while aux_queue.data != None:
            self.insert(aux_queue.remove())
        return last_element

    def last_d(self):
        array = self.array_conversion()
        return array[-1]

    
    def get_value_by_index_c(self, index):
        count = 0
        aux_queue = Queue()

        while self.data != None:
            if count == index:
                value = self.remove()
                aux_queue.insert(value)
            aux_queue.insert(self.remove())
            count += 1
        while aux_queue.data != None:
            self.insert(aux_queue.remove())

        return value

    def get_value_by_index_d(self, index):
        array = self.array_conversion
        return array[index]

    def get_index_by_value_c(self, value):
        count = 0
        aux_queue = Queue()
        while self.data != value:
            
            aux_queue.insert(self.remove())
            count += 1
            index = count

        self.self_to_aux(aux_queue)
        
        self.aux_to_self(aux_queue)

        return index
    def get_index_by_value_d(self, value):
        array = self.array_conversion()

        return array.index(value)
    
    def get_all_indexs_by_value_c(self, value):
        aux_queue = Queue() 
        count = 0
        array_of_indexs = []


        while self.data != None:
            if self.data == value:
                array_of_indexs.append(count)
            aux_queue.insert(self.remove())
            count += 1

        self.aux_to_self(aux_queue)

        return array_of_indexs

    def get_all_indexs_by_value_d(self, value):
        array = self.array_conversion()
        
        values = np.array(array)
        array_of_indexs = np.where(values == value)[0]

        return array_of_indexs
    def get_values_by_indexs_c(self, indexes):
        array_of_values = []
        count = 0
        aux_queue = Queue()

        while self.data != None:
            if count in indexes:
                array_of_values.append(self.data)
            aux_queue.insert(self.remove())
            count += 1
            
        self.aux_to_self(aux_queue)
        return array_of_values

    def get_values_by_indexs_d(self, indexes):
        array = self.array_conversion()
        array_of_values = []

        for i in range(self.len_d()):
            if i in indexes:
                array_of_values.append(array[i])
        return array_of_values

    def get_values_by_slice_c(self, start, end):
        aux_queue = Queue()
        count = 0
        array_of_values = []

        while self.data != None:
            if count == start:
                while count < end:
                    array_of_values.append(self.data)
                    aux_queue.insert(self.remove())
                    count += 1
            aux_queue.insert(self.remove())
            count += 1
        
        self.aux_to_self(aux_queue)

        return array_of_values
                
    def get_values_by_slice_d(self, start, end):
        array = np.array(self.array_conversion())

        return array[start:end]

    def remove_all_c(self):
        while self.data != None:
            self.remove()

    def remove_all_d(self):
        self.data = None
        self.next = None

    def remove_by_index_c(self, index):
        aux_queue = Queue()
        count = 0

        while self.data != None:
            if count == index:
                self.remove()
            aux_queue.insert(self.remove())
            count += 1
        
        self.aux_to_self(aux_queue)
    def remove_by_index_d(self, index):

        #acha e retira o elemento do array
        array = self.array_conversion()
        array.pop(index)

        
        #esvazia a lista
        self.remove_all_d()

        #devolve os valores para a lista
        if self.data == None:
            self.data = array[0]
        for i in range(1, len(array)):
            f = Queue(array[i], None)

            aux_queue = self

            while aux_queue.next != None:
                aux_queue = aux_queue.next
            
            aux_queue.next = f
        
    def remove_by_value_c(self, value):
        aux_queue = Queue()
        while self.data != None:
            if self.data == value:
                self.remove()
            aux_queue.insert(self.remove())
        
        self.aux_to_self(aux_queue)


    def remove_by_value_d(self, value):
        array = self.array_conversion()

        array.remove(value)

        self.remove_all_d()

        #devolve os valores para a lista
        if self.data == None:
            self.data = array[0]
        for i in range(1, len(array)):
            f = Queue(array[i], None)

            aux_queue = self

            while aux_queue.next != None:
                aux_queue = aux_queue.next
            
            aux_queue.next = f

    def remove_all_by_value_c(self, value):
        aux_queue = Queue()

        while self.data != None:
            if self.data == value:
                self.remove()
            aux_queue.insert(self.remove())
        
        self.aux_to_self(aux_queue)

    def remove_all_by_value_d(self, value):
        array = self.array_conversion()
        aux_array = []

        for i in range(len(array)):
            if value != array[i]:
                aux_array.append(array[i])

        self.remove_all_d()
        
        if self.data == None:
            self.data = aux_array[0]
        for i in range(1, len(aux_array)):
            f = Queue(aux_array[i], None)

            aux_queue = self

            while aux_queue.next != None:
                aux_queue = aux_queue.next
            
            aux_queue.next = f

    def remove_all_by_indexes_c(self, indexes):
        aux_queue = Queue()
        count = 0
        
        while self.data != None:
            if count in indexes:  
                self.remove()
            else:
                aux_queue.insert(self.remove())            
            count += 1

        self.aux_to_self(aux_queue)
        
    def remove_all_by_indexes_d(self, indexes):
        array = self.array_conversion()

        for index in indexes:
            array.pop(index)

        self.rebuild_queue(array)

    def remove_all_by_slice_c(self, start, end):
        aux_queue = Queue()
        count = 0

        while self.data != None:
            if count == start:
                while count <= end:
                    self.remove()
                    count += 1
            aux_queue.insert(self.remove())
            count += 1
        
        self.aux_to_self(aux_queue)


    def remove_all_by_slice_d(self, start, end):
        array = self.array_conversion()
        new_array = array[:start] + array[end:]

        self.rebuild_queue(new_array)

    def set_value_in_index_c(self, index, value):
        aux_queue = Queue()
        count = 0

        while self.data != None:
            if count == index:
                self.data = value
            count += 1
            aux_queue.insert(self.remove())
        
        self.aux_to_self(aux_queue)

    def set_value_in_index_d(self, index, value):
        array = self.array_conversion()

        array[index] = value

        self.rebuild_queue(array)

    def set_values_in_indexes(self, indexes, values):
        aux_queue = Queue()
        count = 0

        
        while self.data != None:
            if count in indexes:
                self.data = values[indexes.index(count)]
            count += 1
            aux_queue.insert(self.remove())

        self.aux_to_self(aux_queue)

    def set_values_in_indexes_d(self, indexes, values):

        array = self.array_conversion()
        count = 0
        for index in indexes:
            array[index] = values[indexes.index(index)]
            count += 1

        self.rebuild_queue(array)

def popular_fila(fila):
    for i in range(8):
        fila.insert(i)

queue = Queue()

popular_fila(queue)
print(queue.array_conversion())

print(queue.first_c())
print(queue.first_d())

print(queue.array_conversion())

print(queue.is_empty_c())
print(queue.is_empty_d())


print(queue.len_c())
print(queue.len_d())

print(queue.last_c())
print(queue.last_d())
print(queue.array_conversion())

print(queue.get_value_by_index_c(4))
print(queue.get_value_by_index_c(4))

print(queue.array_conversion())

print(queue.get_index_by_value_c(5))

print(queue.get_index_by_value_d(5))

queue.insert(3)
print(queue.array_conversion())

print(queue.get_all_indexs_by_value_c(3))
print(queue.get_all_indexs_by_value_d(3))

indexs = [2,3,5,1, 8]
print(queue.get_values_by_indexs_c(indexs))
print(queue.get_values_by_indexs_d(indexs))

print(queue.array_conversion())

print(queue.get_values_by_slice_c(2,5))
print(queue.array_conversion())

print(queue.get_values_by_slice_d(2,5))

queue.remove_all_c()
print(queue.array_conversion())

popular_fila(queue)

queue.remove_all_d()
print(queue.array_conversion())

popular_fila(queue)
print(queue.array_conversion())

queue.remove_by_index_c(3)
print(queue.array_conversion())


print(queue.remove_by_index_d(1))
print(queue.array_conversion())

print(queue.remove_by_value_c(2))
print(queue.array_conversion())

queue.remove_by_value_d(4)
print(queue.array_conversion())

popular_fila(queue)
print(queue.array_conversion())

queue.remove_all_by_value_c(5)
print(queue.array_conversion())

queue.remove_all_by_value_d(0)
print(queue.array_conversion())

indexes = [0, 3, 5, 6]
queue.remove_all_by_indexes_c(indexes)
print(queue.array_conversion())

popular_fila(queue)
print(queue.array_conversion())

queue.remove_all_by_indexes_d(indexes)
print(queue.array_conversion())

queue.remove_all_by_slice_c(2,5)
print(queue.array_conversion())

popular_fila(queue)
print(queue.array_conversion())

queue.remove_all_by_slice_d(2,5)
print(queue.array_conversion())

queue.set_value_in_index_c(1, 1)
print(queue.array_conversion())

queue.set_value_in_index_d(3, 1)
print(queue.array_conversion())

indexes = [4, 5, 6]
values = [1, 1, 1]

queue.set_values_in_indexes(indexes, values)
print(queue.array_conversion())

indexes = [7, 8]
values = [1,1]
queue.set_values_in_indexes_d(indexes, values)
print(queue.array_conversion())
