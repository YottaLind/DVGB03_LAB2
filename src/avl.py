#!/usr/bin/env python3

import sys
import bst


class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, value):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        super().add(value)
        return self.balance()

    def delete(self, value):
        super().delete(value)
        return self.balance()

    def check(self):
        left = self.lc().height() if self.lc() is not None else 0
        right = self.rc().height() if self.rc() is not None else 0

        return left - right

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        balance = self.check()

        if balance == 2:
            if self.lc().check() >= 0:
                return self.srr()
            else:
                return self.drr()
        elif balance == -2:
            if self.rc().check() <= 0:
                return self.slr()
            else:
                return self.dlr()
        else:
            return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        node = self.rc()
        self.set_rc(node.lc())
        node.set_lc(self)

        return node

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        node = self.lc()
        self.set_lc(node.rc())
        node.set_rc(self)

        return node

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr()
