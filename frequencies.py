"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections
def frequencies(items):
    newitems = collections.Counter(items)

    return dict(newitems)
