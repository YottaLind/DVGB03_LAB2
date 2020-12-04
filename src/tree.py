#!/usr/bin/env python3

import sys
import logging

log = logging.getLogger(__name__)


class BinarySearchTree:

    value = None

    left = None
    right = None

    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None.
        '''
        self.value = value

        if not self.empty():
            self.construct(BinarySearchTree(), BinarySearchTree())

    def construct(self, left, right):
        '''
        Constructs a tree rooted at `self`.
        '''
        self.left = left
        self.right = right
        return self

    def empty(self):
        '''
        True if the tree is empty.
        '''
        return self.value is None

    def find(self, value):
        '''
        True if `value` exist in the tree.
        '''
        if self.empty():
            return False
        if self.value == value:
            return True
        if self.value < value:
            return self.right.find(value)
        else:
            return self.left.find(value)

    def size(self):
        '''
        Number of nodes in the tree.
        '''
        if self.empty():
            return 0
        else:
            left = self.left.height()
            right = self.right.height()
            return 1 + left + right

    def height(self):
        '''
        Maximal height of the tree.
        '''
        if self.empty():
            return 0
        else:
            left = self.left.height()
            right = self.right.height()
            return 1 + max(left, right)

    def preorder(self):
        '''
        List of members in preorder.
        '''
        if self.empty():
            return []
        else:
            return [self.value] + self.left.preorder() + self.right.preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.empty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.empty():
            return []
        else:
            return self.left.inorder() + self.right.inorder() + [self.value]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        log.info("TODO@src/bst.py: implement bfs_order_star()")
        return []

    def add(self, value):
        '''
        Add `value` if not already present in tree.
        '''
        if self.empty():
            self.__init__(value=value)
            return self

        if value < self.value:
            return self.construct(self.left.add(value), self.right)

        if value > self.value:
            return self.construct(self.left, self.right.add(value))

        return self

    def remove(self, value):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''

        # base case: key found not in tree
        if self.empty():
            return self

        # if given key is less than the root node, recur for left subtree
        if value < self.value:
            self.left.remove(value)

        # if given key is more than the root node, recur for right subtree
        elif value > self.value:
            self.right.remove(value)

        # key found
        else:

            # Case 1: node to be deleted has no children (it is a leaf node)
            if self.left is None and self.right is None:
                # update root to None
                self = None
                return self

            # Case 2: node to be deleted has two children
            elif self.left and self.right:
                # find its in-order predecessor node
                predecessor = self.left.maximum()

                # Copy the value of predecessor to current node
                self.value = predecessor.value

                # recursively delete the predecessor. Note that the
                # predecessor will have at-most one child (left child)
                self.left.remove(predecessor.value)

            # Case 3: node to be deleted has only one child
            else:
                # find child node
                child = self.left if self.left else self.right
                self = child

        return self

    def maximum(self):
        '''
        Maximum node of tree
        '''
        if self.right is None:
            return self
        else:
            return self.right.maximum()
