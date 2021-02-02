'''
AVL Trees
Name: Liam Bok
'''

import random as r      # To use for testing

class Node:

    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None    # The root Node of the tree
        self.size = 0       # The number of Nodes in the tree

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def visual(self):
        """
        Returns a visual representation of the AVL Tree in terms of levels
        :return: None
        """
        root = self.root
        if not root:
            print("Empty tree.")
            return
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = self.height(self.root)
        for i in range(h+1):
            track[i] = []
        while bfs_queue:
            node = bfs_queue.pop(0)
            track[node[1]].append(node)
            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
        for i in range(h+1):
            print(f"Level {i}: ", end='')
            for node in track[i]:
                print(tuple([node[0], node[2]]), end=' ')
            print()

    def insert(self, node, value):
        """
        Add node with given value to the tree
        :param node: root node of tree
        :param value: value of new node being inserted
        """
        # If tree is empty
        if self.root is None:
            self.root = Node(value)
            self.root.value = value
            self.size += 1
            self.root.parent = None
            return
        if self.root.value == value:
            return
        if node.value == value:
            return
        # Find correct position for node
        elif node.value < value:
            if node.right is not None:
                return self.insert(node.right, value)
            else:
                node.right = Node(value)
                node.right.parent = node
        else:
            if node.left is not None:
                return self.insert(node.left, value)
            else:
                node.left = Node(value)
                node.left.parent = node
        # Increase size, update height, and rebalance tree
        self.size += 1
        self.update_height(node)
        node = node.parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

    def remove(self, node, value):
        """
        Remove node with value from tree if found, otherwise do nothing
        :param node: root node
        :param value: value being searched for to remove
        :return: root of subtree
        """
        if node is None:
            return None
        if node.parent is not None:
            par = node.parent
            cur = node
        else:
            par = None
            cur = node
        # Search for node being removed
        if cur is not None:
            # Node is found
            if cur.value == value:
                if not cur.left and not cur.right:
                    # Remove root node which is last node in tree
                    if not par and self.size == 1:
                        self.root = None
                        self.size = 0
                        return
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None
                elif not par and self.size > 1 and self.size <= 3:
                    if not cur.left and cur.right:
                        self.root.value = cur.right.value
                        cur.right = None
                        self.size -= 1
                    elif cur.left:
                        self.root.value = cur.left.value
                        cur.left = None
                        self.size -= 1
                # Remove node with only left child
                elif cur.left and not cur.right:
                    if not par:
                        node = cur.left
                    elif par.left == cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left
                # Remove node with only right child
                elif not cur.left and cur.right:
                    if not par:
                        node = cur.right
                    elif par.left == cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right
                # Remove node with two children
                else:
                    # Find successor (maximum value of left subtree)
                    suc = self.max(node.left)

                    successorData = suc
                    # Remove the successor from its original position and replace with node being removed
                    self.remove(node, suc.value)
                    node.value = successorData.value
                    self.update_height(node)
                while node is not None:
                    self.rebalance(node)
                    node = node.parent
                return self.root
            # Search right or left of tree based on value
            elif cur.value < value:
                par = cur
                cur = cur.right
                self.remove(cur, value)
            else:
                par = cur
                cur = cur.left
                self.remove(cur, value)

            # Recalculate size before return
            num_of_nodes = self.inorder(node)
            size = 0
            for i in num_of_nodes:
                size += 1
            self.size = size
            # Node not found
            return

    def search(self, node, value):
        """
        Search for node with passed value
        :param node: root node
        :param value: value being searched for
        :return: node with given value if found, otherwise potential parent node
        """
        temp = None
        while node is not None:
            if value == node.value:
                return node
            elif value < node.value:
                temp = node
                node = node.left
            else:
                temp = node
                node = node.right
        return temp

    def inorder(self, node):
        """
        Traverse tree using inorder method
        :param node: root node
        :return: generator object of traversed tree
        """
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node
        yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Traverse tree using preorder method
        :param node: root node
        :return: generator object of traversed tree
        """
        if node is None:
            return
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node):
        """
        Traverse tree using postorder method
        :param node: root node
        :return: generator object of traversed tree
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node

    def depth(self, value):
        """
        Get depth of node with given value
        :param value: value of node
        :return: depth of node
        """
        res = -1
        if self.root is None:
            return res
        elif self.root.value == value:
            return 0
        else:
            temp = 0
            node = self.root
            while node is not None:
                if value == node.value:
                    return temp
                elif value < node.value:
                    temp += 1
                    node = node.left
                else:
                    temp += 1
                    node = node.right
            return res

    def height(self, node):
        """
        Get height of tree rooted at node passed in
        :param node: root node passed in
        :return: height of tree at node
        """
        if node is None:
            return -1
        else:
            return node.height

    def min(self, node):
        """
        Get the minimum value of the AVL tree
        :param node: root node
        :return: minimum value
        """
        if node is None or node.left is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """
        Get the maximum value of the AVL tree
        :param node: root node
        :return: maximum value
        """
        if node is None or node.right is None:
            return node
        else:
            return self.max(node.right)

    def get_size(self):
        """
        Get the size of the AVL tree
        :return: size of AVL tree
        """
        return self.size

    def get_balance(self, node):
        """
        Get balance factor of node passed in
        :param node: node passed in to get balance factor
        :return: balance factor
        """
        if node is None:
            return 0
        else:
            left_h = -1
            if node.left is not None:
                left_h = self.height(node.left)
            right_h = -1
            if node.right is not None:
                right_h = self.height(node.right)
            return left_h - right_h

    def left_rotate(self, root):
        """
        Perform AVL left rotation on subtree rooted at root
        :param root: root of subtree
        :return: root of new subtree
        """
        rightLeftChild = root.right.left
        if root.parent is not None:
            self.replace_child(root.parent, root, root.right)
        else:
            self.root = root.right
            self.root.parent = None
        self.set_child(root.right, "left", root)
        self.set_child(root, "right", rightLeftChild)

    def right_rotate(self, root):
        """
        Perform AVL right rotation on subtree rooted at root
        :param root: root of subtree
        :return: root of new subtree
        """
        leftRightChild = root.left.right
        if root.parent is not None:
            self.replace_child(root.parent, root, root.left)
        else:
            self.root = root.left
            self.root.parent = None
        self.set_child(root.left, "right", root)
        self.set_child(root, "left", leftRightChild)

    def rebalance(self, node):
        """
        Rebalance subtree at root node if needed
        :param node: root node
        :return: root of new balanced tree
        """
        self.update_height(node)
        if self.get_balance(node) == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
            return self.left_rotate(node)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
            return self.right_rotate(node)
        return node

    def update_height(self, node):
        """
        Update the heights of each node
        :param node: root node passed in
        """
        left_h = -1
        if node.left is not None:
            left_h = self.height(node.left)
        right_h = -1
        if node.right is not None:
            right_h = self.height(node.right)
        node.height = max(left_h, right_h) + 1

    def set_child(self, parent, whichChild, child):
        """
        Set new child node for rotation functions
        :param parent: parent node
        :param whichChild: which child needs to be set
        :param child: child node to be set
        :return: True or False, depending if function is fully executed
        """
        if whichChild != "left" and whichChild != "right":
            return False
        if whichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        self.update_height(parent)
        return True

    def replace_child(self, parent, curChild, newChild):
        """
        Determine which child needs to be replaced for rotation functions
        :param parent: parent node
        :param curChild: current child of parent node
        :param newChild: new child of parent node
        :return: True or False, depending if function is fully executed
        """
        if parent.left == curChild:
            return self.set_child(parent, "left", newChild)
        elif parent.right == curChild:
            return self.set_child(parent, "right", newChild)
        return False

def repair_tree(tree):
    """
    Repairs tree by finding if two values have been swapped, and swapping them back if needed
    :param tree: AVL tree to be repaired
    """
    if tree.size <= 1:
        return
    node_list = list(tree.inorder(tree.root))
    i = 0
    prev = node_list[i]
    prev_a = None
    prev_b = None
    swap_a = None
    swap_b = None
    # Go through list of nodes and find two values that have been swapped
    for node in node_list[1:]:
        prev = node_list[i]
        if node.value < prev.value and swap_a is None:
            swap_a = prev
            prev_a = node
        elif node.value < prev.value and swap_a is not None:
            swap_b = node
            prev_b = prev
        if swap_a is not None and swap_b is not None:
            temp = swap_a.value
            swap_a.value = swap_b.value
            swap_b.value = temp
            return
        i += 1
    # Cases where tree only contains root with one or two children
    if swap_a is not None:
        temp = prev_a.value
        prev_a.value = swap_a.value
        swap_a.value = temp

