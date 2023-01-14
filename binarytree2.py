from binary_tree_part_1 import(
    BinarySearchTreeNode,
    build_tree,  
)

if __name__ == '__main__':
    #main method to execute a coroutine on the default event loop?
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34, 18, 4])
    numbers_tree.delete(34)
    print("After deleting 20, ", numbers_tree.in_order_traversal())