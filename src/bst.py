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
        return [self.value()] + self.left.preorder() + self.right.preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        log.info("TODO@src/bst.py: implement inorder()")
        return []

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        log.info("TODO@src/bst.py: implement postorder()")
        return []

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

        if value < self.value():
            return self.construct(self.left.add(value), self.right)

        if value > self.value():
            return self.construct(self.left, self.right.add(value))

        return self

    def remove(self, value):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''

        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
