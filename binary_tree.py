from numpy import array
from stack_elementar_2 import Stack_array


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
    def in_order(self, root):
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.data)
            res = res + self.in_order(root.right)
        return res

    def pre_order(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res
    
    def post_order(self, root):
        res = []

        if root:
            res = self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.data)
        return res

    def level_order(self, root):
        res = []
        level_array = []
        res.append(root)
        
        while len(res) > 0:
            level_array.append(res[-1].data)
            node = res.pop()

            if node.left:
                res.insert(0, node.left)
            if node.right:
                res.insert(0, node.right)

        return level_array
    
    def altura(self):
    
        if self.left is not None and self.right is not None:
            return max(self.left.altura(), self.right.altura()) + 1
        elif self.left is not None:
            return self.left.altura() + 1
        elif self.right is not None:
            return self.right.altura() + 1
        else:
            return 1
    
    def size(self, root):
        
        if self.data is None:
            return 0

        stack = Stack_array()
        stack.push(root)
        size = 1
        while stack.stack != []:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size
    
    def leafs(self, root):
        stack = Stack_array()
        stack.push(root)
        counter = 0

        while stack.stack != []:
            node = stack.pop()

            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
            if node.left and node.right is None:
                counter += 1
        return counter
    
    def is_complete(self, root):
        stack = Stack_array()
        stack.push(root)

        while stack.stack != []:
            node = stack.pop()

            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
            if node.left and node.right is None:
                return 'is not complete'
        return 'is complete'





        

                    
        

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(43)

#print(root.inorderTraversal(root))
print(root.in_order(root))
print(root.pre_order(root))
print(root.post_order(root))
print(root.level_order(root))
print(root.altura())
print(root.size(root))
print(root.leafs(root))
print(root.is_complete(root))