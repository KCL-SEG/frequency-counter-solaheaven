"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter
items = (['a','a','b','b','b','c'])
def frequencies(items):
    items = (['a','a','b','b','b','c'])
    newitems = []
    # Your code goes here
    for i in items:
        if i not in newitems:
            newitems.append(i)
            for j in range (len(newitems-1)):
                str(newitems[j]).count(str(items[i])) 
    return frequencies
