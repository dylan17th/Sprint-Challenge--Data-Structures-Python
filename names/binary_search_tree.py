"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: 
            return True

        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False 
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None: 
            node.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        my_list = []
        my_list.append(node)

        while len(my_list) > 0:

            current_node = my_list[0]

            if current_node.left is not None:
                my_list.append(current_node.left)
            if current_node.right is not None:
                my_list.append(current_node.right)
            print(current_node.value)
            my_list.pop(0)
         


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        my_stack = []
        my_stack.append(node)

        while len(my_stack) > 0:
            current_node = my_stack[-1]
            my_stack.pop()

            if current_node.right:
                my_stack.append(current_node.right)

            if current_node.left:
                my_stack.append(current_node.left)

            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)



if __name__ == '__main__':
    myBST = BSTNode(10)
    myBST.insert(5)
    myBST.insert(7)
    myBST.insert(15)
    myBST.insert(12)
    myBST.insert(14)
    myBST.insert(3)
    myBST.insert(4)
    myBST.dft_print(myBST)