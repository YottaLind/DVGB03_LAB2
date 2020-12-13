#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)


class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, value):
        '''
        Returns true if the value `value` is a member of the tree.
        '''
        if self.is_empty():
            return False
        if self.value() == value:
            return True
        if self.value() < value:
            return self.rc().is_member(value)
        else:
            return self.lc().is_member(value)
        return False

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        else:
            left = self.lc().height()
            right = self.rc().height()
            return 1 + left + right

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        else:
            left = self.lc().height()
            right = self.rc().height()
            return 1 + max(left, right)

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        else:
            return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        else:
            return self.lc().inorder() + self.rc().inorder() + [self.value()]

    def noneroot(self, index, size):
        exclusion = []
        left_child = right_child = index

        while left_child <= size:
            exclusion.append(left_child)
            left_child = (2 * left_child) + 1

        while right_child <= size:
            exclusion.append(right_child)
            right_child = (2 * right_child) + 2

        return exclusion

    def bfs_list(self):

        queue = []
        temporary = []

        queue.append(self)

        while(len(queue) > 0):

            temporary.append(queue[0])
            node = queue.pop(0)

            if not node.lc().is_empty():
                queue.append(node.lc())

            if not node.rc().is_empty():
                queue.append(node.rc())

        return temporary

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).
        '''
        if self.is_empty():
            return []
        else:
            total = ((2**self.height()) - 1)

            bfsqueue = [None] * total
            tree = self.bfs_list()
            exclusion = []

            for index in range(total):
                if index not in exclusion:
                    if len(tree) > 0:
                        node = tree.pop(0)

                        bfsqueue[index] = node.value()

                        if node.lc().is_empty():
                            index_left = (2 * index) + 1
                            exclusion += self.noneroot(index_left, total)

                        if node.rc().is_empty():
                            index_right = (2 * index) + 2
                            exclusion += self.noneroot(index_right, total)

            return bfsqueue

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self

    def _removeNode(self):
        if self.lc().is_empty() and self.rc().is_empty():
            self._value = None
            return self.construct(None, None)

        elif self.lc().is_empty() and not self.rc().is_empty():
            self._value = self.rc().value()
            return self.construct(self.rc().lc(), self.rc().rc())

        elif not self.lc().is_empty() and self.rc().is_empty():
            self._value = self.lc().value()
            return self.construct(self.lc().lc(), self.lc().rc())

        elif not self.lc().is_empty() and not self.rc().is_empty():
            self.smallest = self.minimum()
            self._value = self.smallest.value()
            self.smallest._removeNode()
            return self

    def delete(self, value):
        '''
        Removes the value `value` from the tree and returns the new (updated) tree.
        If `value` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty() or not self.is_member(value):
            return self
        elif value < self.value():
            return self.construct(self.lc().delete(value), self.rc())
        elif value > self.value():
            return self.construct(self.lc(), self.rc().delete(value))
        else:
            return self._removeNode()

    def minimum(self):
        '''
        Minimum node of tree
        '''
        if self.lc() is None:
            return self
        else:
            return self.lc().minimum()

    def maximum(self):
        '''
        Maximum node of tree
        '''
        if self.rc() is None:
            return self
        else:
            return self.rc().maximum()


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
