from binary_tree_part_1 import(
    BinarySearchTreeNode,
    build_tree,  
)

if __name__ == '__main__':
    #main method to execute a coroutine on the default event loop?
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    
    print("UK is in the list?", country_tree.search("UK"))
    print("Sweden is in the list?", country_tree.search("Sweden"))

    print(country_tree.in_order_traversal())


