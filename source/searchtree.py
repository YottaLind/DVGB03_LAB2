#!/usr/bin/env python3

import logging

log = logging.getLogger(__name__)


class BinarySearchTree():
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
        Returns true if the tree is empty.
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

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.empty():
            return False
        else:
            if v < self.value:
                if self.left == None:
                    return False
                return self.left.is_member(v)
            elif v > self.value:
                if self.right == None:
                    return False
                return self.right.is_member(v)
            else:
                return True

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

    def removeNode(self):
        if self.left.empty() and self.right.empty():
            self.value = None
            return self.construct(None, None)

        elif self.left.empty() and not self.right.empty():
            self.value = self.right.value
            return self.construct(self.right.left, self.right.right)

        elif not self.left.empty() and self.right.empty():
            self.value = self.left.value
            return self.construct(self.left.left, self.left.right)

        elif not self.left.empty() and not self.right.empty():
            self.smallest = self.minimum()
            self.value = self.smallest.value
            self.smallest.removeNode()
            return self

    def remove(self, value):
        '''
        Removes the value `value` from the tree and returns the new (updated) tree.
        If `value` is a non-member, the same tree is returned without modification.
        '''
        if self.empty() or not self.find(value):
            return self
        elif value < self.value:
            return self.construct(self.left.remove(value), self.right)
        elif value > self.value:
            return self.construct(self.left, self.right.remove(value))
        else:
            return self.removeNode()

    def minimum(self):
        '''
        Minimum node of tree
        '''
        current = self
        while current.left != None:
            current = current.left
        return current

    def maximum(self):
        '''
        Maximum node of tree
        '''
        if self.right is None:
            return self
        else:
            return self.right.maximum()
