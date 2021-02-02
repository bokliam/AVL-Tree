# AVL Tree Specifications

* insert(self, node, value):
*  Takes in a value to be added in the form of a node to the tree
*  Takes in the root of the (sub)tree the node will be added into
*  Do nothing if the value is already in the tree
*  Must be recursive
*  Balances the tree if it needs it
*  O(log(n)) time complexity, O(1)* space complexity

* remove(self, node, value):
*  Takes in a value to remove from the tree
*  Takes in the root of the (sub)tree the node will be removed from
*  Do nothing if the value is not found
*  When removing a value with two children, replace with the maximum of the left subtree
*  Return the root of the subtree
*  Must be recursive
*  Balances the tree if it needs it
*  O(log(n)) time complexity, O(1)* space complexity

* search(self, node, value):
*  Takes in a value to search for and a node which is the root of a given tree or subtree
*  Returns the node with the given value if found, else returns the potential parent node
*  O(log(n)) time complexity, O(1)* space complexity

* inorder(self, node):
*  Returns a generator object of the tree traversed using the inorder method of traversal starting at the given node
*  Points will be deducted if the return of this function is not a generator object (hint: yield and from)
*  Must be recursive
*  O(n) time complexity, O(n) space complexity

* preorder(self, node):
*  Same as inorder, only using the preorder method of traversal
*  O(n) time complexity, O(n) space complexity

* postorder(self, node):
*  Same as inorder, only using the postorder method of traversal
*  O(n) time complexity, O(n) space complexity

* depth(self, value):
*  Returns the depth of the node with the given value
*  O(height) time complexity, O(1) space complexity

* height(self, node):
*  Returns the height of the tree rooted at the given node
*  O(1) time complexity, O(1) space complexity

* min(self, node):
*  Returns the minimum of the tree rooted at the given node
*  Must be recursive
*  O(log(n)) time complexity, O(1)* space complexity

* max(self, node):
*  Returns the maximum of the tree rooted at the given node
*  Must be recursive
*  O(log(n)) time complexity, O(1)* space complexity

* get_size(self)
*  Returns the number of nodes in the AVL Tree
*  O(1) time complexity, O(1) space complexity

* get_balance(self, node):
*  Returns the balance factor of the node passed in
*  Balance Factor = height of left subtree – height of right subtree
*  O(1) time complexity, O(1) space complexity

* left_rotate(self, root):
*  Performs an AVL left rotation on the subtree rooted at root
*  Returns the root of the new subtree
*  O(1) time complexity, O(1) space complexity

* right_rotate(self, root):
*  Performs an AVL right rotation on the subtree rooted at root
*  Returns the root of the new subtree
*  O(1) time complexity, O(1) space complexity

* rebalance(self, node):
*  Rebalances the subtree rooted at node, if needed
*  Returns the root of the new, balanced subtree
*  O(1) time complexity, O(1) space complexity
 
* def repair_tree(tree):
*  Takes in a tree where two values may have been swapped, violating the BST property of nodes on the left being less than the parent node, and nodes on the right being larger than the parent node
*  Repairs the tree by finding if two values have actually been swapped, and swapping them back if necessary
*  O(n) time complexity, O(n) space complexity
*  Not taking into account space allocated on the call stack

