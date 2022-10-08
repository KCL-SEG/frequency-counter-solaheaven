"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections
def frequencies(items):
    newitems = [tuple(str(ele) for ele in sub) for sub in items]
    newitems = collections.Counter(items)

    return dict(newitems)
