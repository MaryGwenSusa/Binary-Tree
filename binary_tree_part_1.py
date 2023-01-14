class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data) #if self.left already has a value--recursively call the function to create another small subtree with another child value
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data) #if self.right already has a value--recursively call the function to create another small subtree with another child value
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        #returns the nodes in ascending order
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #visit base/root node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            #val might be in left subtree
            if self.left:
                """recursion"""
                return self.left.search(val) 
            else:
                return False
        
        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

        

def build_tree(elements):
    #helper method - takes elements as inputs
    root = BinarySearchTreeNode(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    #main method to execute a coroutine on the default event loop?
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    #print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(105))
