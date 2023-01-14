from binary_tree_part_1 import(BinarySearchTreeNode, build_tree)

if __name__ == '__main__':
    #main method to execute a coroutine on the default event loop?
    nameLetters = ["m", "a", "r", "y", "g", "w", "e", "n", "g", "s", "u", "s", "a"]
    nameTree = build_tree(nameLetters)
    
    print(nameTree.search("G"))
    print(nameTree.search("g"))
    print("Min:",nameTree.find_min())
    print("Max:",nameTree.find_max())
    print("In Order Traversal: \n", nameTree.in_order_traversal())
    print("Pre-Order Traversal: \n", nameTree.pre_order_traversal())
    print("Post-Order Traversal: \n", nameTree.post_order_traversal())