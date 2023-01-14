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

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    
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
    
    def find_min(self):
        """goes to the left subtree's leftmost node"""
        if self.left is None: #checks if the current level of the subtree still has a left node child
            return self.data #returns the leftmost node value
        return self.left.find_min()
    
    def find_max(self):
        """goes to the right subtree's rightmost node"""
        if self.right is None: #checks if the current level of the subtree still has a right node child
            return self.data #returns the righmost node value
        return self.right.find_max()

    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum = 0
        if self.right:
            right_sum = self.right.calculate_sum()  
        else:
            right_sum = 0
        return self.data + left_sum + right_sum
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val) #this recursive approach will be useful to shortened the code and lessen nested if-else/elif conditionals
            #no need for these code since python will automatically do this
            #else:
            #   return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None: #regards to no child node at all
                return None
            if self.left is None: #this is for when there is only one child
                return self.right
            if self.right is None: #this is for when there is only one child
                return self.left
            
            #min_val = self.right.find_min()
            #self.data = min_val
            #self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
            
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
    #print(numbers_tree.search(105))

    #print("Min:",numbers_tree.find_min())
    #print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    #print("In Order Traversal: \n", numbers_tree.in_order_traversal())
    #print("Pre-Order Traversal: \n", numbers_tree.pre_order_traversal())
    #print("Post-Order Traversal: \n", numbers_tree.post_order_traversal())
    



